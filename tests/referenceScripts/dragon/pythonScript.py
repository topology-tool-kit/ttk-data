#!/usr/bin/env pvpython

from paraview.simple import *

if len(sys.argv) >= 2:
    inputFileBase = sys.argv[1]
    if len(sys.argv) == 3:
        debugLevel = sys.argv[2]
    else:
        debugLevel = 0;
else:
    print("Missing state file name")
    sys.exit()

outputDirectory = "tests/referenceOutputs/" + inputFileBase + "/"

print("Loading state '" + inputFileBase + "'...")
print("Output directory '" + outputDirectory + "'...")
if debugLevel != 0:
    print("  Debug level: " + debugLevel)

# create a new 'XML Unstructured Grid Reader'
dragonvtu = XMLUnstructuredGridReader(FileName=['dragon.vtu'])

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=dragonvtu)

# save the output
cleantoGrid_1 = CleantoGrid(Input=tTKGeometrySmoother1)
tTKGeometrySmoother1.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "geometrySmoother1.vtu", proxy=cleantoGrid_1)

# create a new 'Calculator'
elevation = Calculator(Input=tTKGeometrySmoother1)
elevation.ResultArrayName = 'Elevation'
elevation.Function = 'coordsY'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=elevation)
tTKPersistenceDiagram1.ScalarField = 'Elevation'
tTKPersistenceDiagram1.InputOffsetField = ''
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)

cleantoGrid_2 = CleantoGrid(Input=tTKPersistenceDiagram1)
SaveData(outputDirectory + "persistenceDiagram1.vtu", proxy=cleantoGrid_2)

# create a new 'Threshold'
pairs = Threshold(Input=tTKPersistenceDiagram1)
pairs.Scalars = ['CELLS', 'PairIdentifier']
pairs.ThresholdRange = [0.0, 9999.0]

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=elevation)
tTKPersistenceCurve1.ScalarField = 'Elevation'
tTKPersistenceCurve1.InputOffsetField = ''
tTKPersistenceCurve1.DebugLevel = int(debugLevel)

SaveData(outputDirectory + "persistenceCurve1_0.vtk", OutputPort(tTKPersistenceCurve1, 0))
SaveData(outputDirectory + "persistenceCurve1_1.vtk", OutputPort(tTKPersistenceCurve1, 1))
SaveData(outputDirectory + "persistenceCurve1_2.vtk", OutputPort(tTKPersistenceCurve1, 2))
SaveData(outputDirectory + "persistenceCurve1_3.vtk", OutputPort(tTKPersistenceCurve1, 3))

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=pairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [2.0, 1000.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=elevation,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'Elevation'
tTKTopologicalSimplification1.InputOffsetField = ''
tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "topologicalSimplification1.vtu", CleantoGrid(tTKTopologicalSimplification1))

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = 'Elevation'
tTKScalarFieldCriticalPoints1.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints1.Withvertexidentifiers = 0
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0
tTKScalarFieldCriticalPoints1.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "scalarFieldCriticalPoints1.vtu", CleantoGrid(tTKScalarFieldCriticalPoints1))

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 1.5
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "sphereFromPoint2.vtu", CleantoGrid(tTKSphereFromPoint2))

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKTopologicalSimplification1)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface3)

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKContourTree1 = TTKMergeandContourTreeFTM(Input=tTKTopologicalSimplification1)
tTKContourTree1.ScalarField = 'Elevation'
tTKContourTree1.UseInputOffsetScalarField = 1
tTKContourTree1.InputOffset = 'OutputOffsetScalarField'
tTKContourTree1.ArcSampling = 30
tTKContourTree1.DebugLevel = int(debugLevel)

SaveData(outputDirectory + "contourTree1_0.vtu", CleantoGrid(OutputPort(tTKContourTree1, 0)))
SaveData(outputDirectory + "contourTree1_1.vtu", CleantoGrid(OutputPort(tTKContourTree1, 1)))
SaveData(outputDirectory + "contourTree1_2.vtu", CleantoGrid(OutputPort(tTKContourTree1, 2)))


# find source
tTKContourTree1_1 = FindSource('TTKContourTree1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=OutputPort(tTKContourTree1,1))
tTKGeometrySmoother2.IterationNumber = 40
tTKGeometrySmoother2.UseInputMaskField = 1
tTKGeometrySmoother2.InputMaskField = 'RegularMask'
tTKGeometrySmoother2.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "geometrySmoother2.vtu", CleantoGrid(tTKGeometrySmoother2))

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKContourTree1)
tTKSphereFromPoint4.Radius = 2.0
tTKSphereFromPoint4.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "sphereFromPoint4.vtu", CleantoGrid(tTKSphereFromPoint4))

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 1.5
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
SaveData(outputDirectory + "sphereFromPoint1.vtu", CleantoGrid(tTKSphereFromPoint1))
