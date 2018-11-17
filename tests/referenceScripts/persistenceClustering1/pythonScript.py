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
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView10 = CreateView('RenderView')
renderView10.ViewSize = [821, 589]
renderView10.InteractionMode = '2D'
renderView10.AxesGrid = 'GridAxes3DActor'
renderView10.OrientationAxesVisibility = 0
renderView10.CenterOfRotation = [-0.0187499550000001, 0.031322095, 0.0]
renderView10.StereoType = 0
renderView10.CameraPosition = [-0.00532513936137657, 0.00761441820211089, 10.6574753000108]
renderView10.CameraFocalPoint = [-0.00532513936137657, 0.00761441820211089, 0.0]
renderView10.CameraParallelScale = 2.0616591672826
renderView10.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView10.AxesGrid.Visibility = 1
renderView10.AxesGrid.XTitle = 'Birth'
renderView10.AxesGrid.YTitle = 'Death'
renderView10.AxesGrid.ZTitle = ''
renderView10.AxesGrid.XTitleFontFile = ''
renderView10.AxesGrid.YTitleFontFile = ''
renderView10.AxesGrid.ZTitleFontFile = ''
renderView10.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView10.AxesGrid.ShowEdges = 0
renderView10.AxesGrid.ShowTicks = 0
renderView10.AxesGrid.AxesToLabel = 0
renderView10.AxesGrid.XLabelFontFile = ''
renderView10.AxesGrid.YLabelFontFile = ''
renderView10.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView12 = CreateView('RenderView')
renderView12.ViewSize = [822, 589]
renderView12.InteractionMode = '2D'
renderView12.AxesGrid = 'GridAxes3DActor'
renderView12.OrientationAxesVisibility = 0
renderView12.CenterOfRotation = [-0.0187499550000001, 0.031322095, 0.0]
renderView12.StereoType = 0
renderView12.CameraPosition = [-0.00532513936137657, 0.00761441820211089, 10.6574753000108]
renderView12.CameraFocalPoint = [-0.00532513936137657, 0.00761441820211089, 0.0]
renderView12.CameraParallelScale = 2.0616591672826
renderView12.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView12.AxesGrid.Visibility = 1
renderView12.AxesGrid.XTitle = 'Birth'
renderView12.AxesGrid.YTitle = 'Death'
renderView12.AxesGrid.ZTitle = ''
renderView12.AxesGrid.XTitleFontFile = ''
renderView12.AxesGrid.YTitleFontFile = ''
renderView12.AxesGrid.ZTitleFontFile = ''
renderView12.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView12.AxesGrid.ShowEdges = 0
renderView12.AxesGrid.ShowTicks = 0
renderView12.AxesGrid.AxesToLabel = 0
renderView12.AxesGrid.XLabelFontFile = ''
renderView12.AxesGrid.YLabelFontFile = ''
renderView12.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView13 = CreateView('RenderView')
renderView13.ViewSize = [821, 589]
renderView13.InteractionMode = '2D'
renderView13.AxesGrid = 'GridAxes3DActor'
renderView13.OrientationAxesVisibility = 0
renderView13.CenterOfRotation = [-0.0187499550000001, 0.031322095, 0.0]
renderView13.StereoType = 0
renderView13.CameraPosition = [-0.00532513936137657, 0.00761441820211089, 10.6574753000108]
renderView13.CameraFocalPoint = [-0.00532513936137657, 0.00761441820211089, 0.0]
renderView13.CameraParallelScale = 2.0616591672826
renderView13.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView13.AxesGrid.Visibility = 1
renderView13.AxesGrid.XTitle = 'Birth'
renderView13.AxesGrid.YTitle = 'Death'
renderView13.AxesGrid.ZTitle = ''
renderView13.AxesGrid.XTitleFontFile = ''
renderView13.AxesGrid.YTitleFontFile = ''
renderView13.AxesGrid.ZTitleFontFile = ''
renderView13.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView13.AxesGrid.ShowEdges = 0
renderView13.AxesGrid.ShowTicks = 0
renderView13.AxesGrid.AxesToLabel = 0
renderView13.AxesGrid.XLabelFontFile = ''
renderView13.AxesGrid.YLabelFontFile = ''
renderView13.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView14 = CreateView('RenderView')
renderView14.ViewSize = [822, 589]
renderView14.InteractionMode = '2D'
renderView14.AxesGrid = 'GridAxes3DActor'
renderView14.OrientationAxesVisibility = 0
renderView14.CenterOfRotation = [18.0001735687256, 19.4165477752686, 0.0]
renderView14.StereoType = 0
renderView14.CameraPosition = [21.9000086559306, 23.1492699949158, 102.297597669232]
renderView14.CameraFocalPoint = [21.9000086559306, 23.1492699949158, 0.0]
renderView14.CameraParallelScale = 29.3606249607563
renderView14.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView14.AxesGrid.Visibility = 1
renderView14.AxesGrid.XTitle = 'Birth'
renderView14.AxesGrid.YTitle = 'Death'
renderView14.AxesGrid.ZTitle = ''
renderView14.AxesGrid.XTitleFontFile = ''
renderView14.AxesGrid.YTitleFontFile = ''
renderView14.AxesGrid.ZTitleFontFile = ''
renderView14.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView14.AxesGrid.ShowGrid = 1
renderView14.AxesGrid.AxesToLabel = 3
renderView14.AxesGrid.XLabelFontFile = ''
renderView14.AxesGrid.YLabelFontFile = ''
renderView14.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView10)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
clusteringcsv = CSVReader(FileName=['clustering1.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clusteringcsv)
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.ZColumn = 'X'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

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

# create a new 'Extract Surface'
extractSurface7 = ExtractSurface(Input=threshold12)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tableToPoints1)
tTKSphereFromPoint2.Radius = 0.05

# create a new 'Tube'
tube7 = Tube(Input=extractSurface7)
tube7.Scalars = ['POINTS', 'CriticalType']
tube7.Vectors = ['POINTS', 'Coordinates']
tube7.Radius = 0.75

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

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint3.Radius = 0.075

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator1 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex1_2,3),
    Target=tableToPoints1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKDataSetInterpolator1)
