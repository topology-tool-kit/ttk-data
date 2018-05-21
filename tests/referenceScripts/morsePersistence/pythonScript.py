from paraview.simple import *
if len(sys.argv) >= 2:
	outputDirectory = sys.argv[1] + '/'
	if len(sys.argv) == 3:
		debugLevel = sys.argv[2]
	else:
		debugLevel = 0
else:
	print('Missing output directory')
	sys.exit()
if debugLevel != 0:
	print('  Debug level: ' + debugLevel)
# state file generated using paraview version 5.5.0

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Plane'
plane1 = Plane()
plane1.XResolution = 300
plane1.YResolution = 300

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(Input=plane1)
randomAttributes1.DataType = 'Float'
randomAttributes1.ComponentRange = [0.0, 1.0]
randomAttributes1.GeneratePointScalars = 1
randomAttributes1.GenerateCellVectors = 0

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=randomAttributes1)
tTKScalarFieldSmoother1.ScalarField = 'RandomPointScalars'
tTKScalarFieldSmoother1.IterationNumber = 6

# create a new 'Calculator'
sine = Calculator(Input=tTKScalarFieldSmoother1)
sine.ResultArrayName = 'Sine'
sine.Function = 'sin(20*coordsX+1.5)+sin(20*coordsY+1.5)'

# create a new 'Calculator'
distanceField = Calculator(Input=sine)
distanceField.ResultArrayName = 'DistanceField'
distanceField.Function = '-sqrt(coordsX*coordsX+coordsY*coordsY)'

# create a new 'Calculator'
calculator1 = Calculator(Input=distanceField)
calculator1.ResultArrayName = 'Blend'
calculator1.Function = 'Sine+5*DistanceField+5*RandomPointScalars'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=calculator1)

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tetrahedralize1)
warpByScalar1.Scalars = ['POINTS', 'Blend']
warpByScalar1.ScaleFactor = 0.05

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=warpByScalar1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface1)

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=warpByScalar1)
tTKPersistenceCurve1.ScalarField = 'Blend'
tTKPersistenceCurve1.InputOffsetField = ''

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=warpByScalar1)
tTKPersistenceDiagram1.ScalarField = 'Blend'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold2)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface2)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [0.0, 100000.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.7, 10000.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 0.15

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.0799698305130005

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=warpByScalar1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'Blend'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'Blend'
tTKMorseSmaleComplex1.UseInputOffsetField = 1
tTKMorseSmaleComplex1.SaddleConnectors = 0
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint2.Radius = 0.02

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=OutputPort(tTKMorseSmaleComplex1_1,3))

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractSurface4)

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=OutputPort(tTKMorseSmaleComplex1_2,1))

# create a new 'Tube'
tube3 = Tube(Input=extractSurface5)
tube3.Scalars = ['POINTS', 'CellDimension']
tube3.Vectors = [None, '']
tube3.Radius = 0.005

# ----------------------------------------------------------------tTKScalarFieldSmoother1.DebugLevel = int(debugLevel)
if tTKScalarFieldSmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldSmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldSmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldSmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldSmoother1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldSmoother1)))
tTKPersistenceCurve1.DebugLevel = int(debugLevel)
if tTKPersistenceCurve1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceCurve1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceCurve1_' + str(i) + '.vtk',
			OutputPort(tTKPersistenceCurve1, i))
else:
	SaveData(outputDirectory + 'tTKPersistenceCurve1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceCurve1)))
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))
tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification1, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification1.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification1)))
tTKMorseSmaleComplex1.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex1, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex1.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex1)))
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
