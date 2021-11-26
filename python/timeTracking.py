#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Image Data Reader'
timeTrackingvti = XMLImageDataReader(FileName=['timeTracking.vti'])
timeTrackingvti.CellArrayStatus = []
# select data arrays 000, 002, 004, ..., 118
timeTrackingvti.PointArrayStatus = ['{:0>3}'.format(i) for i in range(0, 120, 2)] 

# create a new 'TTK TrackingFromFields'
tTKTrackingFromFields1 = TTKTrackingFromFields(Input=timeTrackingvti)
tTKTrackingFromFields1.ForceZtranslation = 1
tTKTrackingFromFields1.ZTranslation = 0.125

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKTrackingFromFields1)

# save the output
SaveData('timeTracking.vtp', extractSurface1)