tTKSphereFromPoint1.Radius = 0.05

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=persistenceThreshold0)

# create a new 'Tube'
tube6 = Tube(Input=extractSurface6)
tube6.Scalars = ['POINTS', 'CriticalType']
tube6.Vectors = ['POINTS', 'Coordinates']
tube6.Radius = 0.75

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint11 = TTKSphereFromPoint(Input=persistenceThreshold0)
tTKSphereFromPoint11.Radius = 1.0

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.025

# ----------------------------------------------------------------
# setup the visualization in view 'renderView10'
# ----------------------------------------------------------------

# show data from tTKMorseSmaleComplex1_2
tTKMorseSmaleComplex1Display = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView10)

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.RGBPoints = [-1.0, 0.278431372549, 0.278431372549, 0.858823529412, -0.571, 0.0, 0.0, 0.360784313725, -0.145, 0.0, 1.0, 1.0, 0.287, 0.0, 0.501960784314, 0.0, 0.713, 1.0, 1.0, 0.0, 1.142, 1.0, 0.380392156863, 0.0, 1.571, 0.419607843137, 0.0, 0.0, 2.0, 0.878431372549, 0.301960784314, 0.301960784314]
ascendingManifoldLUT.ColorSpace = 'RGB'
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex1Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex1Display.Opacity = 0.5
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex1Display.ScaleFactor = 0.47112181186676
tTKMorseSmaleComplex1Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.023556090593338
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex1Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView10)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 0.482380127906799
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 0.02411900639534
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display.DataAxesGrid.XTitleFontFile = ''
tube1Display.DataAxesGrid.YTitleFontFile = ''
tube1Display.DataAxesGrid.ZTitleFontFile = ''
tube1Display.DataAxesGrid.XLabelFontFile = ''
tube1Display.DataAxesGrid.YLabelFontFile = ''
tube1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView10)

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint1Display.ScaleFactor = 0.402567327022552
tTKSphereFromPoint1Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint1Display.GaussianRadius = 0.0201283663511276
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint1Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKTopologicalSimplification1
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView10)

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Surface'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification1Display.Specular = 1.0
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification1Display.ScaleFactor = 0.47112181186676
tTKTopologicalSimplification1Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification1Display.GaussianRadius = 0.023556090593338
tTKTopologicalSimplification1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification1Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification1Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView12'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint2
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView12)

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = [None, '']
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint2Display.ScaleFactor = 0.402567327022552
tTKSphereFromPoint2Display.SelectScaleArray = 'None'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint2Display.GaussianRadius = 0.0201283663511276
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint2Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint2Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint2Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint2Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint2Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView13'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView13)

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 24.7797819776106, 0.917647, 0.941176, 0.788235, 49.5595639552215, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice1Display.LookupTable = splatterValuesLUT
slice1Display.Specular = 1.0
slice1Display.OSPRayScaleArray = 'SplatterValues'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.47112181186676
slice1Display.SelectScaleArray = 'SplatterValues'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'SplatterValues'
slice1Display.GaussianRadius = 0.023556090593338
slice1Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'SplatterValues']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.5595639552215, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.5595639552215, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView13)

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.LookupTable = cellDimensionLUT
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint3Display.ScaleFactor = 0.570780253410339
tTKSphereFromPoint3Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint3Display.GaussianRadius = 0.028539012670517
tTKSphereFromPoint3Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint3Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint3Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint3Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView14'
# ----------------------------------------------------------------

