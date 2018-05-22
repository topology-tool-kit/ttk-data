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
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample2.vti'])
builtInExamplevti.PointArrayStatus = ['Rho', 'log(Rho)', 'log(s)']

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=builtInExamplevti)
computeDerivatives1.Scalars = ['POINTS', 'log(Rho)']
computeDerivatives1.Vectors = [None, '']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=builtInExamplevti)
tTKMorseSmaleComplex1.ScalarField = 'log(Rho)'
tTKMorseSmaleComplex1.InputOffsetField = ''
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.Descending2Separatrices = 1

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,2))
threshold5.Scalars = ['CELLS', 'CriticalPointIndex']
threshold5.ThresholdRange = [2.0, 2.0]

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,2))
threshold4.Scalars = ['CELLS', 'CriticalPointIndex']
threshold4.ThresholdRange = [1.0, 1.0]

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(Input=threshold4)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=cleantoGrid2)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tetrahedralize1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint2.Radius = 3.0

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)
threshold3.Scalars = ['POINTS', 'CellDimension']
threshold3.ThresholdRange = [3.0, 3.0]

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold1.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'Threshold'
threshold2 = Threshold(Input=threshold1)
threshold2.Scalars = ['CELLS', 'CriticalPointIndex']
threshold2.ThresholdRange = [2.0, 2.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint1.Radius = 1.5

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 50

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKGeometrySmoother1)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 1.25

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=extractSurface2)
tTKGeometrySmoother2.IterationNumber = 20

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=computeDerivatives1,
    SeedType='Point Source')
streamTracer1.Vectors = ['CELLS', 'ScalarGradient']
streamTracer1.IntegrationDirection = 'FORWARD'
streamTracer1.MaximumStreamlineLength = 133.0

# init the 'Point Source' selected for 'SeedType'
streamTracer1.SeedType.Center = [57.0177693769277, 35.7637631216166, 73.6417192169949]
streamTracer1.SeedType.Radius = 0.5

# create a new 'Tube'
tube4 = Tube(Input=streamTracer1)
tube4.Scalars = ['POINTS', 'log(s)']
tube4.Vectors = ['POINTS', 'Normals']

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=computeDerivatives1,
    SeedType='Point Source')
streamTracer2.Vectors = ['CELLS', 'ScalarGradient']
streamTracer2.IntegrationDirection = 'FORWARD'
streamTracer2.MaximumStreamlineLength = 133.0

# init the 'Point Source' selected for 'SeedType'
streamTracer2.SeedType.Center = [56.9955364629553, 35.7177590290303, 76.44491140625]
streamTracer2.SeedType.Radius = 0.5

# create a new 'Tube'
tube3 = Tube(Input=streamTracer2)
tube3.Scalars = ['POINTS', 'IntegrationTime']
tube3.Vectors = ['POINTS', 'Normals']

# create a new 'Threshold'
threshold8 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold8.Scalars = ['CELLS', 'CriticalPointIndex']
threshold8.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold9 = Threshold(Input=threshold8)
threshold9.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'Threshold'
threshold10 = Threshold(Input=threshold9)
threshold10.Scalars = ['CELLS', 'SeparatrixId']
threshold10.ThresholdRange = [77.0, 78.0]

# create a new 'Threshold'
threshold11 = Threshold(Input=threshold9)
threshold11.Scalars = ['CELLS', 'SeparatrixId']
threshold11.ThresholdRange = [78.0, 80.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[threshold10, threshold11])

# create a new 'Clean to Grid'
cleantoGrid4 = CleantoGrid(Input=appendDatasets1)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother4 = TTKGeometrySmoother(Input=cleantoGrid4)
tTKGeometrySmoother4.IterationNumber = 10

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKGeometrySmoother4)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Vectors = [None, '']
tube2.Radius = 0.75

# create a new 'Point Source'
pointSource1 = PointSource()
pointSource1.Center = [57.0177693769277, 35.7177590290303, 74.44491140625]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=pointSource1)
tTKSphereFromPoint3.Radius = 3.0

# create a new 'Threshold'
threshold6 = Threshold(Input=threshold5)
threshold6.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold6.ThresholdRange = [4.0, 4.0]

# create a new 'Threshold'
threshold7 = Threshold(Input=threshold6)
threshold7.Scalars = ['CELLS', 'SeparatrixId']
threshold7.ThresholdRange = [22.0, 22.0]

# create a new 'Clean to Grid'
cleantoGrid3 = CleantoGrid(Input=threshold7)

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=cleantoGrid3)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=tetrahedralize2)
tTKGeometrySmoother3.IterationNumber = 20

# create a new 'Contour'
contour1 = Contour(Input=builtInExamplevti)
contour1.ContourBy = ['POINTS', 'log(Rho)']
contour1.ComputeScalars = 1
contour1.Isosurfaces = [1.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------tTKMorseSmaleComplex1.DebugLevel = int(debugLevel)
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
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))
tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
tTKGeometrySmoother2.DebugLevel = int(debugLevel)
if tTKGeometrySmoother2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother2, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother2.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother2)))
tTKGeometrySmoother4.DebugLevel = int(debugLevel)
if tTKGeometrySmoother4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother4, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother4.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother4)))
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKGeometrySmoother3.DebugLevel = int(debugLevel)
if tTKGeometrySmoother3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother3, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother3.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother3)))
