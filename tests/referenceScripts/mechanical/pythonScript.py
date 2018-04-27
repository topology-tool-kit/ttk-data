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

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [773, 611]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.434635043144226, 0.0922348499298096, 1.5816547870636]
renderView1.StereoType = 0
renderView1.CameraPosition = [19.2718960140724, 12.9454572135077, -7.85020157567848]
renderView1.CameraFocalPoint = [0.236234316231568, -0.745247663489039, -0.488982566651684]
renderView1.CameraViewUp = [0.604893096134141, -0.514055959354024, 0.608153609626603]
renderView1.CameraParallelScale = 11.2684294733435
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitle = 'Birth'
renderView1.AxesGrid.YTitle = 'Death'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [822, 611]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.717007488012314, 0.630256831645966, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [0.488509495015511, 0.534003638276636, 1.14148710832862]
renderView2.CameraFocalPoint = [0.488509495015511, 0.534003638276636, 0.0]
renderView2.CameraParallelScale = 0.633298884235501
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitle = 'Magnitude'
renderView2.AxesGrid.YTitle = 'Curl'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [822, 610]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.717007488012314, 0.630256831645966, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [0.488509495015511, 0.534003638276636, 1.14148710832862]
renderView3.CameraFocalPoint = [0.488509495015511, 0.534003638276636, 0.0]
renderView3.CameraParallelScale = 0.633298884235501
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1
renderView3.AxesGrid.XTitle = 'Magnitude'
renderView3.AxesGrid.YTitle = 'Curl'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [773, 610]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.717007488012314, 0.630256831645966, 0.0]
renderView4.StereoType = 0
renderView4.CameraPosition = [0.488509495015511, 0.534003638276636, 1.14148710832862]
renderView4.CameraFocalPoint = [0.488509495015511, 0.534003638276636, 0.0]
renderView4.CameraParallelScale = 0.633298884235501
renderView4.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.Visibility = 1
renderView4.AxesGrid.XTitle = 'Magnitude'
renderView4.AxesGrid.YTitle = 'Curl'
renderView4.AxesGrid.XTitleFontFile = ''
renderView4.AxesGrid.YTitleFontFile = ''
renderView4.AxesGrid.ZTitleFontFile = ''
renderView4.AxesGrid.XLabelFontFile = ''
renderView4.AxesGrid.YLabelFontFile = ''
renderView4.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
mechanicalvtu = XMLUnstructuredGridReader(FileName=['mechanical.vtu'])
mechanicalvtu.PointArrayStatus = ['magnitude', 'curl']

# create a new 'TTK ReebSpace'
tTKReebSpace1 = TTKReebSpace(Input=mechanicalvtu)
tTKReebSpace1.UComponent = 'magnitude'
tTKReebSpace1.VComponent = 'curl'
tTKReebSpace1.Uoffsetfield = ''
tTKReebSpace1.Voffsetfield = ''
tTKReebSpace1.SimplificationThreshold = 0.05

# find source
tTKReebSpace1_1 = FindSource('TTKReebSpace1')

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=OutputPort(tTKReebSpace1_1,1))

# find source
tTKReebSpace1_2 = FindSource('TTKReebSpace1')

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKReebSpace1_2,3))
threshold1.Scalars = ['POINTS', '3-SheetId']
threshold1.ThresholdRange = [0.0, 6.0]

