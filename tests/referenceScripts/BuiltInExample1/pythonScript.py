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
a3DWarp = CreateView('RenderView')
a3DWarp.ViewSize = [751, 1252]
a3DWarp.AxesGrid = 'GridAxes3DActor'
a3DWarp.OrientationAxesVisibility = 0
a3DWarp.CenterOfRotation = [32.0, -256.0, 0.0]
a3DWarp.StereoType = 0
a3DWarp.CameraPosition = [317.275758920842, 469.779731687591, 327.180648793585]
a3DWarp.CameraFocalPoint = [-13.7118672101019, -265.393226178892, 94.8437903141333]
a3DWarp.CameraViewUp = [-0.13454429652009, -0.243018800495004, 0.960645457429474]
a3DWarp.CameraParallelScale = 344.199413722482
a3DWarp.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
a3DWarp.AxesGrid.XTitleFontFile = ''
a3DWarp.AxesGrid.YTitleFontFile = ''
a3DWarp.AxesGrid.ZTitleFontFile = ''
a3DWarp.AxesGrid.XLabelFontFile = ''
a3DWarp.AxesGrid.YLabelFontFile = ''
a3DWarp.AxesGrid.ZLabelFontFile = ''

# Create a new 'Line Chart View'
persistenceCurve = CreateView('XYChartView')
persistenceCurve.ViewSize = [563, 611]
persistenceCurve.ChartTitleFontFile = ''
persistenceCurve.LegendPosition = [334, 569]
persistenceCurve.LeftAxisTitle = 'Number of Pairs'
persistenceCurve.LeftAxisTitleFontFile = ''
persistenceCurve.LeftAxisLogScale = 1
persistenceCurve.LeftAxisUseCustomRange = 1
persistenceCurve.LeftAxisRangeMinimum = 0.958957943163809
persistenceCurve.LeftAxisRangeMaximum = 1059.62327057131
persistenceCurve.LeftAxisLabelFontFile = ''
persistenceCurve.BottomAxisTitle = 'Persistence'
persistenceCurve.BottomAxisTitleFontFile = ''
persistenceCurve.BottomAxisLogScale = 1
persistenceCurve.BottomAxisUseCustomRange = 1
persistenceCurve.BottomAxisRangeMinimum = 8.34199382720694e-07
persistenceCurve.BottomAxisRangeMaximum = 1.18316606452145
persistenceCurve.BottomAxisLabelFontFile = ''
persistenceCurve.RightAxisLabelFontFile = ''
persistenceCurve.TopAxisTitleFontFile = ''
persistenceCurve.TopAxisLabelFontFile = ''

# Create a new 'Render View'
persistenceDiagram = CreateView('RenderView')
persistenceDiagram.ViewSize = [563, 610]
persistenceDiagram.InteractionMode = '2D'
persistenceDiagram.AxesGrid = 'GridAxes3DActor'
persistenceDiagram.OrientationAxesVisibility = 0
persistenceDiagram.CenterOfRotation = [0.389500730550765, 0.500000976837157, 0.0]
persistenceDiagram.StereoType = 0
persistenceDiagram.CameraPosition = [0.368720206702922, 0.508313186376294, 10000.0]
persistenceDiagram.CameraFocalPoint = [0.368720206702922, 0.508313186376294, 0.0]
persistenceDiagram.CameraParallelScale = 0.633805977359223
persistenceDiagram.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
persistenceDiagram.AxesGrid.Visibility = 1
persistenceDiagram.AxesGrid.XTitle = 'Birth'
persistenceDiagram.AxesGrid.YTitle = 'Death'
persistenceDiagram.AxesGrid.XTitleFontFile = ''
persistenceDiagram.AxesGrid.YTitleFontFile = ''
persistenceDiagram.AxesGrid.ZTitleFontFile = ''
persistenceDiagram.AxesGrid.XLabelFontFile = ''
persistenceDiagram.AxesGrid.YLabelFontFile = ''
persistenceDiagram.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
vorticity = CreateView('RenderView')
vorticity.ViewSize = [272, 1252]
vorticity.InteractionMode = '2D'
vorticity.AxesGrid = 'GridAxes3DActor'
vorticity.OrientationAxesVisibility = 0
vorticity.CenterOfRotation = [32.0000000000001, -256.0, 0.0]
vorticity.StereoType = 0
vorticity.CameraPosition = [32.0000000000001, -256.0, 1035.83091921264]
vorticity.CameraFocalPoint = [32.0000000000001, -256.0, 0.0]
vorticity.CameraParallelScale = 268.803351668986
vorticity.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
vorticity.AxesGrid.XTitleFontFile = ''
vorticity.AxesGrid.YTitleFontFile = ''
vorticity.AxesGrid.ZTitleFontFile = ''
vorticity.AxesGrid.XLabelFontFile = ''
vorticity.AxesGrid.YLabelFontFile = ''
vorticity.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(a3DWarp)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample1.vti'])
builtInExamplevti.PointArrayStatus = ['Vectors_']

