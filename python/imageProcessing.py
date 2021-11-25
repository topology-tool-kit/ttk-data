#!/usr/bin/env python

from paraview.simple import *

naturalImagepng = PNGSeriesReader(FileNames=["naturalImage.png"])

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=naturalImagepng)
computeDerivatives1.Scalars = ["POINTS", "PNGImage"]
computeDerivatives1.Vectors = [None, ""]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.ResultArrayName = "gradient"
calculator1.Function = "mag(ScalarGradient)"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "gradient"]
tTKPersistenceDiagram1.InputOffsetField = [None, ""]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "PairIdentifier"]
threshold1.ThresholdRange = [-0.1, 59608.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold1)

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ["CELLS", "Persistence"]
persistenceThreshold.ThresholdRange = [6.0, 9999.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=persistenceThreshold)

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=extractSurface1)
tTKIcospheresFromPoints1.Radius = 0.65

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator1,
    Constraints=persistenceThreshold,
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "gradient"]
tTKTopologicalSimplification1.InputOffsetField = [None, ""]
tTKTopologicalSimplification1.VertexIdentifierField = [None, ""]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "gradient"]
tTKMorseSmaleComplex1.OffsetField = ["POINTS", "OutputOffsetScalarField"]

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold3.Scalars = ["CELLS", "SeparatrixType"]
threshold3.ThresholdRange = [1.0, 1.0]

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(
    Input=OutputPort(tTKMorseSmaleComplex1, 3),
)
tTKIdentifierRandomizer1.ScalarField = ["POINTS", "DescendingManifold"]

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ["CELLS", "PairIdentifier"]
threshold2.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold2)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface3)
tube1.Scalars = ["POINTS", "CriticalType"]
tube1.Vectors = ["POINTS", "Coordinates"]
tube1.Radius = 0.35

SaveData("Segmentation.vti", tTKIdentifierRandomizer1)
