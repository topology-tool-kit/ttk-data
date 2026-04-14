#!/usr/bin/env python

from paraview.simple import *

# create a new 'CSV Reader'
pointCloudcsv = CSVReader(FileName=["pointCloud.csv"])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=pointCloudcsv)
tableToPoints1.XColumn = "Points:0"
tableToPoints1.YColumn = "Points:1"
tableToPoints1.ZColumn = "Points:2"

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ["POINTS", "ignore arrays"]
gaussianResampling1.ResamplingGrid = [64, 64, 128]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=gaussianResampling1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = -0.1
threshold1.UpperThreshold = 999999999

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdMethod = "Between"
persistenceThreshold.LowerThreshold = 0.01
persistenceThreshold.UpperThreshold = 999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=gaussianResampling1, Constraints=persistenceThreshold
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.01
tTKMorseSmaleComplex1.ThresholdIsAbsolute = True

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=OutputPort(tTKMorseSmaleComplex1, 2))

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=tetrahedralize1)
tTKGeometrySmoother2.IterationNumber = 20
tTKGeometrySmoother2.InputMaskField = [None, ""]

# threshold the output surface
threshold5 = Threshold(Input=tTKGeometrySmoother2)
threshold5.Scalars = ['CELLS', 'SeparatrixFunctionMinimum']
threshold5.LowerThreshold = 0.2
threshold5.UpperThreshold = 1

SaveData("OutputSurface.vtu", threshold5)