# create a new 'Transform'
transform1 = Transform(Input=builtInExamplevti)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Rotate = [0.0, 0.0, -90.0]

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=transform1)
computeDerivatives1.Scalars = [None, '']
computeDerivatives1.Vectors = ['POINTS', 'Vectors_']
computeDerivatives1.OutputVectorType = 'Vorticity'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData1)
calculator1.ResultArrayName = 'myVorticity'
calculator1.Function = 'Vorticity_Z'

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = 'myVorticity'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=tTKScalarFieldNormalizer1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'myVorticity'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram1)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'Threshold'
persistencePairs = Threshold(Input=tTKPersistenceDiagram1)
persistencePairs.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs.ThresholdRange = [-0.1, 957.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=persistencePairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.02, 1.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 0.025
tTKSphereFromPoint1.ThetaResolution = 10

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint1)
tTKTopologicalSimplification1.ScalarField = 'myVorticity'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tTKTopologicalSimplification1)
warpByScalar1.Scalars = ['POINTS', 'myVorticity']
warpByScalar1.ScaleFactor = 300.0
warpByScalar1.UseNormal = 1

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.015

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=warpByScalar1)
tTKScalarFieldCriticalPoints1.ScalarField = 'myVorticity'
tTKScalarFieldCriticalPoints1.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 5.0

# create a new 'Threshold'
maxima = Threshold(Input=tTKSphereFromPoint2)
maxima.Scalars = ['POINTS', 'CriticalIndex']
maxima.ThresholdRange = [1.9, 2.0]

# create a new 'Threshold'
minima = Threshold(Input=tTKSphereFromPoint2)
minima.Scalars = ['POINTS', 'CriticalIndex']
minima.ThresholdRange = [0.0, 0.1]

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(Input=tetrahedralize1)
tTKPersistenceCurve1.ScalarField = 'myVorticity'
tTKPersistenceCurve1.InputOffsetField = ''

# ----------------------------------------------------------------
# setup the visualization in view 'a3DWarp'
# ----------------------------------------------------------------

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, a3DWarp)

