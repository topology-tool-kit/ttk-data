#!/usr/bin/env python

#### import the simple module from the paraview
from paraview.simple import *

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
mixingVonKarmanvti = XMLImageDataReader(FileName=['mixingVonKarman.vti'])
mixingVonKarmanvti.PointArrayStatus = ["sf_0{:0>3}".format(i) for i in range(0, 150, 1)]

# create a new 'TTK TrackingFromFields'
tTKTrackingFromFields1 = TTKTrackingFromFields(Input=mixingVonKarmanvti)
tTKTrackingFromFields1.Persistencethreshold = 10.0
tTKTrackingFromFields1.Relativedestructioncost = 0.01
tTKTrackingFromFields1.ForceZtranslation = 1
tTKTrackingFromFields1.ZTranslation = 0.02

# create a new 'Threshold'
minima = Threshold(Input=tTKTrackingFromFields1)
minima.Scalars = ['POINTS', 'CriticalType']
minima.LowerThreshold = 0.0
minima.UpperThreshold = 0.0

# create a new 'Threshold'
maxima = Threshold(Input=tTKTrackingFromFields1)
maxima.Scalars = ['POINTS', 'CriticalType']
maxima.LowerThreshold = 3.0
maxima.UpperThreshold = 3.0

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[maxima, minima])

# create a new 'Threshold'
threshold1 = Threshold(Input=appendDatasets1)
threshold1.Scalars = ['CELLS', 'ComponentLength']
threshold1.LowerThreshold = 40.0
threshold1.UpperThreshold = 9999.0

SaveData("mixingVonKarman.vtu", threshold1)
