#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
ctBonesvti = XMLImageDataReader(FileName=['ctBones.vti'])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=ctBonesvti)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Scalars_']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [0, 9999999.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [180.0, 255.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=ctBonesvti,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'Scalars_']

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(Input=tTKTopologicalSimplification1)
tTKMergeandContourTreeFTM1.ScalarField = ['POINTS', 'Scalars_']
tTKMergeandContourTreeFTM1.TreeType = 'Split Tree'

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMergeandContourTreeFTM1,2))
threshold3.Scalars = ['POINTS', 'RegionType']
threshold3.ThresholdRange = [1.0, 1.0]

SaveData("CTBonesOutputSegmentation.vtu", threshold3)
