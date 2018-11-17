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

# Create a new 'Render View'

# init the 'GridAxes3DActor' selected for 'AxesGrid'

# Create a new 'Render View'

# init the 'GridAxes3DActor' selected for 'AxesGrid'

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
clustering4csv = CSVReader(FileName=['clustering4.csv'])

# create a new 'CSV Reader'
clustering3csv = CSVReader(FileName=['clustering3.csv'])

# create a new 'CSV Reader'
clustering2csv = CSVReader(FileName=['clustering2.csv'])

# create a new 'Table To Points'
tableToPoints3 = TableToPoints(Input=clustering2csv)
tableToPoints3.XColumn = 'X'
tableToPoints3.YColumn = 'Y'
tableToPoints3.ZColumn = 'X'
tableToPoints3.a2DPoints = 1
tableToPoints3.KeepAllDataArrays = 1

# create a new 'CSV Reader'
clustering0csv = CSVReader(FileName=['clustering0.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clustering0csv)
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.ZColumn = 'X'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'CSV Reader'
clustering1csv = CSVReader(FileName=['clustering1.csv'])

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=clustering1csv)
tableToPoints2.XColumn = 'X'
tableToPoints2.YColumn = 'Y'
tableToPoints2.ZColumn = 'X'
tableToPoints2.a2DPoints = 1
tableToPoints2.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=tableToPoints3)
tTKSphereFromPoint5.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tableToPoints2)
tTKSphereFromPoint3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tableToPoints1)
tTKSphereFromPoint2.Radius = 0.05

# create a new 'Table To Points'
tableToPoints5 = TableToPoints(Input=clustering4csv)
tableToPoints5.XColumn = 'X'
tableToPoints5.YColumn = 'Y'
tableToPoints5.ZColumn = 'X'
tableToPoints5.a2DPoints = 1
tableToPoints5.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint8 = TTKSphereFromPoint(Input=tableToPoints5)
tTKSphereFromPoint8.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling5 = GaussianResampling(Input=tableToPoints5)
gaussianResampling5.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling5.ResamplingGrid = [256, 256, 3]
gaussianResampling5.SplatAccumulationMode = 'Sum'

# create a new 'Table To Points'
tableToPoints4 = TableToPoints(Input=clustering3csv)
tableToPoints4.XColumn = 'X'
tableToPoints4.YColumn = 'Y'
tableToPoints4.ZColumn = 'X'
tableToPoints4.a2DPoints = 1
tableToPoints4.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint7 = TTKSphereFromPoint(Input=tableToPoints4)
tTKSphereFromPoint7.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling4 = GaussianResampling(Input=tableToPoints4)
gaussianResampling4.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling4.ResamplingGrid = [256, 256, 3]
gaussianResampling4.GaussianSplatRadius = 0.025
gaussianResampling4.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice4 = Slice(Input=gaussianResampling4)
slice4.SliceType = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [0.432938475, -0.313307725, 0.0]
slice4.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(Input=slice4)
tTKPersistenceDiagram4.ScalarField = 'SplatterValues'
tTKPersistenceDiagram4.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold7 = Threshold(Input=tTKPersistenceDiagram4)
threshold7.Scalars = ['CELLS', 'PairIdentifier']
threshold7.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold3 = Threshold(Input=threshold7)
persistenceThreshold3.Scalars = ['CELLS', 'Persistence']
persistenceThreshold3.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification4 = TTKTopologicalSimplification(Domain=slice4,
    Constraints=persistenceThreshold3)
tTKTopologicalSimplification4.ScalarField = 'SplatterValues'
tTKTopologicalSimplification4.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification4.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification4.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex4 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification4)
tTKMorseSmaleComplex4.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex4.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex4_1 = FindSource('TTKMorseSmaleComplex4')

# create a new 'Threshold'
threshold8 = Threshold(Input=OutputPort(tTKMorseSmaleComplex4,1))
threshold8.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother4 = TTKGeometrySmoother(Input=threshold8)
tTKGeometrySmoother4.IterationNumber = 10
tTKGeometrySmoother4.InputMaskField = 'CellDimension'

# find source
tTKMorseSmaleComplex4_2 = FindSource('TTKMorseSmaleComplex4')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator4 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex4,3),
    Target=tableToPoints4)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint9 = TTKSphereFromPoint(Input=tTKDataSetInterpolator4)
