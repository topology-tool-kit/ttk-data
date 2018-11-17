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
# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'

# init the 'GridAxes3DActor' selected for 'AxesGrid'

# Create a new 'Render View'

# init the 'GridAxes3DActor' selected for 'AxesGrid'

# ----------------------------------------------------------------
# restore active view
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
pointCloudcsv = CSVReader(FileName=['pointCloud.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=pointCloudcsv)
tableToPoints1.XColumn = 'Points:0'
tableToPoints1.YColumn = 'Points:1'
tableToPoints1.ZColumn = 'Points:2'

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling1.ResamplingGrid = [64, 64, 128]

# create a new 'Outline'
outline1 = Outline(Input=gaussianResampling1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=gaussianResampling1)
tTKPersistenceDiagram1.ScalarField = 'SplatterValues'
tTKPersistenceDiagram1.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 9999.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.01, 0.999953171649318]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=gaussianResampling1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'SplatterValues'
tTKTopologicalSimplification1.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification1.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification1.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex1.InputOffsetField = 'SplatterValues'
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.01

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint1.Radius = 0.025

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=OutputPort(tTKMorseSmaleComplex1_1,2))

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=tetrahedralize1)
tTKGeometrySmoother2.IterationNumber = 20
tTKGeometrySmoother2.InputMaskField = 'NumberOfCriticalPointsOnBoundary'

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface2)

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold2.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 20
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.01

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from outline1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint1

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from generateSurfaceNormals1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from gaussianResampling1

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 0.153352356380398, 0.0941176470588235, 0.211764705882353, 0.603921568627451, 0.64855273377577, 0.917647, 0.941176, 0.788235, 0.99998518154625, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.546317791268681, 0.264423072338104, 0.5, 0.0, 0.99998518154625, 0.0769230797886848, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tableToPoints1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from outline1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
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


tTKMorseSmaleComplex1.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex1, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex1.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex1)))


tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))


tTKGeometrySmoother2.DebugLevel = int(debugLevel)
if tTKGeometrySmoother2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother2, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother2.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother2)))


tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
