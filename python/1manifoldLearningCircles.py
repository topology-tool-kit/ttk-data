#!/usr/bin/env python

from paraview.simple import *

# create a new 'CSV Reader'
clustering0csv = CSVReader(FileName=["clustering0.csv"])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clustering0csv)
tableToPoints1.XColumn = "X"
tableToPoints1.YColumn = "Y"
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ["POINTS", "ignore arrays"]
gaussianResampling1.ResamplingGrid = [256, 256, 3]
gaussianResampling1.SplatAccumulationMode = "Sum"

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling1)
slice1.SliceType = "Plane"

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "SplatterValues"]
tTKPersistenceDiagram1.IgnoreBoundary = True

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = -0.1
threshold1.UpperThreshold = 999999999

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ["CELLS", "Persistence"]
persistenceThreshold0.ThresholdMethod = "Between"
persistenceThreshold0.LowerThreshold = 10.0
persistenceThreshold0.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=slice1, Constraints=persistenceThreshold0
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold2.Scalars = ["CELLS", "SeparatrixType"]
threshold2.ThresholdMethod = "Between"
threshold2.LowerThreshold = 1.0
threshold2.UpperThreshold = 1.0

# create a new 'Threshold'
threshold3 = Threshold(Input=threshold2)
threshold3.Scalars = ["CELLS", "SeparatrixFunctionMinimum"]
threshold3.ThresholdMethod = "Between"
threshold3.LowerThreshold = 2.0
threshold3.UpperThreshold = 999999999

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(
    SourceDataArrays=OutputPort(tTKMorseSmaleComplex1, 3),
    DestinationMesh=tableToPoints1,
)

# save the ouput
SaveData("Clustering.csv", resampleWithDataset1)
SaveData("Generators.vtu", threshold3)