# create a new 'Threshold'
threshold5 = Threshold(Input=threshold1)
threshold5.Scalars = ['POINTS', '3-SheetId']
threshold5.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
a3sheet3 = Threshold(Input=threshold1)
a3sheet3.Scalars = ['POINTS', '3-SheetId']
a3sheet3.ThresholdRange = [3.0, 3.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField4 = TTKProjectionFromField(Input=a3sheet3)
tTKProjectionFromField4.UComponent = 'magnitude'
tTKProjectionFromField4.VComponent = 'curl'

# create a new 'Threshold'
a3sheet4 = Threshold(Input=threshold1)
a3sheet4.Scalars = ['POINTS', '3-SheetId']
a3sheet4.ThresholdRange = [4.0, 4.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField5 = TTKProjectionFromField(Input=a3sheet4)
tTKProjectionFromField5.UComponent = 'magnitude'
tTKProjectionFromField5.VComponent = 'curl'
tTKProjectionFromField5.DebugLevel = 13

# create a new 'Threshold'
a3sheet2 = Threshold(Input=threshold1)
a3sheet2.Scalars = ['POINTS', '3-SheetId']
a3sheet2.ThresholdRange = [2.0, 2.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField3 = TTKProjectionFromField(Input=a3sheet2)
tTKProjectionFromField3.UComponent = 'magnitude'
tTKProjectionFromField3.VComponent = 'curl'

# create a new 'Threshold'
a3sheetIdselectionthreshold = Threshold(Input=threshold1)
a3sheetIdselectionthreshold.Scalars = ['POINTS', '3-SheetId']
a3sheetIdselectionthreshold.ThresholdRange = [4.0, 4.0]

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot2 = TTKContinuousScatterPlot(Input=a3sheetIdselectionthreshold)
tTKContinuousScatterPlot2.ScalarField1 = 'magnitude'
tTKContinuousScatterPlot2.ScalarField2 = 'curl'

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKContinuousScatterPlot2)
threshold3.Scalars = ['POINTS', 'ValidPointMask']
threshold3.ThresholdRange = [1.0, 1.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField1 = TTKProjectionFromField(Input=a3sheetIdselectionthreshold)
tTKProjectionFromField1.UComponent = 'magnitude'
tTKProjectionFromField1.VComponent = 'curl'

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKProjectionFromField1)

# create a new 'Threshold'
a3sheet5 = Threshold(Input=threshold1)
a3sheet5.Scalars = ['POINTS', '3-SheetId']
a3sheet5.ThresholdRange = [5.0, 5.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField6 = TTKProjectionFromField(Input=a3sheet5)
tTKProjectionFromField6.UComponent = 'magnitude'
tTKProjectionFromField6.VComponent = 'curl'

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot1 = TTKContinuousScatterPlot(Input=mechanicalvtu)
tTKContinuousScatterPlot1.ScalarField1 = 'magnitude'
tTKContinuousScatterPlot1.ScalarField2 = 'curl'

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKContinuousScatterPlot1)
threshold2.Scalars = ['POINTS', 'ValidPointMask']
threshold2.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold2)

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=extractSurface3)
resampleToImage1.SamplingDimensions = [1920, 1080, 1]
resampleToImage1.SamplingBounds = [0.0745950043201447, 0.959481716156006, 0.0409988947212696, 0.936145842075348, 0.0, 0.0]

# create a new 'Threshold'
threshold4 = Threshold(Input=resampleToImage1)
threshold4.Scalars = ['POINTS', 'vtkValidPointMask']
threshold4.ThresholdRange = [1.0, 1.0]

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'VertexIds']
tube1.Vectors = [None, '']
tube1.Radius = 0.0125

# create a new 'Threshold'
threshold6 = Threshold(Input=threshold1)
threshold6.Scalars = ['POINTS', '3-SheetId']
threshold6.ThresholdRange = [6.0, 6.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField7 = TTKProjectionFromField(Input=threshold6)
tTKProjectionFromField7.UComponent = 'magnitude'
tTKProjectionFromField7.VComponent = 'curl'

# create a new 'TTK ProjectionFromField'
a3sheet1 = TTKProjectionFromField(Input=threshold5)
a3sheet1.UComponent = 'magnitude'
a3sheet1.VComponent = 'curl'

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=threshold4)

# create a new 'Feature Edges'
featureEdges2 = FeatureEdges(Input=extractSurface4)
featureEdges2.FeatureEdges = 0
featureEdges2.NonManifoldEdges = 0

# create a new 'Tube'
tube3 = Tube(Input=featureEdges2)
tube3.Scalars = ['POINTS', '3-SheetDomainVolume']
tube3.Vectors = [None, '']
tube3.Radius = 0.01

# create a new 'Threshold'
a3sheet0 = Threshold(Input=threshold1)
a3sheet0.Scalars = ['POINTS', '3-SheetId']

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField2 = TTKProjectionFromField(Input=a3sheet0)
tTKProjectionFromField2.UComponent = 'magnitude'
tTKProjectionFromField2.VComponent = 'curl'

# create a new 'Feature Edges'
featureEdges1 = FeatureEdges(Input=extractSurface2)
featureEdges1.FeatureEdges = 0
featureEdges1.NonManifoldEdges = 0

# create a new 'Tube'
tube2 = Tube(Input=featureEdges1)
tube2.Scalars = ['POINTS', 'Density']
tube2.Vectors = [None, '']
tube2.Radius = 0.0075

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=a3sheetIdselectionthreshold)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=extractSurface5)
tTKGeometrySmoother1.IterationNumber = 2

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKReebSpace1
tTKReebSpace1Display = Show(tTKReebSpace1, renderView1)