tTKSphereFromPoint9.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling3 = GaussianResampling(Input=tableToPoints3)
gaussianResampling3.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling3.ResamplingGrid = [256, 256, 3]
gaussianResampling3.GaussianSplatRadius = 0.05
gaussianResampling3.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice3 = Slice(Input=gaussianResampling3)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [-0.189980645, 0.28712807, 0.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=slice3)
tTKPersistenceDiagram3.ScalarField = 'SplatterValues'
tTKPersistenceDiagram3.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold5 = Threshold(Input=tTKPersistenceDiagram3)
threshold5.Scalars = ['CELLS', 'PairIdentifier']
threshold5.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold2 = Threshold(Input=threshold5)
persistenceThreshold2.Scalars = ['CELLS', 'Persistence']
persistenceThreshold2.ThresholdRange = [5.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification3 = TTKTopologicalSimplification(Domain=slice3,
    Constraints=persistenceThreshold2)
tTKTopologicalSimplification3.ScalarField = 'SplatterValues'
tTKTopologicalSimplification3.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification3.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification3.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex3 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification3)
tTKMorseSmaleComplex3.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex3.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex3_1 = FindSource('TTKMorseSmaleComplex3')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator3 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex3,3),
    Target=tableToPoints3)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint6 = TTKSphereFromPoint(Input=tTKDataSetInterpolator3)
tTKSphereFromPoint6.Radius = 0.05

# find source
tTKMorseSmaleComplex3_2 = FindSource('TTKMorseSmaleComplex3')

# create a new 'Threshold'
threshold6 = Threshold(Input=OutputPort(tTKMorseSmaleComplex3,1))
threshold6.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=threshold6)
tTKGeometrySmoother3.IterationNumber = 10
tTKGeometrySmoother3.InputMaskField = 'CellDimension'

# create a new 'Gaussian Resampling'
gaussianResampling2 = GaussianResampling(Input=tableToPoints2)
gaussianResampling2.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling2.ResamplingGrid = [256, 256, 3]
gaussianResampling2.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice2 = Slice(Input=gaussianResampling2)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.0283216049999999, -0.0118457750000003, 0.0]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=slice2)
tTKPersistenceDiagram2.ScalarField = 'SplatterValues'
tTKPersistenceDiagram2.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram2)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold3)
persistenceThreshold1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold1.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=slice2,
    Constraints=persistenceThreshold1)
tTKTopologicalSimplification2.ScalarField = 'SplatterValues'
tTKTopologicalSimplification2.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification2.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification2.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification2)
tTKMorseSmaleComplex2.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex2.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator2 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex2_1,3),
    Target=tableToPoints2)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKDataSetInterpolator2)
tTKSphereFromPoint4.Radius = 0.05

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2_2,1))
threshold4.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=threshold4)
tTKGeometrySmoother2.IterationNumber = 10
tTKGeometrySmoother2.InputMaskField = 'CellDimension'

# create a new 'Slice'
slice5 = Slice(Input=gaussianResampling5)
slice5.SliceType = 'Plane'
slice5.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice5.SliceType.Origin = [-0.309726305, -0.0956821999999999, 0.0]
slice5.SliceType.Normal = [0.0, 0.0, 1.0]

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
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ['CELLS', 'Persistence']
persistenceThreshold0.ThresholdRange = [10.0, 9999.0]

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

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,1))
threshold2.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 10
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator1 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex1_2,3),
    Target=tableToPoints1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKDataSetInterpolator1)
tTKSphereFromPoint1.Radius = 0.05

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKGeometrySmoother4)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'CellDimension']
tube4.Vectors = [None, '']
tube4.Radius = 0.04

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKGeometrySmoother3)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'CellDimension']
tube3.Vectors = [None, '']
tube3.Radius = 0.04

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Vectors = [None, '']
tube2.Radius = 0.04

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(Input=slice5)
tTKPersistenceDiagram5.ScalarField = 'SplatterValues'
tTKPersistenceDiagram5.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold9 = Threshold(Input=tTKPersistenceDiagram5)
threshold9.Scalars = ['CELLS', 'PairIdentifier']
threshold9.ThresholdRange = [-0.1, 9999.0]

# create a new 'Threshold'
threshold10 = Threshold(Input=threshold9)
threshold10.Scalars = ['CELLS', 'Persistence']
threshold10.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification5 = TTKTopologicalSimplification(Domain=slice5,
    Constraints=threshold10)
