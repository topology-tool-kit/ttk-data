#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Image Data Reader'
timeTrackingvti = XMLImageDataReader(FileName=["timeTracking.vti"])
timeTrackingvti.CellArrayStatus = []
# select data arrays 000, 002, 004, ..., 118
timeTrackingvti.PointArrayStatus = ["{:0>3}".format(i) for i in range(0, 120, 2)]

# create a new 'TTK TrackingFromFields'
tTKTrackingFromFields1 = TTKTrackingFromFields(Input=timeTrackingvti)
tTKTrackingFromFields1.ForceZtranslation = 1
tTKTrackingFromFields1.ZTranslation = 0.125
tTKTrackingFromFields1.Fweight = 1

# create a new 'Threshold', get the minimum trajectories
threshold1 = Threshold(Input=tTKTrackingFromFields1)
threshold1.Scalars = "CriticalType"
threshold1.LowerThreshold = 0.0
threshold1.UpperThreshold = 0.0

# create a new 'Threshold', get the maximum trajectories
threshold2 = Threshold(Input=tTKTrackingFromFields1)
threshold2.Scalars = "CriticalType"
threshold2.LowerThreshold = 3.0
threshold2.UpperThreshold = 3.0

# group minima and maxima trajectories
appendDatasets1 = AppendDatasets(Input=[threshold1, threshold2])

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=appendDatasets1)

# save the output
SaveData("timeTracking.vtp", extractSurface1)
