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
renderView1.ViewSize = [798, 611]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.500000000000007, 0.5, -1.0547118733939e-15]
renderView1.StereoType = 0
renderView1.CameraPosition = [-0.731020048691096, 1.74757771221334, -1.36845223319578]
renderView1.CameraFocalPoint = [0.486946217940843, 0.499132911540707, 0.0107428990826124]
renderView1.CameraViewUp = [0.33018770050097, 0.826269639458471, 0.456349170424413]
renderView1.CameraParallelScale = 1.23363670975111
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
renderView2.ViewSize = [797, 611]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, 0.500000005820766, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [0.0259054347444046, 0.51297921859193, 10000.0]
renderView2.CameraFocalPoint = [0.0259054347444046, 0.51297921859193, 0.0]
renderView2.CameraParallelScale = 0.65834000979047
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitle = 'u'
renderView2.AxesGrid.YTitle = 'v'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [797, 610]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.0, 0.500000005820766, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [0.0259054347444046, 0.51297921859193, 10000.0]
renderView3.CameraFocalPoint = [0.0259054347444046, 0.51297921859193, 0.0]
renderView3.CameraParallelScale = 0.65834000979047
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1
renderView3.AxesGrid.XTitle = 'u'
renderView3.AxesGrid.YTitle = 'v'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [798, 610]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.0, 0.500000005820766, 0.0]
renderView4.StereoType = 0
renderView4.CameraPosition = [0.0259054347444046, 0.51297921859193, 10000.0]
renderView4.CameraFocalPoint = [0.0259054347444046, 0.51297921859193, 0.0]
renderView4.CameraParallelScale = 0.65834000979047
renderView4.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.Visibility = 1
renderView4.AxesGrid.XTitle = 'u'
renderView4.AxesGrid.YTitle = 'v'
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
bivariateToyvtu = XMLUnstructuredGridReader(FileName=['bivariateToy.vtu'])

# create a new 'Transform'
transform1 = Transform(Input=bivariateToyvtu)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.00541578717330643, 0.0148061334965645, 0.141327167699776]
transform1.Transform.Rotate = [10.1720909852194, 27.8134114635651, -5.8843291901696]
transform1.Transform.Scale = [1.00000000000001, 0.999999999999994, 0.999999999999992]

# create a new 'Calculator'
calculator1 = Calculator(Input=transform1)
calculator1.ResultArrayName = 'u'
calculator1.Function = 'coordsZ'

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.ResultArrayName = 'v'
calculator2.Function = 'coordsY'

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot1 = TTKContinuousScatterPlot(Input=calculator2)
tTKContinuousScatterPlot1.ScalarField1 = 'u'
tTKContinuousScatterPlot1.ScalarField2 = 'v'

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKContinuousScatterPlot1)
threshold2.Scalars = ['POINTS', 'ValidPointMask']
threshold2.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold2)

# create a new 'Feature Edges'
featureEdges1 = FeatureEdges(Input=extractSurface3)
featureEdges1.FeatureEdges = 0
featureEdges1.NonManifoldEdges = 0

# create a new 'Tube'
tube2 = Tube(Input=featureEdges1)
tube2.Scalars = ['POINTS', 'Density']
tube2.Vectors = [None, '']
tube2.Radius = 0.00986887728795409

# create a new 'TTK ReebSpace'
tTKReebSpace1 = TTKReebSpace(Input=calculator2)
tTKReebSpace1.UComponent = 'u'
tTKReebSpace1.VComponent = 'v'
tTKReebSpace1.Uoffsetfield = ''
tTKReebSpace1.Voffsetfield = ''

# find source
tTKReebSpace1_1 = FindSource('TTKReebSpace1')