# get color transfer function/color map for 'myVorticity'
myVorticityLUT = GetColorTransferFunction('myVorticity')
myVorticityLUT.RGBPoints = [-0.742480184882879, 0.0, 0.129412, 0.584314, 0.475, 0.0156862745098039, 0.141176470588235, 0.588235294117647, 0.52, 0.917647, 0.941176, 0.788235, 0.55, 0.0509803921568627, 0.458823529411765, 0.0431372549019608, 1.000001, 0.0, 0.431373, 0.0]
myVorticityLUT.ColorSpace = 'RGB'
myVorticityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
myVorticityLUT.NanColor = [0.0, 0.0, 0.0]
myVorticityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'myVorticity'
myVorticityPWF = GetOpacityTransferFunction('myVorticity')
myVorticityPWF.Points = [-0.742480184882879, 0.0, 0.5, 0.0, 1.000001, 1.0, 0.5, 0.0]
myVorticityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'myVorticity']
warpByScalar1Display.LookupTable = myVorticityLUT
warpByScalar1Display.Specular = 1.0
warpByScalar1Display.OSPRayScaleArray = 'OutputOffsetScalarField'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.ScaleFactor = 3334.4
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.CustomShader = ''
warpByScalar1Display.SetScaleArray = ['POINTS', 'OutputOffsetScalarField']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'OutputOffsetScalarField']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.SelectionCellLabelFontFile = ''
warpByScalar1Display.SelectionPointLabelFontFile = ''
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = myVorticityPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 827.134964286673

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
warpByScalar1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
warpByScalar1Display.DataAxesGrid.XTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.YTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.ZTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.XLabelFontFile = ''
warpByScalar1Display.DataAxesGrid.YLabelFontFile = ''
warpByScalar1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
warpByScalar1Display.PolarAxes.PolarAxisTitleFontFile = ''
warpByScalar1Display.PolarAxes.PolarAxisLabelFontFile = ''
warpByScalar1Display.PolarAxes.LastRadialAxisTextFontFile = ''
warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from minima
minimaDisplay = Show(minima, a3DWarp)

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [-1.0, 0.0, 0.0, 0.0, 6.66673333332701e-06, 0.0, 0.129411764705882, 0.584313725490196, 1.00001333346667, 0.917647, 0.941176, 0.788235, 2.0000200002, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0000200002, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
minimaDisplay.Representation = 'Surface'
minimaDisplay.ColorArrayName = ['POINTS', 'CriticalIndex']
minimaDisplay.LookupTable = criticalTypeLUT
minimaDisplay.Specular = 1.0
minimaDisplay.OSPRayScaleArray = 'CriticalIndex'
minimaDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
minimaDisplay.ScaleFactor = 48.3965831756592
minimaDisplay.GlyphType = 'Arrow'
minimaDisplay.CustomShader = ''
minimaDisplay.SetScaleArray = ['POINTS', 'CriticalIndex']
minimaDisplay.ScaleTransferFunction = 'PiecewiseFunction'
minimaDisplay.OpacityArray = ['POINTS', 'CriticalIndex']
minimaDisplay.OpacityTransferFunction = 'PiecewiseFunction'
minimaDisplay.DataAxesGrid = 'GridAxesRepresentation'
minimaDisplay.SelectionCellLabelFontFile = ''
minimaDisplay.SelectionPointLabelFontFile = ''
minimaDisplay.PolarAxes = 'PolarAxesRepresentation'
minimaDisplay.ScalarOpacityFunction = criticalTypePWF
minimaDisplay.ScalarOpacityUnitDistance = 23.2471523228504

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
minimaDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
minimaDisplay.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
minimaDisplay.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
minimaDisplay.DataAxesGrid.XTitleFontFile = ''
minimaDisplay.DataAxesGrid.YTitleFontFile = ''
minimaDisplay.DataAxesGrid.ZTitleFontFile = ''
minimaDisplay.DataAxesGrid.XLabelFontFile = ''
minimaDisplay.DataAxesGrid.YLabelFontFile = ''
minimaDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
minimaDisplay.PolarAxes.PolarAxisTitleFontFile = ''
minimaDisplay.PolarAxes.PolarAxisLabelFontFile = ''
minimaDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
minimaDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from maxima
maximaDisplay = Show(maxima, a3DWarp)

# trace defaults for the display properties.
maximaDisplay.Representation = 'Surface'
maximaDisplay.ColorArrayName = ['POINTS', 'CriticalIndex']
maximaDisplay.LookupTable = criticalTypeLUT
maximaDisplay.Specular = 1.0
maximaDisplay.OSPRayScaleArray = 'CriticalIndex'
maximaDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
maximaDisplay.ScaleFactor = 46.0965831756592
maximaDisplay.GlyphType = 'Arrow'
maximaDisplay.CustomShader = ''
maximaDisplay.SetScaleArray = ['POINTS', 'CriticalIndex']
maximaDisplay.ScaleTransferFunction = 'PiecewiseFunction'
maximaDisplay.OpacityArray = ['POINTS', 'CriticalIndex']
maximaDisplay.OpacityTransferFunction = 'PiecewiseFunction'
maximaDisplay.DataAxesGrid = 'GridAxesRepresentation'
maximaDisplay.SelectionCellLabelFontFile = ''
maximaDisplay.SelectionPointLabelFontFile = ''
maximaDisplay.PolarAxes = 'PolarAxesRepresentation'
maximaDisplay.ScalarOpacityFunction = criticalTypePWF
maximaDisplay.ScalarOpacityUnitDistance = 22.6471753908021

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maximaDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maximaDisplay.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maximaDisplay.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
maximaDisplay.DataAxesGrid.XTitleFontFile = ''
maximaDisplay.DataAxesGrid.YTitleFontFile = ''
maximaDisplay.DataAxesGrid.ZTitleFontFile = ''
maximaDisplay.DataAxesGrid.XLabelFontFile = ''
maximaDisplay.DataAxesGrid.YLabelFontFile = ''
maximaDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
maximaDisplay.PolarAxes.PolarAxisTitleFontFile = ''
maximaDisplay.PolarAxes.PolarAxisLabelFontFile = ''
maximaDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
maximaDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'persistenceCurve'
# ----------------------------------------------------------------

# find source
tTKPersistenceCurve1_1 = FindSource('TTKPersistenceCurve1')

# show data from tTKPersistenceCurve1_1
tTKPersistenceCurve1Display = Show(OutputPort(tTKPersistenceCurve1, 3), persistenceCurve)

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
# setup the visualization in view 'persistenceDiagram'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, persistenceDiagram)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.36078431372549, 0.36078431372549, 0.36078431372549]
tube1Display.Specular = 1.0
tube1Display.SpecularPower = 50.0
tube1Display.OSPRayScaleArray = 'NodeType'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.ScaleFactor = 0.0788540237117559
tube1Display.GlyphType = 'Arrow'
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
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, persistenceDiagram)

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
tTKSphereFromPoint1Display.ScaleFactor = 0.199658441543579
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
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
tube2Display = Show(tube2, persistenceDiagram)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Specular = 1.0
tube2Display.SpecularPower = 50.0
tube2Display.OSPRayScaleArray = 'NodeType'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.ScaleFactor = 0.0999999953674319
tube2Display.GlyphType = 'Arrow'
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
# setup the visualization in view 'vorticity'
# ----------------------------------------------------------------

