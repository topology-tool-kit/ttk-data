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
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.5.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [521, 611]
lineChartView1.ChartTitleFontFile = ''
lineChartView1.LeftAxisTitle = 'Number of Pairs'
lineChartView1.LeftAxisGridColor = [0.784313725490196, 0.784313725490196, 0.784313725490196]
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisLogScale = 1
lineChartView1.LeftAxisUseCustomRange = 1
lineChartView1.LeftAxisRangeMinimum = 1.06038345801786
lineChartView1.LeftAxisRangeMaximum = 2586.16845314171
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.BottomAxisTitle = 'Persistence'
lineChartView1.BottomAxisGridColor = [0.784313725490196, 0.784313725490196, 0.784313725490196]
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisLogScale = 1
lineChartView1.BottomAxisUseCustomRange = 1
lineChartView1.BottomAxisRangeMinimum = 7.53351568057874e-05
lineChartView1.BottomAxisRangeMaximum = 9.50818827819817
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisLabelFontFile = ''

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1111, 1252]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, 0.0301545187830925]
renderView1.StereoType = 0
renderView1.CameraPosition = [-0.328287412992487, -1.27371248629734, 2.28960340532275]
renderView1.CameraFocalPoint = [0.0218086848780257, -0.00833918706993919, -0.223827778386087]
renderView1.CameraViewUp = [0.221222674519957, 0.858339466889751, 0.462940479821818]
renderView1.CameraParallelScale = 0.733927630065455
renderView1.Background = [0.188235294117647, 0.184313725490196, 0.184313725490196]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [521, 610]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.501142740249634, 0.654267549514771, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [-0.0776060748738056, 0.43906490533155, 10000.0]
renderView2.CameraFocalPoint = [-0.0776060748738056, 0.43906490533155, 0.0]
renderView2.CameraParallelScale = 5.90831525572308
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitle = 'Birth'
renderView2.AxesGrid.YTitle = 'Death'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

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

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# find source
tTKPersistenceCurve1_1 = FindSource('TTKPersistenceCurve1')

# show data from tTKPersistenceCurve1_1
tTKPersistenceCurve1Display = Show(OutputPort(tTKPersistenceCurve1, 3), lineChartView1)

# trace defaults for the display properties.
tTKPersistenceCurve1Display.CompositeDataSetIndex = [0]
tTKPersistenceCurve1Display.AttributeType = 'Row Data'
tTKPersistenceCurve1Display.UseIndexForXAxis = 0
tTKPersistenceCurve1Display.XArrayName = 'Persistence (all pairs)'
tTKPersistenceCurve1Display.SeriesVisibility = ['Number Of Pairs', 'Number Of Pairs (all pairs)']
tTKPersistenceCurve1Display.SeriesLabel = ['Persistence', 'Persistence', 'Number Of Pairs', 'Number Of Pairs', 'Number Of Pairs (all pairs)', 'Number Of Pairs (all pairs)', 'Persistence (all pairs)', 'Persistence (all pairs)']
tTKPersistenceCurve1Display.SeriesColor = ['Persistence', '0', '0', '0', 'Number Of Pairs', '0', '0.129412', '0.584314', 'Number Of Pairs (all pairs)', '0', '0.129412', '0.584314', 'Persistence (all pairs)', '0.889998', '0.100008', '0.110002']
tTKPersistenceCurve1Display.SeriesPlotCorner = ['Number Of Pairs', '0', 'Number Of Pairs (all pairs)', '0', 'Persistence', '0', 'Persistence (all pairs)', '0']
tTKPersistenceCurve1Display.SeriesLabelPrefix = ''
tTKPersistenceCurve1Display.SeriesLineStyle = ['Number Of Pairs', '1', 'Number Of Pairs (all pairs)', '1', 'Persistence', '1', 'Persistence (all pairs)', '1']
tTKPersistenceCurve1Display.SeriesLineThickness = ['Number Of Pairs', '4', 'Number Of Pairs (all pairs)', '5', 'Persistence', '2', 'Persistence (all pairs)', '2']
tTKPersistenceCurve1Display.SeriesMarkerStyle = ['Number Of Pairs', '0', 'Number Of Pairs (all pairs)', '0', 'Persistence', '0', 'Persistence (all pairs)', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint2
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView1)

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint2Display.LookupTable = cellDimensionLUT
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint2Display.ScaleFactor = 0.199658453464508
tTKSphereFromPoint2Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GaussianRadius = 0.099829226732254
tTKSphereFromPoint2Display.CustomShader = ''
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint2Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint2Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from tube3
tube3Display = Show(tube3, renderView1)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'CellDimension'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'CellDimension'
tube3Display.ScaleFactor = 0.101999998092651
tube3Display.SelectScaleArray = 'CellDimension'
tube3Display.GlyphType = 'Arrow'
tube3Display.GaussianRadius = 0.0509999990463257
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', 'CellDimension']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'CellDimension']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.SelectionCellLabelFontFile = ''
tube3Display.SelectionPointLabelFontFile = ''
tube3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube3Display.DataAxesGrid.XTitleFontFile = ''
tube3Display.DataAxesGrid.YTitleFontFile = ''
tube3Display.DataAxesGrid.ZTitleFontFile = ''
tube3Display.DataAxesGrid.XLabelFontFile = ''
tube3Display.DataAxesGrid.YLabelFontFile = ''
tube3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube3Display.PolarAxes.PolarAxisTitleFontFile = ''
tube3Display.PolarAxes.PolarAxisLabelFontFile = ''
tube3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from generateSurfaceNormals2
generateSurfaceNormals2Display = Show(generateSurfaceNormals2, renderView1)

