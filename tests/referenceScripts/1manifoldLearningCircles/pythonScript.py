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
clustering0csv = CSVReader(FileName=['clustering0.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clustering0csv)
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.ZColumn = 'X'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tableToPoints1)
tTKSphereFromPoint2.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling1.ResamplingGrid = [256, 256, 3]
gaussianResampling1.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.0187499550000001, 0.0313220950000002, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = 'SplatterValues'
tTKPersistenceDiagram1.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold12 = Threshold(Input=tTKPersistenceDiagram1)
threshold12.Scalars = ['CELLS', 'PairIdentifier']
threshold12.ThresholdRange = [-1.0, -0.1]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ['CELLS', 'Persistence']
persistenceThreshold0.ThresholdRange = [10.0, 9999.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint11 = TTKSphereFromPoint(Input=persistenceThreshold0)
tTKSphereFromPoint11.Radius = 0.75

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=slice1,
    Constraints=persistenceThreshold0)
tTKTopologicalSimplification1.ScalarField = 'SplatterValues'
tTKTopologicalSimplification1.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification1.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification1.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex1.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator1 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex1_1,3),
    Target=tableToPoints1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKDataSetInterpolator1)
tTKSphereFromPoint1.Radius = 0.05

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.ThresholdRange = [1.0, 1.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint3.Radius = 0.075

# create a new 'Extract Surface'
extractSurface7 = ExtractSurface(Input=threshold12)

# create a new 'Tube'
tube7 = Tube(Input=extractSurface7)
tube7.Scalars = ['POINTS', 'CriticalType']
tube7.Vectors = ['POINTS', 'Coordinates']
tube7.Radius = 0.5

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=persistenceThreshold0)

# create a new 'Tube'
tube6 = Tube(Input=extractSurface6)
tube6.Scalars = ['POINTS', 'CriticalType']
tube6.Vectors = ['POINTS', 'Coordinates']
tube6.Radius = 0.5

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold4.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=threshold4)
tTKGeometrySmoother2.IterationNumber = 10
tTKGeometrySmoother2.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Vectors = [None, '']
tube2.Radius = 0.02

# create a new 'Threshold'
threshold3 = Threshold(Input=threshold2)
threshold3.Scalars = ['CELLS', 'SeparatrixFunctionMinimum']
threshold3.ThresholdRange = [2.0, 999.0]

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=threshold3)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=cleantoGrid1)

# create a new 'Calculator'
calculator1 = Calculator(Input=connectivity1)
calculator1.ResultArrayName = 'AscendingManifold'
calculator1.Function = 'RegionId'

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=calculator1)
tTKGeometrySmoother1.IterationNumber = 500
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'AscendingManifold']
tube1.Vectors = [None, '']
tube1.Radius = 0.125

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKMorseSmaleComplex1_1

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.RGBPoints = [-1.0, 0.278431372549, 0.278431372549, 0.858823529412, -0.571, 0.0, 0.0, 0.360784313725, -0.145, 0.0, 1.0, 1.0, 0.287, 0.0, 0.501960784314, 0.0, 0.713, 1.0, 1.0, 0.0, 1.142, 1.0, 0.380392156863, 0.0, 1.571, 0.419607843137, 0.0, 0.0, 2.0, 0.878431372549, 0.301960784314, 0.301960784314]
ascendingManifoldLUT.ColorSpace = 'RGB'
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKTopologicalSimplification1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from slice1

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 19.416547144102, 0.917647, 0.941176, 0.788235, 38.8330942882042, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint3

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from threshold1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint11

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube6

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube7

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))


tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))


tTKSphereFromPoint11.DebugLevel = int(debugLevel)
if tTKSphereFromPoint11.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint11.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint11_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint11, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint11.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint11)))


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


tTKDataSetInterpolator1.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator1, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator1.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator1)))


tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))


tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))


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