# create a new 'Threshold'
threshold6 = Threshold(Input=OutputPort(tTKReebSpace1_1,3))
threshold6.Scalars = ['POINTS', '3-SheetId']
threshold6.ThresholdRange = [3.0, 3.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField3 = TTKProjectionFromField(Input=threshold6)
tTKProjectionFromField3.UComponent = 'u'
tTKProjectionFromField3.VComponent = 'v'

# create a new 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKReebSpace1_1,3))
threshold5.Scalars = ['POINTS', '3-SheetId']
threshold5.ThresholdRange = [1.0, 1.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField2 = TTKProjectionFromField(Input=threshold5)
tTKProjectionFromField2.UComponent = 'u'
tTKProjectionFromField2.VComponent = 'v'

# find source
tTKReebSpace1_2 = FindSource('TTKReebSpace1')

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=OutputPort(tTKReebSpace1_2,1))

# create a new 'Tube'
tube1 = Tube(Input=extractSurface2)
tube1.Scalars = ['POINTS', 'VertexIds']
tube1.Vectors = [None, '']
tube1.Radius = 0.00989168415777385

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKReebSpace1_1,3))
threshold4.Scalars = ['POINTS', '3-SheetId']

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKReebSpace1_1,3))
threshold1.Scalars = ['POINTS', '3-SheetId']
threshold1.ThresholdRange = [0.0, 3.0]

# create a new 'Threshold'
a3sheetIdselectionthreshold = Threshold(Input=threshold1)
a3sheetIdselectionthreshold.Scalars = ['POINTS', '3-SheetId']
a3sheetIdselectionthreshold.ThresholdRange = [1.0, 1.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField4 = TTKProjectionFromField(Input=a3sheetIdselectionthreshold)
tTKProjectionFromField4.UComponent = 'u'
tTKProjectionFromField4.VComponent = 'v'

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKProjectionFromField4)

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot2 = TTKContinuousScatterPlot(Input=a3sheetIdselectionthreshold)
tTKContinuousScatterPlot2.ScalarField1 = 'u'
tTKContinuousScatterPlot2.ScalarField2 = 'v'

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKContinuousScatterPlot2)
threshold3.Scalars = ['POINTS', 'ValidPointMask']
threshold3.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=a3sheetIdselectionthreshold)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=extractSurface1)
tTKGeometrySmoother1.IterationNumber = 2

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField1 = TTKProjectionFromField(Input=threshold4)
tTKProjectionFromField1.UComponent = 'u'
tTKProjectionFromField1.VComponent = 'v'

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=extractSurface4)
resampleToImage1.SamplingDimensions = [1920, 1080, 1]
resampleToImage1.SamplingBounds = [-0.435284703969955, 0.435284703969955, 0.0060984012670815, 0.607737004756927, 0.0, 0.0]

# create a new 'Threshold'
threshold7 = Threshold(Input=resampleToImage1)
threshold7.Scalars = ['POINTS', 'vtkValidPointMask']
threshold7.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=threshold7)

# create a new 'Feature Edges'
featureEdges2 = FeatureEdges(Input=extractSurface5)
featureEdges2.FeatureEdges = 0
featureEdges2.NonManifoldEdges = 0

# create a new 'Tube'
tube3 = Tube(Input=featureEdges2)
tube3.Scalars = ['POINTS', 'v']
tube3.Vectors = [None, '']
tube3.Radius = 0.015

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKReebSpace1
tTKReebSpace1Display = Show(tTKReebSpace1, renderView1)

# get color transfer function/color map for 'v'
vLUT = GetColorTransferFunction('v')
vLUT.RGBPoints = [-0.0583422966301441, 0.0, 0.129412, 0.584314, 0.500000020489097, 0.917647, 0.941176, 0.788235, 1.05834233760834, 0.0, 0.431373, 0.0]
vLUT.ColorSpace = 'RGB'
vLUT.AboveRangeColor = [1.0, 1.0, 1.0]
vLUT.NanColor = [0.0, 0.0, 0.0]
vLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'v'
vPWF = GetOpacityTransferFunction('v')
vPWF.Points = [-0.0583422966301441, 0.0, 0.5, 0.0, 1.05834233760834, 1.0, 0.5, 0.0]
vPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKReebSpace1Display.Representation = 'Surface'
tTKReebSpace1Display.ColorArrayName = ['POINTS', 'v']
tTKReebSpace1Display.LookupTable = vLUT
tTKReebSpace1Display.Specular = 1.0
tTKReebSpace1Display.OSPRayScaleArray = '0-SheetId'
tTKReebSpace1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKReebSpace1Display.SelectOrientationVectors = '0-SheetId'
tTKReebSpace1Display.ScaleFactor = 0.0870569407939911
tTKReebSpace1Display.SelectScaleArray = '0-SheetId'
tTKReebSpace1Display.GlyphType = 'Arrow'
tTKReebSpace1Display.GaussianRadius = 0.0435284703969955
tTKReebSpace1Display.CustomShader = ''
tTKReebSpace1Display.SetScaleArray = ['POINTS', '0-SheetId']
tTKReebSpace1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display.OpacityArray = ['POINTS', '0-SheetId']
tTKReebSpace1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKReebSpace1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKReebSpace1Display.SelectionCellLabelFontFile = ''
tTKReebSpace1Display.SelectionPointLabelFontFile = ''
tTKReebSpace1Display.PolarAxes = 'PolarAxesRepresentation'
tTKReebSpace1Display.ScalarOpacityFunction = vPWF
tTKReebSpace1Display.ScalarOpacityUnitDistance = 0.999999967790502

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

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)

