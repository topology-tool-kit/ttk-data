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

# create a new 'PNG Series Reader'
tributepng = PNGSeriesReader(FileNames=['tribute.png'])

# create a new 'Calculator'
calculator1 = Calculator(Input=tributepng)
calculator1.ResultArrayName = 'originalData'
calculator1.Function = 'sqrt(PNGImage_X*PNGImage_X+PNGImage_Y*PNGImage_Y)'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=calculator1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'originalData'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram1)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-1.0, -0.1]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 3560.0]

# create a new 'Threshold'
minimumPairs = Threshold(Input=threshold1)
minimumPairs.Scalars = ['CELLS', 'PairType']
minimumPairs.ThresholdRange = [-1.0, 0.0]

# create a new 'Threshold'
maximumPairs = Threshold(Input=threshold1)
maximumPairs.Scalars = ['CELLS', 'PairType']
maximumPairs.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator2 = Calculator(Input=maximumPairs)
calculator2.ResultArrayName = 'Birth'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
birthThreshold = Threshold(Input=calculator2)
birthThreshold.Scalars = ['POINTS', 'Birth']
birthThreshold.ThresholdRange = [257.390747070312, 297.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[minimumPairs, birthThreshold])

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=appendDatasets1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [8.5, 102.106426713382]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint2.Radius = 1.0

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'originalData'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tTKTopologicalSimplification1)
warpByScalar1.Scalars = ['POINTS', 'originalData']
warpByScalar1.ScaleFactor = 0.25

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=warpByScalar1)

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tetrahedralize2)
tTKMorseSmaleComplex2.ScalarField = 'originalData'
tTKMorseSmaleComplex2.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex2)
tTKSphereFromPoint4.Radius = 1.0

# create a new 'Calculator'
calculator5 = Calculator(Input=tTKMorseSmaleComplex2)
calculator5.CoordinateResults = 1
calculator5.ResultArrayName = 'newCoords'
calculator5.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=calculator5)
tTKSphereFromPoint3.Radius = 1.0

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(OutputPort(tTKMorseSmaleComplex2,3))
tTKIdentifierRandomizer2.ScalarField = 'AscendingManifold'

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKIdentifierRandomizer2)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface1)

# create a new 'Calculator'
calculator3 = Calculator(Input=tTKIdentifierRandomizer2)
calculator3.CoordinateResults = 1
calculator3.ResultArrayName = 'newCoords'
calculator3.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2,1))
threshold4.Scalars = ['CELLS', 'CriticalPointIndex']

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=threshold4)

# create a new 'Clip'
clip1 = Clip(Input=extractSurface4)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'CellDimension']
clip1.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [123.0, 66.0, 87.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Calculator'
calculator4 = Calculator(Input=clip1)
calculator4.CoordinateResults = 1
calculator4.ResultArrayName = 'newCoords'
calculator4.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=calculator4)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface5)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.75

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=clip1)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface6)
tube4.Scalars = ['POINTS', 'CellDimension']
tube4.Vectors = [None, '']
tube4.Radius = 0.75

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.5

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold3)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.75

# ----------------------------------------------------------------
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification1, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification1.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification1)))
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
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKIdentifierRandomizer2.DebugLevel = int(debugLevel)
if tTKIdentifierRandomizer2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIdentifierRandomizer2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIdentifierRandomizer2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIdentifierRandomizer2, i)))
else:
	SaveData(outputDirectory + 'tTKIdentifierRandomizer2.vtu',
		CleantoGrid(OutputPort(tTKIdentifierRandomizer2)))