# trace defaults for the display properties.
tTKReebSpace1Display.Representation = 'Surface'
tTKReebSpace1Display.ColorArrayName = [None, '']
tTKReebSpace1Display.Specular = 1.0
tTKReebSpace1Display.OSPRayScaleArray = '0-SheetId'
tTKReebSpace1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKReebSpace1Display.SelectOrientationVectors = '0-SheetId'
tTKReebSpace1Display.ScaleFactor = 1.57274298667908
tTKReebSpace1Display.SelectScaleArray = '0-SheetId'
tTKReebSpace1Display.GlyphType = 'Arrow'
tTKReebSpace1Display.GaussianRadius = 0.786371493339539
tTKReebSpace1Display.CustomShader = ''
tTKReebSpace1Display.SetScaleArray = ['POINTS', '0-SheetId']
tTKReebSpace1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display.OpacityArray = ['POINTS', '0-SheetId']
tTKReebSpace1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKReebSpace1Display.SelectionCellLabelFontFile = ''
tTKReebSpace1Display.SelectionPointLabelFontFile = ''
tTKReebSpace1Display.PolarAxes = 'PolarAxesRepresentation'
tTKReebSpace1Display.ScalarOpacityUnitDistance = 22.5243576703289

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKReebSpace1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKReebSpace1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKReebSpace1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKReebSpace1Display.DataAxesGrid.XTitleFontFile = ''
tTKReebSpace1Display.DataAxesGrid.YTitleFontFile = ''
tTKReebSpace1Display.DataAxesGrid.ZTitleFontFile = ''
tTKReebSpace1Display.DataAxesGrid.XLabelFontFile = ''
tTKReebSpace1Display.DataAxesGrid.YLabelFontFile = ''
tTKReebSpace1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKReebSpace1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKReebSpace1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKReebSpace1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKReebSpace1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# find source
tTKReebSpace1_3 = FindSource('TTKReebSpace1')

# show data from tTKReebSpace1_3
tTKReebSpace1Display_1 = Show(OutputPort(tTKReebSpace1, 2), renderView1)

# trace defaults for the display properties.
tTKReebSpace1Display_1.Representation = 'Surface'
tTKReebSpace1Display_1.ColorArrayName = [None, '']
tTKReebSpace1Display_1.Specular = 1.0
tTKReebSpace1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKReebSpace1Display_1.SelectOrientationVectors = 'None'
tTKReebSpace1Display_1.ScaleFactor = -2e+298
tTKReebSpace1Display_1.SelectScaleArray = 'None'
tTKReebSpace1Display_1.GlyphType = 'Arrow'
tTKReebSpace1Display_1.GaussianRadius = -1e+298
tTKReebSpace1Display_1.CustomShader = ''
tTKReebSpace1Display_1.SetScaleArray = [None, '']
tTKReebSpace1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display_1.OpacityArray = [None, '']
tTKReebSpace1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKReebSpace1Display_1.SelectionCellLabelFontFile = ''
tTKReebSpace1Display_1.SelectionPointLabelFontFile = ''
tTKReebSpace1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKReebSpace1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKReebSpace1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKReebSpace1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKReebSpace1Display_1.DataAxesGrid.XTitleFontFile = ''
tTKReebSpace1Display_1.DataAxesGrid.YTitleFontFile = ''
tTKReebSpace1Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKReebSpace1Display_1.DataAxesGrid.XLabelFontFile = ''
tTKReebSpace1Display_1.DataAxesGrid.YLabelFontFile = ''
tTKReebSpace1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKReebSpace1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKReebSpace1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKReebSpace1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKReebSpace1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView1)

# get color transfer function/color map for 'EdgeType'
edgeTypeLUT = GetColorTransferFunction('EdgeType')
edgeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.129412, 0.584314]
edgeTypeLUT.ColorSpace = 'RGB'
edgeTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
edgeTypeLUT.NanColor = [0.0, 0.0, 0.0]
edgeTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['CELLS', 'EdgeType']
tube1Display.LookupTable = edgeTypeLUT
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'TubeNormals'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'None'
tube1Display.ScaleFactor = 1.60406193733215
tube1Display.SelectScaleArray = 'None'
tube1Display.GlyphType = 'Arrow'
tube1Display.GaussianRadius = 0.802030968666077
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'VertexIds']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'VertexIds']
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

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)