# get color transfer function/color map for 'a3SheetId'
a3SheetIdLUT = GetColorTransferFunction('a3SheetId')
a3SheetIdLUT.AutomaticRescaleRangeMode = 'Never'
a3SheetIdLUT.RGBPoints = [0.0, 0.278431372549, 0.278431372549, 0.858823529412, 0.431234375, 0.0, 0.0, 0.360784313725, 0.859453125, 0.0, 1.0, 1.0, 0.959517002105713, 0.0, 0.886274509803922, 0.772549019607843, 0.977793514728546, 0.0, 0.858823529411765, 0.72156862745098, 1.00520825386047, 0.0, 0.827450980392157, 0.654901960784314, 1.01434659957886, 0.0, 0.815686274509804, 0.631372549019608, 1.05089962482452, 0.0, 0.780392156862745, 0.556862745098039, 1.293703125, 0.0, 0.501960784314, 0.0, 1.721921875, 1.0, 1.0, 0.0, 2.15315625, 1.0, 0.380392156863, 0.0, 2.584390625, 0.419607843137, 0.0, 0.0, 3.015625, 0.878431372549, 0.301960784314, 0.301960784314]
a3SheetIdLUT.ColorSpace = 'RGB'
a3SheetIdLUT.AboveRangeColor = [1.0, 1.0, 1.0]
a3SheetIdLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'a3SheetId'
a3SheetIdPWF = GetOpacityTransferFunction('a3SheetId')
a3SheetIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.015625, 1.0, 0.5, 0.0]
a3SheetIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', '3-SheetId']
threshold1Display.LookupTable = a3SheetIdLUT
threshold1Display.Opacity = 0.2
threshold1Display.Specular = 1.0
threshold1Display.OSPRayScaleArray = 'v'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = '3-SheetDomainVolume'
threshold1Display.ScaleFactor = 0.0989168415777385
threshold1Display.SelectScaleArray = 'v'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GaussianRadius = 0.0494584207888693
threshold1Display.CustomShader = ''
threshold1Display.SetScaleArray = ['POINTS', 'v']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'v']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = a3SheetIdPWF
threshold1Display.ScalarOpacityUnitDistance = 0.0123706372828334

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
tTKGeometrySmoother1Display.OSPRayScaleArray = 'v'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKGeometrySmoother1Display.ScaleFactor = 0.0910582879558206
tTKGeometrySmoother1Display.SelectScaleArray = 'v'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GaussianRadius = 0.0455291439779103
tTKGeometrySmoother1Display.CustomShader = ''
tTKGeometrySmoother1Display.SetScaleArray = ['POINTS', 'v']
tTKGeometrySmoother1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.OpacityArray = ['POINTS', 'v']
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
tube1Display.ScaleFactor = 0.10042881751433
tube1Display.SelectScaleArray = 'None'
tube1Display.GlyphType = 'Arrow'
tube1Display.GaussianRadius = 0.0502144087571651
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from extractSurface3
extractSurface3Display = Show(extractSurface3, renderView2)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.RGBPoints = [2.58756248437169e-08, 0.0, 0.129412, 0.584314, 0.283443165295471, 0.917647, 0.941176, 0.788235, 0.748289853303464, 0.0, 0.431373, 0.0]
densityLUT.ColorSpace = 'RGB'
densityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
densityLUT.NanColor = [0.0, 0.0, 0.0]
densityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
extractSurface3Display.Representation = 'Surface'
extractSurface3Display.ColorArrayName = ['POINTS', 'Density']
extractSurface3Display.LookupTable = densityLUT
extractSurface3Display.Specular = 1.0
extractSurface3Display.OSPRayScaleArray = 'Density'
extractSurface3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface3Display.SelectOrientationVectors = 'Density'
extractSurface3Display.ScaleFactor = 0.0986887728795409
extractSurface3Display.SelectScaleArray = 'Density'
extractSurface3Display.GlyphType = 'Arrow'
extractSurface3Display.GaussianRadius = 0.0493443864397705
extractSurface3Display.CustomShader = ''
extractSurface3Display.SetScaleArray = ['POINTS', 'Density']
extractSurface3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface3Display.OpacityArray = ['POINTS', 'Density']
extractSurface3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface3Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface3Display.SelectionCellLabelFontFile = ''
extractSurface3Display.SelectionPointLabelFontFile = ''
extractSurface3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface3Display.DataAxesGrid.XTitleFontFile = ''
extractSurface3Display.DataAxesGrid.YTitleFontFile = ''
extractSurface3Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface3Display.DataAxesGrid.XLabelFontFile = ''
extractSurface3Display.DataAxesGrid.YLabelFontFile = ''
extractSurface3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface3Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface3Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface3Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube3
tube3Display = Show(tube3, renderView2)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', '3-SheetId']
tube3Display.LookupTable = a3SheetIdLUT
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'v'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = '3-SheetDomainVolume'
tube3Display.ScaleFactor = 0.089966207742691
tube3Display.SelectScaleArray = 'v'
tube3Display.GlyphType = 'Arrow'
tube3Display.GaussianRadius = 0.0449831038713455
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', 'v']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'v']
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