# show data from tetrahedralize1
tetrahedralize1Display = Show(tetrahedralize1, vorticity)

# trace defaults for the display properties.
tetrahedralize1Display.Representation = 'Surface'
tetrahedralize1Display.ColorArrayName = ['POINTS', 'myVorticity']
tetrahedralize1Display.LookupTable = myVorticityLUT
tetrahedralize1Display.Specular = 1.0
tetrahedralize1Display.OSPRayScaleArray = 'VectorGradient'
tetrahedralize1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tetrahedralize1Display.ScaleFactor = 51.2
tetrahedralize1Display.GlyphType = 'Arrow'
tetrahedralize1Display.CustomShader = ''
tetrahedralize1Display.SetScaleArray = ['POINTS', 'myVorticity']
tetrahedralize1Display.ScaleTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display.OpacityArray = ['POINTS', 'myVorticity']
tetrahedralize1Display.OpacityTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display.DataAxesGrid = 'GridAxesRepresentation'
tetrahedralize1Display.SelectionCellLabelFontFile = ''
tetrahedralize1Display.SelectionPointLabelFontFile = ''
tetrahedralize1Display.PolarAxes = 'PolarAxesRepresentation'
tetrahedralize1Display.ScalarOpacityFunction = myVorticityPWF
tetrahedralize1Display.ScalarOpacityUnitDistance = 12.7980364308879

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tetrahedralize1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tetrahedralize1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tetrahedralize1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tetrahedralize1Display.DataAxesGrid.XTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.YTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.ZTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.XLabelFontFile = ''
tetrahedralize1Display.DataAxesGrid.YLabelFontFile = ''
tetrahedralize1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tetrahedralize1Display.PolarAxes.PolarAxisTitleFontFile = ''
tetrahedralize1Display.PolarAxes.PolarAxisLabelFontFile = ''
tetrahedralize1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tetrahedralize1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from minima
minimaDisplay_1 = Show(minima, vorticity)

