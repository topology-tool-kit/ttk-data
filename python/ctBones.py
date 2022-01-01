#!/usr/bin/env python

from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility ===========================================
def ThresholdAbove(threshold, value):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [value, 999999999]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Above Upper Threshold"
        threshold.UpperThreshold = value

def ThresholdAt(threshold, value):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [value, value]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Between"
        threshold.LowerThreshold = value
        threshold.UpperThreshold = value
# end of comphatibility ========================================================

# create a new 'XML Image Data Reader'
ctBonesvti = XMLImageDataReader(FileName=['ctBones.vti'])

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=ctBonesvti)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Scalars_']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
ThresholdAbove(threshold1, 0)

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
ThresholdAbove(persistenceThreshold, 180.0)

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
ThresholdAt(threshold3, 1.0)

SaveData("CTBonesOutputSegmentation.vtu", threshold3)
