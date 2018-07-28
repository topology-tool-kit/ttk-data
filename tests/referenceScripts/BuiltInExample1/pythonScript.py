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

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample1.vti'])
builtInExamplevti.PointArrayStatus = ['Vectors_']

# create a new 'Transform'
transform1 = Transform(Input=builtInExamplevti)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Rotate = [0.0, 0.0, -90.0]

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=transform1)
computeDerivatives1.Scalars = [None, '']
computeDerivatives1.Vectors = ['POINTS', 'Vectors_']
computeDerivatives1.OutputVectorType = 'Vorticity'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.ResultArrayName = 'myVorticity'
calculator1.Function = 'Vorticity_Z'

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = 'myVorticity'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=tTKScalarFieldNormalizer1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'myVorticity'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram1)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'Threshold'
persistencePairs = Threshold(Input=tTKPersistenceDiagram1)
persistencePairs.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs.ThresholdRange = [-0.1, 957.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=persistencePairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.02, 1.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 0.025
tTKSphereFromPoint1.ThetaResolution = 10

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint1)
tTKTopologicalSimplification1.ScalarField = 'myVorticity'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tTKTopologicalSimplification1)
warpByScalar1.Scalars = ['POINTS', 'myVorticity']
warpByScalar1.ScaleFactor = 300.0
warpByScalar1.UseNormal = 1

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.015

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=warpByScalar1)
tTKScalarFieldCriticalPoints1.ScalarField = 'myVorticity'

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 5.0

# create a new 'Threshold'
maxima = Threshold(Input=tTKSphereFromPoint2)
maxima.Scalars = ['POINTS', 'CriticalIndex']
maxima.ThresholdRange = [1.9, 2.0]

# create a new 'Threshold'
minima = Threshold(Input=tTKSphereFromPoint2)
minima.Scalars = ['POINTS', 'CriticalIndex']
minima.ThresholdRange = [0.0, 0.1]

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tetrahedralize1)
tTKPersistenceCurve1.ScalarField = 'myVorticity'
tTKPersistenceCurve1.InputOffsetField = ''

# ----------------------------------------------------------------
tTKScalarFieldNormalizer1.DebugLevel = int(debugLevel)
if tTKScalarFieldNormalizer1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldNormalizer1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldNormalizer1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldNormalizer1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldNormalizer1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldNormalizer1)))
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
tTKScalarFieldCriticalPoints1.DebugLevel = int(debugLevel)
if tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1)))
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
tTKPersistenceCurve1.DebugLevel = int(debugLevel)
if tTKPersistenceCurve1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceCurve1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceCurve1_' + str(i) + '.vtk',
			OutputPort(tTKPersistenceCurve1, i))
else:
	SaveData(outputDirectory + 'tTKPersistenceCurve1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceCurve1)))