# trace defaults for the display properties.
minimaDisplay_1.Representation = 'Surface'
minimaDisplay_1.ColorArrayName = ['POINTS', 'CriticalIndex']
minimaDisplay_1.LookupTable = criticalTypeLUT
minimaDisplay_1.Specular = 1.0
minimaDisplay_1.OSPRayScaleArray = 'CriticalIndex'
minimaDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
minimaDisplay_1.ScaleFactor = 48.3965831756592
minimaDisplay_1.GlyphType = 'Arrow'
minimaDisplay_1.CustomShader = ''
minimaDisplay_1.SetScaleArray = ['POINTS', 'CriticalIndex']
minimaDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
minimaDisplay_1.OpacityArray = ['POINTS', 'CriticalIndex']
minimaDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
minimaDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
minimaDisplay_1.SelectionCellLabelFontFile = ''
minimaDisplay_1.SelectionPointLabelFontFile = ''
minimaDisplay_1.PolarAxes = 'PolarAxesRepresentation'
minimaDisplay_1.ScalarOpacityFunction = criticalTypePWF
minimaDisplay_1.ScalarOpacityUnitDistance = 23.2471523228504

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
minimaDisplay_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
minimaDisplay_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
minimaDisplay_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
minimaDisplay_1.DataAxesGrid.XTitleFontFile = ''
minimaDisplay_1.DataAxesGrid.YTitleFontFile = ''
minimaDisplay_1.DataAxesGrid.ZTitleFontFile = ''
minimaDisplay_1.DataAxesGrid.XLabelFontFile = ''
minimaDisplay_1.DataAxesGrid.YLabelFontFile = ''
minimaDisplay_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
minimaDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
minimaDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
minimaDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
minimaDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from maxima
maximaDisplay_1 = Show(maxima, vorticity)

# trace defaults for the display properties.
maximaDisplay_1.Representation = 'Surface'
maximaDisplay_1.ColorArrayName = ['POINTS', 'CriticalIndex']
maximaDisplay_1.LookupTable = criticalTypeLUT
maximaDisplay_1.Specular = 1.0
maximaDisplay_1.OSPRayScaleArray = 'CriticalIndex'
maximaDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
maximaDisplay_1.ScaleFactor = 46.0965831756592
maximaDisplay_1.GlyphType = 'Arrow'
maximaDisplay_1.CustomShader = ''
maximaDisplay_1.SetScaleArray = ['POINTS', 'CriticalIndex']
maximaDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
maximaDisplay_1.OpacityArray = ['POINTS', 'CriticalIndex']
maximaDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
maximaDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
maximaDisplay_1.SelectionCellLabelFontFile = ''
maximaDisplay_1.SelectionPointLabelFontFile = ''
maximaDisplay_1.PolarAxes = 'PolarAxesRepresentation'
maximaDisplay_1.ScalarOpacityFunction = criticalTypePWF
maximaDisplay_1.ScalarOpacityUnitDistance = 22.6471753908021

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maximaDisplay_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maximaDisplay_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maximaDisplay_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
maximaDisplay_1.DataAxesGrid.XTitleFontFile = ''
maximaDisplay_1.DataAxesGrid.YTitleFontFile = ''
maximaDisplay_1.DataAxesGrid.ZTitleFontFile = ''
maximaDisplay_1.DataAxesGrid.XLabelFontFile = ''
maximaDisplay_1.DataAxesGrid.YLabelFontFile = ''
maximaDisplay_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
maximaDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
maximaDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
maximaDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
maximaDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------tTKScalarFieldNormalizer1.DebugLevel = int(debugLevel)
if tTKScalarFieldNormalizer1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldNormalizer1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldNormalizer1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldNormalizer1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldNormalizer1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldNormalizer1)))
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
tTKScalarFieldCriticalPoints1.DebugLevel = int(debugLevel)
if tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1)))
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
tTKPersistenceCurve1.DebugLevel = int(debugLevel)
if tTKPersistenceCurve1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceCurve1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceCurve1_' + str(i) + '.vtk',
			OutputPort(tTKPersistenceCurve1, i))
else:
	SaveData(outputDirectory + 'tTKPersistenceCurve1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceCurve1)))
