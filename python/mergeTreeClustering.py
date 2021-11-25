#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
isabelvti = XMLImageDataReader(registrationName='isabel.vti', FileName=['isabel.vti'])
isabelvti.PointArrayStatus = ['velocityMag_02', 'velocityMag_03', 'velocityMag_04', 'velocityMag_05', 'velocityMag_30', 'velocityMag_31', 'velocityMag_32', 'velocityMag_33', 'velocityMag_45', 'velocityMag_46', 'velocityMag_47', 'velocityMag_48']
isabelvti.TimeArray = 'None'

all_JT_group = []
all_ST_group = []

for scalarField in isabelvti.PointArrayStatus:
  # create a new 'TTK Merge and Contour Tree (FTM)'
  tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(Input=isabelvti)
  tTKMergeandContourTreeFTM1.ScalarField = ['POINTS', scalarField]
  tTKMergeandContourTreeFTM1.InputOffsetField = ['POINTS', scalarField]
  tTKMergeandContourTreeFTM1.TreeType = 'Join Tree'
  
  # create a new 'Group Datasets'
  groupDatasets1 = GroupDatasets(Input=[tTKMergeandContourTreeFTM1, OutputPort(tTKMergeandContourTreeFTM1,1), OutputPort(tTKMergeandContourTreeFTM1,2)])
  
  all_JT_group.append(groupDatasets1)
  
  # create a new 'TTK Merge and Contour Tree (FTM)'
  tTKMergeandContourTreeFTM2 = TTKMergeandContourTreeFTM(Input=isabelvti)
  tTKMergeandContourTreeFTM2.ScalarField = ['POINTS', scalarField]
  tTKMergeandContourTreeFTM2.InputOffsetField = ['POINTS', scalarField]
  tTKMergeandContourTreeFTM2.TreeType = 'Split Tree'
  
  # create a new 'Group Datasets'
  groupDatasets2 = GroupDatasets(Input=[tTKMergeandContourTreeFTM2, OutputPort(tTKMergeandContourTreeFTM2,1), OutputPort(tTKMergeandContourTreeFTM2,2)])
  
  all_ST_group.append(groupDatasets2)

# create a new 'Group Datasets'
mt_JT_all = GroupDatasets(Input=all_JT_group)

# create a new 'Group Datasets'
mT_all = GroupDatasets(Input=all_ST_group)

# create a new 'TTK MergeTreeClustering'
tTKMergeTreeClustering1 = TTKMergeTreeClustering(Input=mT_all,
    OptionalInputclustering=mt_JT_all)
tTKMergeTreeClustering1.ComputeBarycenter = 1
tTKMergeTreeClustering1.NumberOfClusters = 3
tTKMergeTreeClustering1.Deterministic = 1
tTKMergeTreeClustering1.DimensionSpacing = 0.1
tTKMergeTreeClustering1.PersistenceThreshold = 2.0
tTKMergeTreeClustering1.ImportantPairs = 34.0
tTKMergeTreeClustering1.MaximumNumberofImportantPairs = 3
tTKMergeTreeClustering1.MinimumNumberofImportantPairs = 2
tTKMergeTreeClustering1.ImportantPairsSpacing = 15.0
tTKMergeTreeClustering1.NonImportantPairsProximity = 0.15

# create a new 'Group Datasets'
groupDatasets14 = GroupDatasets(Input=[tTKMergeTreeClustering1, OutputPort(tTKMergeTreeClustering1,1)])

# create a new 'TTK FlattenMultiBlock'
tTKFlattenMultiBlock2 = TTKFlattenMultiBlock(Input=groupDatasets14)

# create a new 'TTK MergeTreeDistanceMatrix'
tTKMergeTreeDistanceMatrix2 = TTKMergeTreeDistanceMatrix(Input=tTKFlattenMultiBlock2)
tTKMergeTreeDistanceMatrix2.PersistenceThreshold = 2.0

# create a new 'TTK DimensionReduction'
tTKDimensionReduction2 = TTKDimensionReduction(Input=tTKMergeTreeDistanceMatrix2,
    ModulePath='default')
tTKDimensionReduction2.InputColumns = ['Tree00', 'Tree01', 'Tree02', 'Tree03', 'Tree04', 'Tree05', 'Tree06', 'Tree07', 'Tree08', 'Tree09', 'Tree10', 'Tree11', 'Tree12', 'Tree13', 'Tree14']
tTKDimensionReduction2.InputIsaDistanceMatrix = 1
tTKDimensionReduction2.UseAllCores = 0

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=tTKDimensionReduction2)
tableToPoints1.XColumn = 'Component_0'
tableToPoints1.YColumn = 'Component_1'
tableToPoints1.ZColumn = 'Component_0'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=tableToPoints1)
tTKIcospheresFromPoints1.Radius = 0.4

# create a new 'Threshold'
threshold33 = Threshold(Input=tTKIcospheresFromPoints1)
threshold33.Scalars = ['POINTS', 'treeID']
threshold33.ThresholdRange = [0.0, 11.0]

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(Input=tableToPoints1)
tTKIcospheresFromPoints2.Radius = 0.8

# create a new 'Extract Block'
nodes_1 = ExtractBlock(Input=tTKMergeTreeClustering1)
nodes_1.BlockIndices = [14, 29, 8, 11, 26, 5, 20, 32, 23, 35, 2, 17]

# create a new 'Threshold'
threshold34 = Threshold(Input=tTKIcospheresFromPoints2)
threshold34.Scalars = ['POINTS', 'treeID']
threshold34.ThresholdRange = [12.0, 14.0]

# save the output
SaveData('MDS_trees.vtu', threshold33)
SaveData('MDS_centroids.vtu', threshold34)