# show data from extractSurface5
extractSurface5Display = Show(extractSurface5, renderView2)

# trace defaults for the display properties.
extractSurface5Display.Representation = 'Surface'
extractSurface5Display.ColorArrayName = ['POINTS', '3-SheetId']
extractSurface5Display.LookupTable = a3SheetIdLUT
extractSurface5Display.Opacity = 0.3
extractSurface5Display.Specular = 1.0
extractSurface5Display.OSPRayScaleArray = 'v'
extractSurface5Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface5Display.SelectOrientationVectors = '3-SheetDomainVolume'
extractSurface5Display.ScaleFactor = 0.086966210603714
extractSurface5Display.SelectScaleArray = 'v'
extractSurface5Display.GlyphType = 'Arrow'
extractSurface5Display.GaussianRadius = 0.043483105301857
extractSurface5Display.CustomShader = ''
extractSurface5Display.SetScaleArray = ['POINTS', 'v']
extractSurface5Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface5Display.OpacityArray = ['POINTS', 'v']
extractSurface5Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface5Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface5Display.SelectionCellLabelFontFile = ''
extractSurface5Display.SelectionPointLabelFontFile = ''
extractSurface5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface5Display.DataAxesGrid.XTitleFontFile = ''
extractSurface5Display.DataAxesGrid.YTitleFontFile = ''
extractSurface5Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface5Display.DataAxesGrid.XLabelFontFile = ''
extractSurface5Display.DataAxesGrid.YLabelFontFile = ''
extractSurface5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface5Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface5Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface5Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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
tube2Display.ScaleFactor = 0.100398113729898
tube2Display.SelectScaleArray = 'Density'
tube2Display.GlyphType = 'Arrow'
tube2Display.GaussianRadius = 0.0501990568649489
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

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [2.58756248437169e-08, 0.0, 0.5, 0.0, 0.748289853303464, 1.0, 0.5, 0.0]
densityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['POINTS', 'Density']
threshold3Display.LookupTable = densityLUT
threshold3Display.Specular = 1.0
threshold3Display.OSPRayScaleArray = 'Density'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'Density'
threshold3Display.ScaleFactor = 0.0870115756988525
threshold3Display.SelectScaleArray = 'Density'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GaussianRadius = 0.0435057878494263
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
threshold3Display.ScalarOpacityUnitDistance = 0.00765047232684098

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
tube2Display_1.ScaleFactor = 0.100398113729898
tube2Display_1.SelectScaleArray = 'Density'
tube2Display_1.GlyphType = 'Arrow'
tube2Display_1.GaussianRadius = 0.0501990568649489
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