# get color transfer function/color map for 'Blend'
blendLUT = GetColorTransferFunction('Blend')
blendLUT.RGBPoints = [-3.35309077487759, 0.0, 0.129412, 0.584314, 0.813536308583949, 0.917647, 0.941176, 0.788235, 4.98016339204548, 0.0, 0.431373, 0.0]
blendLUT.ColorSpace = 'RGB'
blendLUT.AboveRangeColor = [1.0, 1.0, 1.0]
blendLUT.NanColor = [0.0, 0.0, 0.0]
blendLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals2Display.Representation = 'Surface'
generateSurfaceNormals2Display.ColorArrayName = ['POINTS', 'Blend']
generateSurfaceNormals2Display.LookupTable = blendLUT
generateSurfaceNormals2Display.Specular = 1.0
generateSurfaceNormals2Display.OSPRayScaleArray = 'Blend'
generateSurfaceNormals2Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.SelectOrientationVectors = 'Blend'
generateSurfaceNormals2Display.ScaleFactor = 0.1
generateSurfaceNormals2Display.SelectScaleArray = 'Blend'
generateSurfaceNormals2Display.GlyphType = 'Arrow'
generateSurfaceNormals2Display.GaussianRadius = 0.05
generateSurfaceNormals2Display.CustomShader = ''
generateSurfaceNormals2Display.SetScaleArray = ['POINTS', 'Blend']
generateSurfaceNormals2Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.OpacityArray = ['POINTS', 'Blend']
generateSurfaceNormals2Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals2Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals2Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals2Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals2Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals2Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals2Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, renderView2)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube1Display.Specular = 1.0
tube1Display.SpecularPower = 50.0
tube1Display.OSPRayScaleArray = 'NodeType'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'NodeType'
tube1Display.ScaleFactor = 0.804595446586609
tube1Display.SelectScaleArray = 'NodeType'
tube1Display.GlyphType = 'Arrow'
tube1Display.GaussianRadius = 0.402297723293304
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'NodeType']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'NodeType']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView2)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')
nodeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
nodeTypeLUT.ColorSpace = 'RGB'
nodeTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
nodeTypeLUT.NanColor = [0.0, 0.0, 0.0]
nodeTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint1Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.SpecularPower = 50.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint1Display.ScaleFactor = 0.899356770515442
tTKSphereFromPoint1Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GaussianRadius = 0.449678385257721
tTKSphereFromPoint1Display.CustomShader = ''
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'NodeType']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'NodeType']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from tube2
tube2Display = Show(tube2, renderView2)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Specular = 1.0
tube2Display.SpecularPower = 50.0
tube2Display.OSPRayScaleArray = 'NodeType'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'NodeType'
tube2Display.ScaleFactor = 0.799698305130005
tube2Display.SelectScaleArray = 'NodeType'
tube2Display.GlyphType = 'Arrow'
tube2Display.GaussianRadius = 0.399849152565002
tube2Display.CustomShader = ''
tube2Display.SetScaleArray = ['POINTS', 'NodeType']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'NodeType']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.SelectionCellLabelFontFile = ''
tube2Display.SelectionPointLabelFontFile = ''
tube2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display.DataAxesGrid.XTitleFontFile = ''
tube2Display.DataAxesGrid.YTitleFontFile = ''
tube2Display.DataAxesGrid.ZTitleFontFile = ''
tube2Display.DataAxesGrid.XLabelFontFile = ''
tube2Display.DataAxesGrid.YLabelFontFile = ''
tube2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Blend'
blendPWF = GetOpacityTransferFunction('Blend')
blendPWF.Points = [-3.35309077487759, 0.0, 0.5, 0.0, 4.98016339204548, 1.0, 0.5, 0.0]
blendPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
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
