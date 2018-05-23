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

# create a new 'XML Unstructured Grid Reader'
tectonicPuzzlevtu = XMLUnstructuredGridReader(FileName=['tectonicPuzzle.vtu'])
tectonicPuzzlevtu.PointArrayStatus = ['Morse field', 'T', 'Viscosity', 'Jacqueline', 'Strain rate', 'P', 'Velocity', 'Divergence', 'Vorticity']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tectonicPuzzlevtu)

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=extractSurface1)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=cleantoGrid1)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=tetrahedralize1)

# create a new 'Threshold'
threshold1 = Threshold(Input=connectivity1)
threshold1.Scalars = ['POINTS', 'RegionId']
threshold1.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'logViscosity'
calculator1.Function = 'log10(Viscosity)'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = 'logViscosity'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [-0.1, 1269.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold2)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.5, 99.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.ThetaResolution = 4
tTKSphereFromPoint1.PhiResolution = 4

# create a new 'Threshold'
pERSISTENT_MINIMA = Threshold(Input=tTKSphereFromPoint1)
pERSISTENT_MINIMA.Scalars = ['POINTS', 'NodeType']

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=calculator1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractSurface6)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'logViscosity'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'logViscosity'
tTKMorseSmaleComplex1.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint2.Radius = 0.1

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)
threshold3.Scalars = ['POINTS', 'CellDimension']
threshold3.ThresholdRange = [2.0, 2.0]

# create a new 'Threshold'
lARGE_MAXIMA_THRESHOLD = Threshold(Input=threshold3)
lARGE_MAXIMA_THRESHOLD.Scalars = ['POINTS', 'ManifoldSize']
lARGE_MAXIMA_THRESHOLD.ThresholdRange = [75.0, 9999.0]

# create a new 'Append Datasets'
pERSISTENT_MINIMA_AND_LARGE_MAXIMA = AppendDatasets(Input=[pERSISTENT_MINIMA, lARGE_MAXIMA_THRESHOLD])

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=tTKTopologicalSimplification1,
    Constraints=pERSISTENT_MINIMA_AND_LARGE_MAXIMA)
tTKTopologicalSimplification2.ScalarField = 'logViscosity'
tTKTopologicalSimplification2.UseInputOffsetField = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=tTKTopologicalSimplification2)
tTKPersistenceDiagram2.ScalarField = 'logViscosity'
tTKPersistenceDiagram2.UseInputOffsetField = 1

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram2)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [-0.1, 101.0]

# create a new 'Threshold'
threshold5 = Threshold(Input=threshold4)
threshold5.Scalars = ['CELLS', 'PairType']
threshold5.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator2 = Calculator(Input=threshold5)
calculator2.ResultArrayName = 'SaddleValue'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
sADDLE_VALUE_THRESHOLD = Threshold(Input=calculator2)
sADDLE_VALUE_THRESHOLD.Scalars = ['POINTS', 'SaddleValue']
sADDLE_VALUE_THRESHOLD.ThresholdRange = [-0.2, 1.75]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=sADDLE_VALUE_THRESHOLD)

# create a new 'Threshold'
lARGE_MAXIMA_LOW_SADDLE = Threshold(Input=tTKSphereFromPoint3)
lARGE_MAXIMA_LOW_SADDLE.Scalars = ['POINTS', 'NodeType']
lARGE_MAXIMA_LOW_SADDLE.ThresholdRange = [4.0, 4.0]

# create a new 'Append Datasets'
lARGE_MAXIMA_LOW_SADDLE_AND_PERSISTENT_MINIMA = AppendDatasets(Input=[pERSISTENT_MINIMA, lARGE_MAXIMA_LOW_SADDLE])

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification3 = TTKTopologicalSimplification(Domain=tTKTopologicalSimplification2,
    Constraints=lARGE_MAXIMA_LOW_SADDLE_AND_PERSISTENT_MINIMA)
tTKTopologicalSimplification3.ScalarField = 'logViscosity'
tTKTopologicalSimplification3.UseInputOffsetField = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=tTKTopologicalSimplification3)
tTKPersistenceDiagram3.ScalarField = 'logViscosity'
tTKPersistenceDiagram3.UseInputOffsetField = 1

# create a new 'Threshold'
threshold7 = Threshold(Input=tTKPersistenceDiagram3)
threshold7.Scalars = ['CELLS', 'PairIdentifier']
threshold7.ThresholdRange = [-0.1, 799.0]

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=threshold7)

# create a new 'Transform'
transform1 = Transform(Input=extractSurface4)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [3.5, 1.0, 1.0]

# create a new 'Tube'
tube3 = Tube(Input=transform1)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=transform1)
tTKSphereFromPoint5.Radius = 0.1

# create a new 'Threshold'
threshold8 = Threshold(Input=tTKPersistenceDiagram3)
threshold8.Scalars = ['CELLS', 'PairIdentifier']
threshold8.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold8)

# create a new 'Transform'
transform2 = Transform(Input=extractSurface3)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Scale = [3.5, 1.0, 1.0]

# create a new 'Tube'
tube2 = Tube(Input=transform2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.05

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification3)
tTKMorseSmaleComplex2.ScalarField = 'logViscosity'
tTKMorseSmaleComplex2.UseInputOffsetField = 1

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold6 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2_1,1))
threshold6.Scalars = ['CELLS', 'CriticalPointIndex']

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold6)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface2)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex2)
tTKSphereFromPoint4.Radius = 0.05

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(Input=OutputPort(tTKMorseSmaleComplex2_2,3))
tTKIdentifierRandomizer1.ScalarField = 'AscendingManifold'

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(Input=tTKIdentifierRandomizer1)

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=cleantoGrid2)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface5)

# ----------------------------------------------------------------
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
tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))
tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKTopologicalSimplification3.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification3, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification3.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification3)))
tTKPersistenceDiagram3.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram3, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram3.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram3)))
tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))
tTKMorseSmaleComplex2.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex2, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex2.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex2)))
tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))
tTKIdentifierRandomizer1.DebugLevel = int(debugLevel)
if tTKIdentifierRandomizer1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIdentifierRandomizer1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIdentifierRandomizer1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIdentifierRandomizer1, i)))
else:
	SaveData(outputDirectory + 'tTKIdentifierRandomizer1.vtu',
		CleantoGrid(OutputPort(tTKIdentifierRandomizer1)))
