#!/usr/bin/env python

from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility ===========================================
def ThresholdBelow(threshold, value):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [-999999999, value]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Below Lower Threshold"
        threshold.LowerThreshold = value
# end of comphatibility ========================================================

# create a new 'XML PolyData Reader'
stonevtp = XMLPolyDataReader(FileName=['GroundWater.cdb/stone.vtp'])

# create a new 'Elevation'
fakeShadow = Elevation(Input=stonevtp)
fakeShadow.LowPoint = [0.13294358695786565, 0.08882809227819845, -0.018024881743751362]
fakeShadow.HighPoint = [0.06742407365289238, 0.018398674549435334, 0.138207120609427]

# create a new 'TTK IcosphereFromObject'
tTKIcosphereFromObject1 = TTKIcosphereFromObject(Object=stonevtp)

# create a new 'TTK CinemaImaging'
tTKCinemaImaging1 = TTKCinemaImaging(Dataset=fakeShadow,
    SamplingGrid=tTKIcosphereFromObject1)

# create a new 'TTK DepthImageBasedGeometryApproximation'
tTKDepthImageBasedGeometryApproximation1 = TTKDepthImageBasedGeometryApproximation(Input=tTKCinemaImaging1)
tTKDepthImageBasedGeometryApproximation1.DepthArray = ['POINTS', 'Depth']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKDepthImageBasedGeometryApproximation1)
threshold1.Scalars = ['CELLS', 'TriangleDistortion']
ThresholdBelow(threshold1, 0.02)

SaveData('CinemaImages.vtm', tTKCinemaImaging1)
SaveData('GeometryApproximatedStone.vtm', threshold1)
