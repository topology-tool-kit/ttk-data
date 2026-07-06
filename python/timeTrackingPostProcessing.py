#!/usr/bin/env python
from paraview.simple import *
import numpy as np
from vtk.util import numpy_support as ns
from paraview import servermanager as sm

# custom processing functions


def export_crater_profile(source, filename="crater_profile.csv", bin_size=2):
    by = ns.vtk_to_numpy(sm.Fetch(source).GetCellData().GetArray("by"))
    start = np.floor(by.min() / bin_size) * bin_size
    end = np.ceil(by.max() / bin_size) * bin_size
    nbins = int(round((end - start) / bin_size))
    edges = start + np.arange(nbins + 1) * bin_size
    centers = start + (np.arange(nbins) + 0.5) * bin_size
    counts, _ = np.histogram(by, bins=edges)
    np.savetxt(
        filename,
        np.column_stack([centers, -counts]),
        delimiter=",",
        header="X,Counts_neg",
        comments="",
        fmt="%.6g",
    )


def export_ejection_angle(source, filename="ejection_angle.csv"):
    cd = sm.Fetch(source).GetCellData()
    ax = ns.vtk_to_numpy(cd.GetArray("ax"))
    ay = ns.vtk_to_numpy(cd.GetArray("ay"))
    axial = -ax
    angle = np.degrees(np.arctan(ay / axial))
    np.savetxt(
        filename,
        np.column_stack([axial, angle]),
        delimiter=",",
        header="axial_velocity,ejection_angle",
        comments="",
        fmt="%.6g",
    )


# main pipeline

# create a new 'XML Image Data Reader'
impactvti = XMLImageDataReader(FileName=["hvi.vti"])

# create a new 'TTK TrackingFromFields'
tTKTrackingFromFields1 = TTKTrackingFromFields(Input=impactvti)
tTKTrackingFromFields1.Set(
    Persistencethreshold=7.0,
    Relativedestructioncost=0.02,
    Xweight=0.1,
    Yweight=0.9,
    Zweight=0.0,
    Fweight=0.1,
    ForceZtranslation=1,
    Enablepostprocessing=1,
    ChangeStartFrame=1,
    Maxlinkpx=15.0,
    Computemergetreesegmentation=1,
    Maxsurfacesize=100,
    Otsusimplification=1,
)

# create a new 'Threshold'
axial_velocity = Threshold(Input=tTKTrackingFromFields1)
axial_velocity.Set(
    Scalars=["CELLS", "ax"],
    LowerThreshold=-27.0,
    UpperThreshold=-0.001,
)

# create a new 'Threshold'
duration = Threshold(Input=axial_velocity)
duration.Set(
    Scalars=["CELLS", "Duration"],
    LowerThreshold=10.0,
    UpperThreshold=442.0,
)

# create a new 'Threshold'
minima = Threshold(Input=duration)
minima.Scalars = ["CELLS", "CriticalType"]
minima.LowerThreshold = 0.0
minima.UpperThreshold = 0.0

# create a new 'Threshold'
xBoxOrigin = Threshold(Input=minima)
xBoxOrigin.Set(
    Scalars=["CELLS", "bx"],
    LowerThreshold=250.0,
    UpperThreshold=420.0,
)

# create a new 'Threshold'
yBoxOrigin = Threshold(Input=xBoxOrigin)
yBoxOrigin.Set(
    Scalars=["CELLS", "by"],
    LowerThreshold=60.0,
    UpperThreshold=180.0,
)

export_crater_profile(yBoxOrigin)
export_ejection_angle(yBoxOrigin)

SaveData("debrisTrajectories.vtu", yBoxOrigin)
