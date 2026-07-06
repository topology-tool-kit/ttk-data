# Time Tracking Post-Processing

## Pipeline description

This example loads a 2D time-varying scalar field, where time steps are
stored as a sequence of data arrays, and tracks its extrema over time with
[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html).
As in the [Time Tracking](https://topology-tool-kit.github.io/examples/timeTracking/)
and [Tracking From Critical Points](https://topology-tool-kit.github.io/examples/trackingFromCriticalPoints/)
examples, each extremum is followed from one time step to the next by solving
an optimal assignment problem between the persistence diagrams of consecutive
steps, controlled by the persistence threshold and the relative destruction
cost. Here, each tracked minimum captures an individual debris fragment
ejected by a hypervelocity impact, so that the raw output of the tracking is,
for every fragment, the sequence of its positions through the time-space
domain.

This example focuses on the post-processing stage of the filter (parameter
`Enablepostprocessing`), which turns these raw, frame-by-frame tracks into
clean, analyzable trajectories and enriches them with geometric attributes.
In particular, for each time step a merge-tree segmentation (parameter
`Computemergetreesegmentation`) isolates the region around every tracked
extremum and attaches to each trajectory the surface of its associated
feature, recovering a measure of its size in addition to its position.

The resulting trajectory mesh carries, for each fragment, its linearized
motion model (`ax`, `bx`, `ay`, `by`), its duration and its surface
statistics. A sequence of Threshold filters then isolates the fragments of
interest — by axial velocity (`ax`), duration (`Duration`), critical type
(minima) and spatial region of origin (`bx`, `by`) — and two derived plots
summarize the experiment: a crater profile, obtained by binning the impact
positions (`by`), and an ejection diagram, plotting the ejection angle
atan(`ay` / -`ax`) against the axial velocity -`ax`.

Beyond the two tracking parameters described in the other examples, the
post-processing is mainly tuned through the fusion and segmentation controls:
increase `Maxlinkpx` to allow longer reconnections between consecutive
trajectory segments (decrease it to keep only tight, unambiguous links), and
adjust `Maxsurfacesize` to bound the size of the segmented features (lower it
to discard oversized background regions). Enabling `Otsusimplification` is
recommended when the features sit on a noisy or slowly-varying background.

## ParaView

To reproduce the above screenshot, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter
the following command:

```
paraview states/timeTrackingPostProcessing.pvsm
```

## Python code

```python
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
```

To run the above Python script, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter
the following command:

```
pvpython python/timeTrackingPostProcessing.py
```

## Inputs

- hvi.vti:
  2D time-varying scalar field capturing debris fragments ejected by a
  hypervelocity impact, with each time step stored as a separate data array.

## Outputs

- `debrisTrajectories.vtu`: space-time trajectories of the selected debris
  fragments.
- `crater_profile.csv`: debris count binned by vertical impact position.
- `ejection_angle.csv`: ejection angle versus axial velocity per fragment.

## C++/Python API

[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html)

PostProcessingTracking
