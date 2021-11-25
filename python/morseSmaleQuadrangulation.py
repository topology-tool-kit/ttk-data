#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
rockerArmvtu = XMLUnstructuredGridReader(FileName=["rockerArm.vtu"])
rockerArmvtu.PointArrayStatus = ["OutputEigenFunctions"]

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
tTKPersistenceDiagram1.InputOffsetField = [None, ""]
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
tTKTopologicalSimplification1.InputOffsetField = [None, ""]
tTKTopologicalSimplification1.VertexIdentifierField = [None, ""]

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "Result"]
tTKMorseSmaleComplex1.OffsetField = ["POINTS", "Result"]

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(
    registrationName="TTKIdentifierRandomizer1",
    Input=OutputPort(tTKMorseSmaleComplex1, 3),
)
tTKIdentifierRandomizer1.ScalarField = ["POINTS", "MorseSmaleManifold"]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKIdentifierRandomizer1)

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints1.Radius = 0.01

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=OutputPort(tTKMorseSmaleComplex1, 1))
tTKGeometrySmoother1.IterationNumber = 5
tTKGeometrySmoother1.InputMaskField = [None, ""]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ["POINTS", "CellDimension"]
tube1.Vectors = [None, ""]
tube1.Radius = 0.004

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface2)

# create a new 'TTK MorseSmaleQuadrangulation'
tTKMorseSmaleQuadrangulation1 = TTKMorseSmaleQuadrangulation(
    Triangulatedsurface=tTKIdentifierRandomizer1,
    MorseSmalecriticalpoints=tTKMorseSmaleComplex1,
    MorseSmale1separatrices=OutputPort(tTKMorseSmaleComplex1, 1),
)
tTKMorseSmaleQuadrangulation1.DualQuadrangulation = 1

# create a new 'TTK QuadrangulationSubdivision'
tTKQuadrangulationSubdivision1 = TTKQuadrangulationSubdivision(
    registrationName="TTKQuadrangulationSubdivision1",
    Triangulatedsurface=OutputPort(tTKMorseSmaleComplex1, 3),
    Coarsequadrangulation=tTKMorseSmaleQuadrangulation1,
)
tTKQuadrangulationSubdivision1.Levelofsubdivisions = 3
tTKQuadrangulationSubdivision1.Numberofrelaxationiterations = 100

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKQuadrangulationSubdivision1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractSurface3)

# save the output
SaveData("Quadrangulation.vtp", generateSurfaceNormals2)
