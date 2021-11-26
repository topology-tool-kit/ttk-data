#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
isabelvti = XMLImageDataReader(FileName=['isabel.vti'])

all_MT_group = []

scalarFields = ['velocityMag_02', 'velocityMag_03', 'velocityMag_04', 'velocityMag_05', 'velocityMag_30', 'velocityMag_31', 'velocityMag_32', 'velocityMag_33', 'velocityMag_45', 'velocityMag_46', 'velocityMag_47', 'velocityMag_48']
for scalarField in scalarFields:
  # create a new 'TTK Merge and Contour Tree (FTM)'
  tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(Input=isabelvti)
  tTKMergeandContourTreeFTM1.ScalarField = ['POINTS', scalarField]
  tTKMergeandContourTreeFTM1.TreeType = 'Split Tree'
  
  # create a new 'Group Datasets'
  groupDatasets1 = GroupDatasets(Input=[tTKMergeandContourTreeFTM1, OutputPort(tTKMergeandContourTreeFTM1,1), OutputPort(tTKMergeandContourTreeFTM1,2)])
  
  all_MT_group.append(groupDatasets1)

# create a new 'Group Datasets'
all_MT = GroupDatasets(Input=all_MT_group)

# create a new 'TTK MergeTreeTemporalReductionEncoding'
tTKMergeTreeTemporalReductionEncoding1 = TTKMergeTreeTemporalReductionEncoding(Input=all_MT)
tTKMergeTreeTemporalReductionEncoding1.RemovalPercentage = 75.0
tTKMergeTreeTemporalReductionEncoding1.Epsilon1 = 0.0
tTKMergeTreeTemporalReductionEncoding1.Epsilon2 = 100.0
tTKMergeTreeTemporalReductionEncoding1.Epsilon3 = 100.0
tTKMergeTreeTemporalReductionEncoding1.PersistenceThreshold = 3.0

SaveData('ReductionCoefficients.csv', OutputPort(tTKMergeTreeTemporalReductionEncoding1, 1))