# get color transfer function/color map for 'a3SheetId'
a3SheetIdLUT = GetColorTransferFunction('a3SheetId')
a3SheetIdLUT.RGBPoints = [0.0, 0.278431372549, 0.278431372549, 0.858823529412, 0.86246875, 0.0, 0.0, 0.360784313725, 1.71890625, 0.0, 1.0, 1.0, 2.58740625, 0.0, 0.501960784314, 0.0, 3.44384375, 1.0, 1.0, 0.0, 4.3063125, 1.0, 0.380392156863, 0.0, 5.16878125, 0.419607843137, 0.0, 0.0, 6.03125, 0.878431372549, 0.301960784314, 0.301960784314]
a3SheetIdLUT.ColorSpace = 'RGB'
a3SheetIdLUT.AboveRangeColor = [1.0, 1.0, 1.0]
a3SheetIdLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'a3SheetId'
a3SheetIdPWF = GetOpacityTransferFunction('a3SheetId')
a3SheetIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 6.03125, 1.0, 0.5, 0.0]
a3SheetIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface With Edges'
threshold1Display.ColorArrayName = ['POINTS', '3-SheetId']
threshold1Display.LookupTable = a3SheetIdLUT
threshold1Display.Opacity = 0.2
threshold1Display.Specular = 1.0
threshold1Display.OSPRayScaleArray = '3-SheetDomainVolume'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = '3-SheetDomainVolume'
threshold1Display.ScaleFactor = 1.57047400474548
threshold1Display.SelectScaleArray = '3-SheetDomainVolume'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GaussianRadius = 0.785237002372742
threshold1Display.CustomShader = ''
threshold1Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = a3SheetIdPWF
threshold1Display.ScalarOpacityUnitDistance = 0.233636415724598

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from tTKGeometrySmoother1
tTKGeometrySmoother1Display = Show(tTKGeometrySmoother1, renderView1)

# trace defaults for the display properties.
tTKGeometrySmoother1Display.Representation = 'Surface'
tTKGeometrySmoother1Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKGeometrySmoother1Display.LookupTable = a3SheetIdLUT
tTKGeometrySmoother1Display.Specular = 1.0
tTKGeometrySmoother1Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKGeometrySmoother1Display.ScaleFactor = 0.23617582321167
tTKGeometrySmoother1Display.SelectScaleArray = '3-SheetDomainVolume'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GaussianRadius = 0.118087911605835
tTKGeometrySmoother1Display.CustomShader = ''
tTKGeometrySmoother1Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKGeometrySmoother1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKGeometrySmoother1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother1Display.SelectionCellLabelFontFile = ''
tTKGeometrySmoother1Display.SelectionPointLabelFontFile = ''
tTKGeometrySmoother1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKGeometrySmoother1Display.DataAxesGrid.XTitleFontFile = ''
tTKGeometrySmoother1Display.DataAxesGrid.YTitleFontFile = ''
tTKGeometrySmoother1Display.DataAxesGrid.ZTitleFontFile = ''
tTKGeometrySmoother1Display.DataAxesGrid.XLabelFontFile = ''
tTKGeometrySmoother1Display.DataAxesGrid.YLabelFontFile = ''
tTKGeometrySmoother1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKGeometrySmoother1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKGeometrySmoother1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKGeometrySmoother1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKGeometrySmoother1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from threshold2
threshold2Display = Show(threshold2, renderView2)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.RGBPoints = [2.63387318127067e-06, 0.0, 0.129412, 0.584314, 813.80490623255, 0.917647, 0.941176, 0.788235, 1808.45549151133, 0.0352941176470588, 0.450980392156863, 0.0274509803921569, 5967.90292301215, 0.0, 0.431373, 0.0]
densityLUT.ColorSpace = 'RGB'
densityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
densityLUT.NanColor = [0.0, 0.0, 0.0]
densityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [2.63387318127067e-06, 0.0, 0.5, 0.0, 5967.90292301215, 1.0, 0.5, 0.0]
densityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', 'Density']
threshold2Display.LookupTable = densityLUT
threshold2Display.Specular = 1.0
threshold2Display.OSPRayScaleArray = 'Density'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'Density'
threshold2Display.ScaleFactor = 0.0998146431869827
threshold2Display.SelectScaleArray = 'Density'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GaussianRadius = 0.0499073215934914
threshold2Display.CustomShader = ''
threshold2Display.SetScaleArray = ['POINTS', 'Density']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'Density']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.SelectionCellLabelFontFile = ''
threshold2Display.SelectionPointLabelFontFile = ''
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = densityPWF
threshold2Display.ScalarOpacityUnitDistance = 0.0154618596905715

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold2Display.DataAxesGrid.XTitleFontFile = ''
threshold2Display.DataAxesGrid.YTitleFontFile = ''
threshold2Display.DataAxesGrid.ZTitleFontFile = ''
threshold2Display.DataAxesGrid.XLabelFontFile = ''
threshold2Display.DataAxesGrid.YLabelFontFile = ''
threshold2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold2Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold2Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold2Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from extractSurface4
extractSurface4Display = Show(extractSurface4, renderView2)

