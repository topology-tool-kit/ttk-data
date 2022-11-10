#!/usr/bin/env python

from paraview.simple import *

naturalImagepng = PNGSeriesReader(FileNames=["naturalImage.png"])

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=naturalImagepng)
computeDerivatives1.Scalars = ["POINTS", "PNGImage"]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.ResultArrayName = "gradient"
calculator1.Function = "mag(ScalarGradient)"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "gradient"]

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
persistenceThreshold.LowerThreshold = 6.0
persistenceThreshold.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator1,
    Constraints=persistenceThreshold,
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "gradient"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "gradient"]

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold3.Scalars = ["CELLS", "SeparatrixType"]
threshold3.ThresholdMethod = "Between"
threshold3.LowerThreshold = 1.0
threshold3.UpperThreshold = 1.0

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(
    Input=OutputPort(tTKMorseSmaleComplex1, 3),
)
tTKIdentifierRandomizer1.ScalarField = ["POINTS", "DescendingManifold"]

SaveData("Segmentation.vti", tTKIdentifierRandomizer1)
