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
ctBonesvti = XMLImageDataReader(FileName=['ctBones.vti'])
ctBonesvti.PointArrayStatus = ['Scalars_']

# create a new 'Clip'
clip1 = Clip(Input=ctBonesvti)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Scalars_']
clip1.Value = 127.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [131.012324886831, 123.987675113169, 127.5]
clip1.ClipType.Normal = [-0.707106781186548, 0.707106781186548, 0.0]

# create a new 'Contour'
contour1 = Contour(Input=ctBonesvti)
contour1.ContourBy = ['POINTS', 'Scalars_']
contour1.Isosurfaces = [12.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=ctBonesvti)
tTKPersistenceDiagram1.ScalarField = 'Scalars_'

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram1)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold4)

# create a new 'Tube'
diagonal = Tube(Input=extractSurface2)
diagonal.Scalars = ['POINTS', 'NodeType']
diagonal.Vectors = ['POINTS', 'Coordinates']
diagonal.Radius = 1.5

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 345450.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [180.0, 255.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=ctBonesvti,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'Scalars_'

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(Input=tTKTopologicalSimplification1)
tTKMergeandContourTreeFTM1.ScalarField = 'Scalars_'
tTKMergeandContourTreeFTM1.TreeType = 'Split Tree'

# find source
tTKMergeandContourTreeFTM1_1 = FindSource('TTKMergeandContourTreeFTM1')

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMergeandContourTreeFTM1_1,2))
threshold3.Scalars = ['POINTS', 'RegionType']
threshold3.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold3)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=extractSurface1)
tTKGeometrySmoother1.IterationNumber = 3
tTKGeometrySmoother1.InputMaskField = 'RegionType'

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=tTKGeometrySmoother1)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 1.5

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 5.0

# ----------------------------------------------------------------
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))
tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification1, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification1.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification1)))
tTKMergeandContourTreeFTM1.DebugLevel = int(debugLevel)
if tTKMergeandContourTreeFTM1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMergeandContourTreeFTM1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMergeandContourTreeFTM1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMergeandContourTreeFTM1, i)))
else:
	SaveData(outputDirectory + 'tTKMergeandContourTreeFTM1.vtu',
		CleantoGrid(OutputPort(tTKMergeandContourTreeFTM1)))
tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))