# trace defaults for the display properties.
extractSurface4Display.Representation = 'Surface'
extractSurface4Display.ColorArrayName = ['POINTS', '3-SheetId']
extractSurface4Display.LookupTable = a3SheetIdLUT
extractSurface4Display.Opacity = 0.3
extractSurface4Display.Specular = 1.0
extractSurface4Display.OSPRayScaleArray = '3-SheetDomainVolume'
extractSurface4Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface4Display.SelectOrientationVectors = '3-SheetDomainVolume'
extractSurface4Display.ScaleFactor = 0.069106337428093
extractSurface4Display.SelectScaleArray = '3-SheetDomainVolume'
extractSurface4Display.GlyphType = 'Arrow'
extractSurface4Display.GaussianRadius = 0.0345531687140465
extractSurface4Display.CustomShader = ''
extractSurface4Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
extractSurface4Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface4Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
extractSurface4Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface4Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface4Display.SelectionCellLabelFontFile = ''
extractSurface4Display.SelectionPointLabelFontFile = ''
extractSurface4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface4Display.DataAxesGrid.XTitleFontFile = ''
extractSurface4Display.DataAxesGrid.YTitleFontFile = ''
extractSurface4Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface4Display.DataAxesGrid.XLabelFontFile = ''
extractSurface4Display.DataAxesGrid.YLabelFontFile = ''
extractSurface4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface4Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface4Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface4Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube3
tube3Display = Show(tube3, renderView2)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', '3-SheetId']
tube3Display.LookupTable = a3SheetIdLUT
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = '3-SheetDomainVolume'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = '3-SheetDomainVolume'
tube3Display.ScaleFactor = 0.0703032940626144
tube3Display.SelectScaleArray = '3-SheetDomainVolume'
tube3Display.GlyphType = 'Arrow'
tube3Display.GaussianRadius = 0.0351516470313072
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tube2
tube2Display = Show(tube2, renderView3)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'Density'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Density'
tube2Display.ScaleFactor = 0.101450807275251
tube2Display.SelectScaleArray = 'Density'
tube2Display.GlyphType = 'Arrow'
tube2Display.GaussianRadius = 0.0507254036376253
tube2Display.CustomShader = ''
tube2Display.SetScaleArray = ['POINTS', 'Density']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'Density']
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