tTKTopologicalSimplification5.ScalarField = 'SplatterValues'
tTKTopologicalSimplification5.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification5.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification5.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex5 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification5)
tTKMorseSmaleComplex5.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex5.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex5_1 = FindSource('TTKMorseSmaleComplex5')

# create a new 'Threshold'
threshold11 = Threshold(Input=OutputPort(tTKMorseSmaleComplex5_1,1))
threshold11.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother5 = TTKGeometrySmoother(Input=threshold11)
tTKGeometrySmoother5.IterationNumber = 10
tTKGeometrySmoother5.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=tTKGeometrySmoother5)

# create a new 'Tube'
tube5 = Tube(Input=extractSurface5)
tube5.Scalars = ['POINTS', 'CellDimension']
tube5.Vectors = [None, '']
tube5.Radius = 0.04

# find source
tTKMorseSmaleComplex5_2 = FindSource('TTKMorseSmaleComplex5')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator5 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex5_2,3),
    Target=tableToPoints5)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint10 = TTKSphereFromPoint(Input=tTKDataSetInterpolator5)
tTKSphereFromPoint10.Radius = 0.05

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.04

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from slice1

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 9.85870357834292, 0.917647, 0.941176, 0.788235, 19.717407156686, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint8

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from slice5

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from slice2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint7

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from slice4

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint5

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from slice3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tube5

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKTopologicalSimplification5

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex5_2

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

# show data from tTKSphereFromPoint10

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex1_2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex2_1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint4

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube2

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex3_1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube3

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint6

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification4

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex4

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 19.717407156686, 1.0, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# find source
tTKMorseSmaleComplex4_3 = FindSource('TTKMorseSmaleComplex4')

# show data from tTKMorseSmaleComplex4_3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKMorseSmaleComplex4_2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube4

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint9

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

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))


tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))


tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))


tTKSphereFromPoint8.DebugLevel = int(debugLevel)
if tTKSphereFromPoint8.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint8.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint8_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint8, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint8.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint8)))


tTKSphereFromPoint7.DebugLevel = int(debugLevel)
if tTKSphereFromPoint7.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint7.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint7_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint7, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint7.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint7)))


tTKPersistenceDiagram4.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram4, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram4.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram4)))


tTKTopologicalSimplification4.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification4, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification4.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification4)))


tTKMorseSmaleComplex4.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex4, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex4.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex4)))


tTKGeometrySmoother4.DebugLevel = int(debugLevel)
if tTKGeometrySmoother4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother4, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother4.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother4)))


tTKDataSetInterpolator4.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator4, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator4.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator4)))


tTKSphereFromPoint9.DebugLevel = int(debugLevel)
if tTKSphereFromPoint9.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint9.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint9_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint9, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint9.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint9)))


tTKPersistenceDiagram3.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram3, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram3.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram3)))


tTKTopologicalSimplification3.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification3, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification3.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification3)))


tTKMorseSmaleComplex3.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex3, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex3.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex3)))


tTKDataSetInterpolator3.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator3, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator3.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator3)))


tTKSphereFromPoint6.DebugLevel = int(debugLevel)
if tTKSphereFromPoint6.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint6.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint6_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint6, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint6.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint6)))


tTKGeometrySmoother3.DebugLevel = int(debugLevel)
if tTKGeometrySmoother3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother3, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother3.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother3)))


tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))


tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))


tTKMorseSmaleComplex2.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex2, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex2.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex2)))


tTKDataSetInterpolator2.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator2, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator2.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator2)))


tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))


tTKGeometrySmoother2.DebugLevel = int(debugLevel)
if tTKGeometrySmoother2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother2, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother2.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother2)))


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


tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))


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


tTKPersistenceDiagram5.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram5, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram5.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram5)))


tTKTopologicalSimplification5.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification5, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification5.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification5)))


tTKMorseSmaleComplex5.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex5, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex5.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex5)))


tTKGeometrySmoother5.DebugLevel = int(debugLevel)
if tTKGeometrySmoother5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother5, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother5.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother5)))


tTKDataSetInterpolator5.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator5, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator5.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator5)))


tTKSphereFromPoint10.DebugLevel = int(debugLevel)
if tTKSphereFromPoint10.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint10.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint10_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint10, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint10.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint10)))
