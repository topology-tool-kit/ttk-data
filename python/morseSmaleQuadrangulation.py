#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
rockerArmvtu = XMLUnstructuredGridReader(FileName=["rockerArm.vtu"])

# create a new 'Extract Component'
extractComponent1 = ExtractComponent(Input=rockerArmvtu)
extractComponent1.InputArray = ["POINTS", "OutputEigenFunctions"]
extractComponent1.Component = 83

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=extractComponent1)
tTKScalarFieldNormalizer1.ScalarField = ["POINTS", "Result"]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKScalarFieldNormalizer1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "Result"]
tTKPersistenceDiagram1.EmbedinDomain = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "Persistence"]
threshold1.ThresholdRange = [0.001, 0.9999999403953552]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tTKScalarFieldNormalizer1, Constraints=threshold1
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "Result"]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "Result"]

# create a new 'TTK MorseSmaleQuadrangulation'
tTKMorseSmaleQuadrangulation1 = TTKMorseSmaleQuadrangulation(
    Triangulatedsurface=OutputPort(tTKMorseSmaleComplex1, 3),
    MorseSmalecriticalpoints=tTKMorseSmaleComplex1,
    MorseSmale1separatrices=OutputPort(tTKMorseSmaleComplex1, 1),
)
tTKMorseSmaleQuadrangulation1.DualQuadrangulation = 1

# create a new 'TTK QuadrangulationSubdivision'
tTKQuadrangulationSubdivision1 = TTKQuadrangulationSubdivision(
    Triangulatedsurface=OutputPort(tTKMorseSmaleComplex1, 3),
    Coarsequadrangulation=tTKMorseSmaleQuadrangulation1,
)
tTKQuadrangulationSubdivision1.Levelofsubdivisions = 3
tTKQuadrangulationSubdivision1.Numberofrelaxationiterations = 100

# save the output
SaveData("Quadrangulation.vtp", tTKQuadrangulationSubdivision1)