# show data from tTKProjectionFromField1
tTKProjectionFromField1Display = Show(tTKProjectionFromField1, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField1Display.Representation = 'Surface'
tTKProjectionFromField1Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField1Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField1Display.Specular = 1.0
tTKProjectionFromField1Display.OSPRayScaleArray = 'v'
tTKProjectionFromField1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField1Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField1Display.ScaleFactor = 0.0870569407939911
tTKProjectionFromField1Display.SelectScaleArray = 'v'
tTKProjectionFromField1Display.GlyphType = 'Arrow'
tTKProjectionFromField1Display.GaussianRadius = 0.0435284703969955
tTKProjectionFromField1Display.CustomShader = ''
tTKProjectionFromField1Display.SetScaleArray = ['POINTS', 'v']
tTKProjectionFromField1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField1Display.OpacityArray = ['POINTS', 'v']
tTKProjectionFromField1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField1Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField1Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField1Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField1Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField1Display.ScalarOpacityUnitDistance = 0.0091464592503902

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKProjectionFromField1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKProjectionFromField1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKProjectionFromField1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKProjectionFromField1Display.DataAxesGrid.XTitleFontFile = ''
tTKProjectionFromField1Display.DataAxesGrid.YTitleFontFile = ''
tTKProjectionFromField1Display.DataAxesGrid.ZTitleFontFile = ''
tTKProjectionFromField1Display.DataAxesGrid.XLabelFontFile = ''
tTKProjectionFromField1Display.DataAxesGrid.YLabelFontFile = ''
tTKProjectionFromField1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKProjectionFromField1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKProjectionFromField1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKProjectionFromField1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKProjectionFromField1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKProjectionFromField2
tTKProjectionFromField2Display = Show(tTKProjectionFromField2, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField2Display.Representation = 'Surface'
tTKProjectionFromField2Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField2Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField2Display.Specular = 1.0
tTKProjectionFromField2Display.OSPRayScaleArray = 'v'
tTKProjectionFromField2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField2Display.ScaleFactor = 0.0837306827306747
tTKProjectionFromField2Display.SelectScaleArray = 'v'
tTKProjectionFromField2Display.GlyphType = 'Arrow'
tTKProjectionFromField2Display.GaussianRadius = 0.0418653413653374
tTKProjectionFromField2Display.CustomShader = ''
tTKProjectionFromField2Display.SetScaleArray = ['POINTS', 'v']
tTKProjectionFromField2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.OpacityArray = ['POINTS', 'v']
tTKProjectionFromField2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField2Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField2Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField2Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField2Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField2Display.ScalarOpacityUnitDistance = 0.0147119993545041

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

# show data from tTKProjectionFromField3
tTKProjectionFromField3Display = Show(tTKProjectionFromField3, renderView4)

# trace defaults for the display properties.
tTKProjectionFromField3Display.Representation = 'Surface'
tTKProjectionFromField3Display.ColorArrayName = ['POINTS', '3-SheetId']
tTKProjectionFromField3Display.LookupTable = a3SheetIdLUT
tTKProjectionFromField3Display.Specular = 1.0
tTKProjectionFromField3Display.OSPRayScaleArray = 'v'
tTKProjectionFromField3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.SelectOrientationVectors = '3-SheetDomainVolume'
tTKProjectionFromField3Display.ScaleFactor = 0.0843647509813309
tTKProjectionFromField3Display.SelectScaleArray = 'v'
tTKProjectionFromField3Display.GlyphType = 'Arrow'
tTKProjectionFromField3Display.GaussianRadius = 0.0421823754906654
tTKProjectionFromField3Display.CustomShader = ''
tTKProjectionFromField3Display.SetScaleArray = ['POINTS', 'v']
tTKProjectionFromField3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.OpacityArray = ['POINTS', 'v']
tTKProjectionFromField3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKProjectionFromField3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKProjectionFromField3Display.SelectionCellLabelFontFile = ''
tTKProjectionFromField3Display.SelectionPointLabelFontFile = ''
tTKProjectionFromField3Display.PolarAxes = 'PolarAxesRepresentation'
tTKProjectionFromField3Display.ScalarOpacityFunction = a3SheetIdPWF
tTKProjectionFromField3Display.ScalarOpacityUnitDistance = 0.0134343178851545

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

# show data from extractSurface5
extractSurface5Display_1 = Show(extractSurface5, renderView4)

# trace defaults for the display properties.
extractSurface5Display_1.Representation = 'Surface'
extractSurface5Display_1.ColorArrayName = ['POINTS', '3-SheetId']
extractSurface5Display_1.LookupTable = a3SheetIdLUT
extractSurface5Display_1.Specular = 1.0
extractSurface5Display_1.OSPRayScaleArray = 'v'
extractSurface5Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface5Display_1.SelectOrientationVectors = '3-SheetDomainVolume'
extractSurface5Display_1.ScaleFactor = 0.086966210603714
extractSurface5Display_1.SelectScaleArray = 'v'
extractSurface5Display_1.GlyphType = 'Arrow'
extractSurface5Display_1.GaussianRadius = 0.043483105301857
extractSurface5Display_1.CustomShader = ''
extractSurface5Display_1.SetScaleArray = ['POINTS', 'v']
extractSurface5Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface5Display_1.OpacityArray = ['POINTS', 'v']
extractSurface5Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface5Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractSurface5Display_1.SelectionCellLabelFontFile = ''
extractSurface5Display_1.SelectionPointLabelFontFile = ''
extractSurface5Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface5Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface5Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface5Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface5Display_1.DataAxesGrid.XTitleFontFile = ''
extractSurface5Display_1.DataAxesGrid.YTitleFontFile = ''
extractSurface5Display_1.DataAxesGrid.ZTitleFontFile = ''
extractSurface5Display_1.DataAxesGrid.XLabelFontFile = ''
extractSurface5Display_1.DataAxesGrid.YLabelFontFile = ''
extractSurface5Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface5Display_1.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface5Display_1.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface5Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface5Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube3
tube3Display_1 = Show(tube3, renderView4)

# trace defaults for the display properties.
tube3Display_1.Representation = 'Surface'
tube3Display_1.ColorArrayName = ['POINTS', '3-SheetId']
tube3Display_1.LookupTable = a3SheetIdLUT
tube3Display_1.Specular = 1.0
tube3Display_1.OSPRayScaleArray = 'v'
tube3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display_1.SelectOrientationVectors = '3-SheetDomainVolume'
tube3Display_1.ScaleFactor = 0.089966207742691
tube3Display_1.SelectScaleArray = 'v'
tube3Display_1.GlyphType = 'Arrow'
tube3Display_1.GaussianRadius = 0.0449831038713455
tube3Display_1.CustomShader = ''
tube3Display_1.SetScaleArray = ['POINTS', 'v']
tube3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display_1.OpacityArray = ['POINTS', 'v']
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
# ----------------------------------------------------------------tTKContinuousScatterPlot1.DebugLevel = int(debugLevel)
if tTKContinuousScatterPlot1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKContinuousScatterPlot1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKContinuousScatterPlot1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKContinuousScatterPlot1, i)))
else:
	SaveData(outputDirectory + 'tTKContinuousScatterPlot1.vtu',
		CleantoGrid(OutputPort(tTKContinuousScatterPlot1)))