# show data from threshold3
threshold3Display = Show(threshold3, renderView3)

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['POINTS', 'Density']
threshold3Display.LookupTable = densityLUT
threshold3Display.Specular = 1.0
threshold3Display.OSPRayScaleArray = 'Density'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'Density'
threshold3Display.ScaleFactor = 0.0997434316668659
threshold3Display.SelectScaleArray = 'Density'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GaussianRadius = 0.049871715833433
threshold3Display.CustomShader = ''
threshold3Display.SetScaleArray = ['POINTS', 'Density']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'Density']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.SelectionCellLabelFontFile = ''
threshold3Display.SelectionPointLabelFontFile = ''
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = densityPWF
threshold3Display.ScalarOpacityUnitDistance = 0.0185088673015957

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold3Display.DataAxesGrid.XTitleFontFile = ''
threshold3Display.DataAxesGrid.YTitleFontFile = ''
threshold3Display.DataAxesGrid.ZTitleFontFile = ''
threshold3Display.DataAxesGrid.XLabelFontFile = ''
threshold3Display.DataAxesGrid.YLabelFontFile = ''
threshold3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold3Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold3Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold3Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from tTKProjectionFromField2
tTKProjectionFromField2Display = Show(tTKProjectionFromField2, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField2Display.Representation = 'Surface'
tTKProjectionFromField2Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField2Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField2Display.Specular = 1.0
tTKProjectionFromField2Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField2Display.ScaleFactor = 0.0895146947354078
tTKProjectionFromField2Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField2Display.GlyphType = 'Arrow'
tTKProjectionFromField2Display.GaussianRadius = 0.0447573473677039
tTKProjectionFromField2Display.CustomShader = ''
tTKProjectionFromField2Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField2Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField2Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField2Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField2Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField2Display.ScalarOpacityUnitDistance = 0.0187848030673354

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField2Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField2Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField2Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField2Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField2Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display_1 = Show(tube2, renderView4)

# trace defaults for the display properties.
tube2Display_1.Representation = 'Surface'
tube2Display_1.ColorArrayName = [None, '']
tube2Display_1.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube2Display_1.Specular = 1.0
tube2Display_1.OSPRayScaleArray = 'Density'
tube2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display_1.SelectOrientationVectors = 'Density'
tube2Display_1.ScaleFactor = 0.101450807275251
tube2Display_1.SelectScaleArray = 'Density'
tube2Display_1.GlyphType = 'Arrow'
tube2Display_1.GaussianRadius = 0.0507254036376253
tube2Display_1.CustomShader = ''
tube2Display_1.SetScaleArray = ['POINTS', 'Density']
tube2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display_1.OpacityArray = ['POINTS', 'Density']
tube2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube2Display_1.SelectionCellLabelFontFile = ''
tube2Display_1.SelectionPointLabelFontFile = ''
tube2Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display_1.DataAxesGrid.XTitleFontFile = ''
tube2Display_1.DataAxesGrid.YTitleFontFile = ''
tube2Display_1.DataAxesGrid.ZTitleFontFile = ''
tube2Display_1.DataAxesGrid.XLabelFontFile = ''
tube2Display_1.DataAxesGrid.YLabelFontFile = ''
tube2Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from a3sheet1
a3sheet1Display = Show(a3sheet1, renderView4)

# trace defaults for the display properties.
a3sheet1Display.Representation = 'Surface'
a3sheet1Display.ColorArrayName = ['POINTS', '3-SheetId']
a3sheet1Display.LookupTable = a3SheetIdLUT
a3sheet1Display.Specular = 1.0
a3sheet1Display.OSPRayScaleArray = '3-SheetDomainVolume'
a3sheet1Display.OSPRayScaleFunction = 'PiecewiseFunction'
a3sheet1Display.SelectOrientationVectors = '3-SheetDomainVolume'
a3sheet1Display.ScaleFactor = 0.0305299341678619
a3sheet1Display.SelectScaleArray = '3-SheetDomainVolume'
a3sheet1Display.GlyphType = 'Arrow'
a3sheet1Display.GaussianRadius = 0.015264967083931
a3sheet1Display.CustomShader = ''
a3sheet1Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
a3sheet1Display.ScaleTransferFunction = 'PiecewiseFunction'
a3sheet1Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
a3sheet1Display.OpacityTransferFunction = 'PiecewiseFunction'
a3sheet1Display.DataAxesGrid = 'GridAxesRepresentation'
a3sheet1Display.SelectionCellLabelFontFile = ''
a3sheet1Display.SelectionPointLabelFontFile = ''
a3sheet1Display.PolarAxes = 'PolarAxesRepresentation'
a3sheet1Display.ScalarOpacityFunction = a3SheetIdPWF
a3sheet1Display.ScalarOpacityUnitDistance = 0.0151632225917311

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
a3sheet1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a3sheet1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a3sheet1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
a3sheet1Display.DataAxesGrid.XTitleFontFile = ''
a3sheet1Display.DataAxesGrid.YTitleFontFile = ''
a3sheet1Display.DataAxesGrid.ZTitleFontFile = ''
a3sheet1Display.DataAxesGrid.XLabelFontFile = ''
a3sheet1Display.DataAxesGrid.YLabelFontFile = ''
a3sheet1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
a3sheet1Display.PolarAxes.PolarAxisTitleFontFile = ''
a3sheet1Display.PolarAxes.PolarAxisLabelFontFile = ''
a3sheet1Display.PolarAxes.LastRadialAxisTextFontFile = ''
a3sheet1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField3
tTKProjectionFromField3Display = Show(tTKProjectionFromField3, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField3Display.Representation = 'Surface'
tTKProjectionFromField3Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField3Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField3Display.Specular = 1.0
tTKProjectionFromField3Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField3Display.ScaleFactor = 0.0999286562378984
tTKProjectionFromField3Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField3Display.GlyphType = 'Arrow'
tTKProjectionFromField3Display.GaussianRadius = 0.0499643281189492
tTKProjectionFromField3Display.CustomShader = ''
tTKProjectionFromField3Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField3Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField3Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField3Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField3Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField3Display.ScalarOpacityUnitDistance = 0.0165109198317988

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField3Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField3Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField3Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField3Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField3Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField4
tTKProjectionFromField4Display = Show(tTKProjectionFromField4, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField4Display.Representation = 'Surface'
tTKProjectionFromField4Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField4Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField4Display.Specular = 1.0
tTKProjectionFromField4Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField4Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField4Display.ScaleFactor = 0.0289884239435196
tTKProjectionFromField4Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField4Display.GlyphType = 'Arrow'
tTKProjectionFromField4Display.GaussianRadius = 0.0144942119717598
tTKProjectionFromField4Display.CustomShader = ''
tTKProjectionFromField4Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField4Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField4Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField4Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField4Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField4Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField4Display.ScalarOpacityUnitDistance = 0.0110647473388987

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField4Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField4Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField4Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField4Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField4Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField4Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField4Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField5
tTKProjectionFromField5Display = Show(tTKProjectionFromField5, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField5Display.Representation = 'Surface'
tTKProjectionFromField5Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField5Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField5Display.Specular = 1.0
tTKProjectionFromField5Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField5Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField5Display.ScaleFactor = 0.0436394095420837
tTKProjectionFromField5Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField5Display.GlyphType = 'Arrow'
tTKProjectionFromField5Display.GaussianRadius = 0.0218197047710419
tTKProjectionFromField5Display.CustomShader = ''
tTKProjectionFromField5Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField5Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField5Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField5Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField5Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField5Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField5Display.ScalarOpacityUnitDistance = 0.0103039394868335

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField5Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField5Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField5Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField5Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField5Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField5Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField5Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField6
tTKProjectionFromField6Display = Show(tTKProjectionFromField6, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField6Display.Representation = 'Surface'
tTKProjectionFromField6Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField6Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField6Display.Specular = 1.0
tTKProjectionFromField6Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField6Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField6Display.ScaleFactor = 0.0545133650302887
tTKProjectionFromField6Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField6Display.GlyphType = 'Arrow'
tTKProjectionFromField6Display.GaussianRadius = 0.0272566825151443
tTKProjectionFromField6Display.CustomShader = ''
tTKProjectionFromField6Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField6Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField6Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField6Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField6Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField6Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField6Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField6Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField6Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField6Display.ScalarOpacityUnitDistance = 0.0130303073263627

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField6Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField6Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField6Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField6Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField6Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField6Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField6Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField6Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField6Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField6Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField6Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField7
tTKProjectionFromField7Display = Show(tTKProjectionFromField7, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField7Display.Representation = 'Surface'
tTKProjectionFromField7Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField7Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField7Display.Specular = 1.0
tTKProjectionFromField7Display.OSPRayScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField7Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField7Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField7Display.ScaleFactor = 0.0268349915742874
tTKProjectionFromField7Display.SelectScaleArray = '3-SheetDomainVolume'
tTKProjectionFromField7Display.GlyphType = 'Arrow'
tTKProjectionFromField7Display.GaussianRadius = 0.0134174957871437
tTKProjectionFromField7Display.CustomShader = ''
tTKProjectionFromField7Display.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField7Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField7Display.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tTKProjectionFromField7Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField7Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField7Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField7Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField7Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField7Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField7Display.ScalarOpacityUnitDistance = 0.0101120488095086

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField7Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField7Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField7Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField7Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField7Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField7Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField7Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField7Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField7Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField7Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField7Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube3
tube3Display_1 = Show(tube3, renderView4)

# trace defaults for the display properties.
tube3Display_1.Representation = 'Surface'
tube3Display_1.ColorArrayName = ['POINTS', '3-SheetId']
tube3Display_1.LookupTable = a3SheetIdLUT
tube3Display_1.Specular = 1.0
tube3Display_1.OSPRayScaleArray = '3-SheetDomainVolume'
tube3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display_1.SelectOrientationVectors = '3-SheetDomainVolume'
tube3Display_1.ScaleFactor = 0.0447554796934128
tube3Display_1.SelectScaleArray = '3-SheetDomainVolume'
tube3Display_1.GlyphType = 'Arrow'
tube3Display_1.GaussianRadius = 0.0223777398467064
tube3Display_1.CustomShader = ''
tube3Display_1.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
tube3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display_1.OpacityArray = ['POINTS', '3-SheetDomainVolume']
tube3Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube3Display_1.SelectionCellLabelFontFile = ''
tube3Display_1.SelectionPointLabelFontFile = ''
tube3Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube3Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube3Display_1.DataAxesGrid.XTitleFontFile = ''
tube3Display_1.DataAxesGrid.YTitleFontFile = ''
tube3Display_1.DataAxesGrid.ZTitleFontFile = ''
tube3Display_1.DataAxesGrid.XLabelFontFile = ''
tube3Display_1.DataAxesGrid.YLabelFontFile = ''
tube3Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube3Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tube3Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tube3Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tube3Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from extractSurface4
extractSurface4Display_1 = Show(extractSurface4, renderView4)

# trace defaults for the display properties.
extractSurface4Display_1.Representation = 'Surface'
extractSurface4Display_1.ColorArrayName = ['POINTS', '3-SheetId']
extractSurface4Display_1.LookupTable = a3SheetIdLUT
extractSurface4Display_1.Specular = 1.0
extractSurface4Display_1.OSPRayScaleArray = '3-SheetDomainVolume'
extractSurface4Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface4Display_1.SelectOrientationVectors = '3-SheetDomainVolume'
extractSurface4Display_1.ScaleFactor = 0.0435585230588913
extractSurface4Display_1.SelectScaleArray = '3-SheetDomainVolume'
extractSurface4Display_1.GlyphType = 'Arrow'
extractSurface4Display_1.GaussianRadius = 0.0217792615294456
extractSurface4Display_1.CustomShader = ''
extractSurface4Display_1.SetScaleArray = ['POINTS', '3-SheetDomainVolume']
extractSurface4Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface4Display_1.OpacityArray = ['POINTS', '3-SheetDomainVolume']
extractSurface4Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface4Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractSurface4Display_1.SelectionCellLabelFontFile = ''
extractSurface4Display_1.SelectionPointLabelFontFile = ''
extractSurface4Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface4Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface4Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface4Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface4Display_1.DataAxesGrid.XTitleFontFile = ''
extractSurface4Display_1.DataAxesGrid.YTitleFontFile = ''
extractSurface4Display_1.DataAxesGrid.ZTitleFontFile = ''
extractSurface4Display_1.DataAxesGrid.XLabelFontFile = ''
extractSurface4Display_1.DataAxesGrid.YLabelFontFile = ''
extractSurface4Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface4Display_1.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface4Display_1.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface4Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface4Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'EdgeType'
edgeTypePWF = GetOpacityTransferFunction('EdgeType')
edgeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
edgeTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------tTKReebSpace1.DebugLevel = int(debugLevel)
if tTKReebSpace1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKReebSpace1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKReebSpace1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKReebSpace1, i)))
else:
	SaveData(outputDirectory + 'tTKReebSpace1.vtu',
		CleantoGrid(OutputPort(tTKReebSpace1)))
tTKProjectionFromField4.DebugLevel = int(debugLevel)
if tTKProjectionFromField4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField4, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField4.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField4)))
tTKProjectionFromField5.DebugLevel = int(debugLevel)
if tTKProjectionFromField5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField5, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField5.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField5)))
tTKProjectionFromField3.DebugLevel = int(debugLevel)
if tTKProjectionFromField3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField3, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField3.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField3)))
tTKContinuousScatterPlot2.DebugLevel = int(debugLevel)
if tTKContinuousScatterPlot2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKContinuousScatterPlot2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKContinuousScatterPlot2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKContinuousScatterPlot2, i)))
else:
	SaveData(outputDirectory + 'tTKContinuousScatterPlot2.vtu',
		CleantoGrid(OutputPort(tTKContinuousScatterPlot2)))
tTKProjectionFromField1.DebugLevel = int(debugLevel)
if tTKProjectionFromField1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField1, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField1.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField1)))
tTKProjectionFromField6.DebugLevel = int(debugLevel)
if tTKProjectionFromField6.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField6.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField6_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField6, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField6.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField6)))
tTKContinuousScatterPlot1.DebugLevel = int(debugLevel)
if tTKContinuousScatterPlot1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKContinuousScatterPlot1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKContinuousScatterPlot1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKContinuousScatterPlot1, i)))
else:
	SaveData(outputDirectory + 'tTKContinuousScatterPlot1.vtu',
		CleantoGrid(OutputPort(tTKContinuousScatterPlot1)))
tTKProjectionFromField7.DebugLevel = int(debugLevel)
if tTKProjectionFromField7.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField7.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField7_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField7, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField7.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField7)))
tTKProjectionFromField2.DebugLevel = int(debugLevel)
if tTKProjectionFromField2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField2, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField2.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField2)))
tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
