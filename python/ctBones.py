#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
ctBonesvti = XMLImageDataReader(FileName=["ctBones.vti"])

# create a new 'Calculator'
calculator1 = Calculator(Input=ctBonesvti)
calculator1.ResultArrayName = "Scalars_"
calculator1.Function = "-Scalars_"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "Scalars_"]
tTKPersistenceDiagram1.Dimensions = "Selected Dimensions (no infinite pairs)"
tTKPersistenceDiagram1.Saddlesaddlediagramdimension1slowest = False

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = 0.0
threshold1.UpperThreshold = 999999999

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 180.0
persistenceThreshold.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator1, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "Scalars_"]

# create a new 'TTK Merge and Contour Tree ()'
tTKMergeandContourTree1 = TTKMergeTree(
    Input=tTKTopologicalSimplification1
)
tTKMergeandContourTree1.ScalarField = ["POINTS", "Scalars_"]
tTKMergeandContourTree1.TreeType = "Join Tree"

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMergeandContourTree1, 2))
threshold3.Scalars = ["POINTS", "RegionType"]
threshold3.ThresholdMethod = "Between"
threshold3.LowerThreshold = 0.0
threshold3.UpperThreshold = 0.0

SaveData("CTBonesOutputSegmentation.vtu", threshold3)