tTKReebSpace1.DebugLevel = int(debugLevel)
if tTKReebSpace1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKReebSpace1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKReebSpace1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKReebSpace1, i)))
else:
	SaveData(outputDirectory + 'tTKReebSpace1.vtu',
		CleantoGrid(OutputPort(tTKReebSpace1)))
tTKProjectionFromField3.DebugLevel = int(debugLevel)
if tTKProjectionFromField3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField3, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField3.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField3)))
tTKProjectionFromField2.DebugLevel = int(debugLevel)
if tTKProjectionFromField2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField2, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField2.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField2)))
tTKProjectionFromField4.DebugLevel = int(debugLevel)
if tTKProjectionFromField4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField4, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField4.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField4)))
tTKContinuousScatterPlot2.DebugLevel = int(debugLevel)
if tTKContinuousScatterPlot2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKContinuousScatterPlot2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKContinuousScatterPlot2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKContinuousScatterPlot2, i)))
else:
	SaveData(outputDirectory + 'tTKContinuousScatterPlot2.vtu',
		CleantoGrid(OutputPort(tTKContinuousScatterPlot2)))
tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
tTKProjectionFromField1.DebugLevel = int(debugLevel)
if tTKProjectionFromField1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKProjectionFromField1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKProjectionFromField1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKProjectionFromField1, i)))
else:
	SaveData(outputDirectory + 'tTKProjectionFromField1.vtu',
		CleantoGrid(OutputPort(tTKProjectionFromField1)))