# show data from threshold1
threshold1Display = Show(threshold1, renderView14)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.Opacity = 0.5
threshold1Display.Specular = 1.0
threshold1Display.OSPRayScaleArray = 'Coordinates'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'Coordinates'
threshold1Display.ScaleFactor = 3.88330955505371
threshold1Display.SelectScaleArray = 'Coordinates'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'Coordinates'
threshold1Display.GaussianRadius = 0.194165477752686
threshold1Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'Coordinates']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityUnitDistance = 9.0548583885181

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [-2.34916925430298, 0.0, 0.5, 0.0, 2.31166934967041, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [-2.34916925430298, 0.0, 0.5, 0.0, 2.31166934967041, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold1Display.DataAxesGrid.XTitleFontFile = ''
threshold1Display.DataAxesGrid.YTitleFontFile = ''
threshold1Display.DataAxesGrid.ZTitleFontFile = ''
threshold1Display.DataAxesGrid.XLabelFontFile = ''
threshold1Display.DataAxesGrid.YLabelFontFile = ''
threshold1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold1Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold1Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold1Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint11
tTKSphereFromPoint11Display = Show(tTKSphereFromPoint11, renderView14)

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint11Display.Representation = 'Surface'
tTKSphereFromPoint11Display.ColorArrayName = ['POINTS', 'CriticalType']
tTKSphereFromPoint11Display.LookupTable = criticalTypeLUT
tTKSphereFromPoint11Display.Specular = 1.0
tTKSphereFromPoint11Display.OSPRayScaleArray = 'CriticalType'
tTKSphereFromPoint11Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint11Display.SelectOrientationVectors = 'CriticalType'
tTKSphereFromPoint11Display.ScaleFactor = 3.89327523522079
tTKSphereFromPoint11Display.SelectScaleArray = 'CriticalType'
tTKSphereFromPoint11Display.GlyphType = 'Arrow'
tTKSphereFromPoint11Display.GlyphTableIndexArray = 'CriticalType'
tTKSphereFromPoint11Display.GaussianRadius = 0.194663761761039
tTKSphereFromPoint11Display.SetScaleArray = ['POINTS', 'CriticalType']
tTKSphereFromPoint11Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint11Display.OpacityArray = ['POINTS', 'CriticalType']
tTKSphereFromPoint11Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint11Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint11Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint11Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint11Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint11Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint11Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint11Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint11Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint11Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint11Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint11Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint11Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint11Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint11Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint11Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint11Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube6
tube6Display = Show(tube6, renderView14)

# trace defaults for the display properties.
tube6Display.Representation = 'Surface'
tube6Display.ColorArrayName = [None, '']
tube6Display.Specular = 1.0
tube6Display.OSPRayScaleArray = 'Coordinates'
tube6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube6Display.SelectOrientationVectors = 'Coordinates'
tube6Display.ScaleFactor = 3.88330955505371
tube6Display.SelectScaleArray = 'Coordinates'
tube6Display.GlyphType = 'Arrow'
tube6Display.GlyphTableIndexArray = 'Coordinates'
tube6Display.GaussianRadius = 0.194165477752686
tube6Display.SetScaleArray = ['POINTS', 'Coordinates']
tube6Display.ScaleTransferFunction = 'PiecewiseFunction'
tube6Display.OpacityArray = ['POINTS', 'Coordinates']
tube6Display.OpacityTransferFunction = 'PiecewiseFunction'
tube6Display.DataAxesGrid = 'GridAxesRepresentation'
tube6Display.SelectionCellLabelFontFile = ''
tube6Display.SelectionPointLabelFontFile = ''
tube6Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube6Display.ScaleTransferFunction.Points = [-2.24305248260498, 0.0, 0.5, 0.0, 0.675181150436401, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube6Display.OpacityTransferFunction.Points = [-2.24305248260498, 0.0, 0.5, 0.0, 0.675181150436401, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube6Display.DataAxesGrid.XTitleFontFile = ''
tube6Display.DataAxesGrid.YTitleFontFile = ''
tube6Display.DataAxesGrid.ZTitleFontFile = ''
tube6Display.DataAxesGrid.XLabelFontFile = ''
tube6Display.DataAxesGrid.YLabelFontFile = ''
tube6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube6Display.PolarAxes.PolarAxisTitleFontFile = ''
tube6Display.PolarAxes.PolarAxisLabelFontFile = ''
tube6Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube7
tube7Display = Show(tube7, renderView14)

# trace defaults for the display properties.
tube7Display.Representation = 'Surface'
tube7Display.ColorArrayName = [None, '']
tube7Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube7Display.Specular = 1.0
tube7Display.OSPRayScaleArray = 'Coordinates'
tube7Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube7Display.SelectOrientationVectors = 'Coordinates'
tube7Display.ScaleFactor = 3.63065316826105
tube7Display.SelectScaleArray = 'Coordinates'
tube7Display.GlyphType = 'Arrow'
tube7Display.GlyphTableIndexArray = 'Coordinates'
tube7Display.GaussianRadius = 0.181532658413053
tube7Display.SetScaleArray = ['POINTS', 'Coordinates']
tube7Display.ScaleTransferFunction = 'PiecewiseFunction'
tube7Display.OpacityArray = ['POINTS', 'Coordinates']
tube7Display.OpacityTransferFunction = 'PiecewiseFunction'
tube7Display.DataAxesGrid = 'GridAxesRepresentation'
tube7Display.SelectionCellLabelFontFile = ''
tube7Display.SelectionPointLabelFontFile = ''
tube7Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube7Display.ScaleTransferFunction.Points = [-2.24305248260498, 0.0, 0.5, 0.0, -0.297563403844833, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube7Display.OpacityTransferFunction.Points = [-2.24305248260498, 0.0, 0.5, 0.0, -0.297563403844833, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube7Display.DataAxesGrid.XTitleFontFile = ''
tube7Display.DataAxesGrid.YTitleFontFile = ''
tube7Display.DataAxesGrid.ZTitleFontFile = ''
tube7Display.DataAxesGrid.XLabelFontFile = ''
tube7Display.DataAxesGrid.YLabelFontFile = ''
tube7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube7Display.PolarAxes.PolarAxisTitleFontFile = ''
tube7Display.PolarAxes.PolarAxisLabelFontFile = ''
tube7Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 49.5595639552215, 1.0, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

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


tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))


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


tTKSphereFromPoint11.DebugLevel = int(debugLevel)
if tTKSphereFromPoint11.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint11.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint11_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint11, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint11.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint11)))
