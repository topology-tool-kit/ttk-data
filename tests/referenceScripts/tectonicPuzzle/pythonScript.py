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

# Create a new 'Histogram View'
histogramView1 = CreateView('XYHistogramChartView')
histogramView1.ViewSize = [797, 355]
histogramView1.ChartTitleFontFile = ''
histogramView1.LeftAxisTitleFontFile = ''
histogramView1.LeftAxisRangeMaximum = 1400.0
histogramView1.LeftAxisLabelFontFile = ''
histogramView1.BottomAxisTitleFontFile = ''
histogramView1.BottomAxisRangeMinimum = -1.0
histogramView1.BottomAxisRangeMaximum = 4.5
histogramView1.BottomAxisLabelFontFile = ''
histogramView1.RightAxisLabelFontFile = ''
histogramView1.TopAxisTitleFontFile = ''
histogramView1.TopAxisLabelFontFile = ''

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [797, 825]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 0
renderView1.CameraPosition = [-0.828678211321353, -4.2788043940965, -8.72449112359904]
renderView1.CameraFocalPoint = [0.0983302158150595, 0.124331318431967, 0.256591003122397]
renderView1.CameraViewUp = [-0.978109710746932, 0.208087169488646, -0.00106001733796991]
renderView1.CameraParallelScale = 3.80651158263537
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [796, 827]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.StereoType = 0
renderView2.CameraPosition = [-0.828678211321353, -4.2788043940965, -8.72449112359904]
renderView2.CameraFocalPoint = [0.0983302158150595, 0.124331318431967, 0.256591003122397]
renderView2.CameraViewUp = [-0.978109710746932, 0.208087169488646, -0.00106001733796991]
renderView2.CameraParallelScale = 3.80651158263537
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [796, 353]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.479937165975571, 1.68303689360619, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [1.81110855295689, 1.60236128386359, 10000.0]
renderView3.CameraFocalPoint = [1.81110855295689, 1.60236128386359, 0.0]
renderView3.CameraParallelScale = 2.76710670073114
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1
renderView3.AxesGrid.XTitle = 'Birth'
renderView3.AxesGrid.YTitle = 'Death'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView3.AxesGrid.ShowGrid = 1
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
tectonicPuzzlevtu = XMLUnstructuredGridReader(FileName=['tectonicPuzzle.vtu'])
tectonicPuzzlevtu.PointArrayStatus = ['Morse field', 'T', 'Viscosity', 'Jacqueline', 'Strain rate', 'P', 'Velocity', 'Divergence', 'Vorticity']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tectonicPuzzlevtu)

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=extractSurface1)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=cleantoGrid1)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=tetrahedralize1)

# create a new 'Threshold'
threshold1 = Threshold(Input=connectivity1)
threshold1.Scalars = ['POINTS', 'RegionId']
threshold1.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'logViscosity'
calculator1.Function = 'log10(Viscosity)'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = 'logViscosity'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [-0.1, 1269.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold2)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.5, 99.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.ThetaResolution = 4
tTKSphereFromPoint1.PhiResolution = 4

# create a new 'Threshold'
pERSISTENT_MINIMA = Threshold(Input=tTKSphereFromPoint1)
pERSISTENT_MINIMA.Scalars = ['POINTS', 'NodeType']

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=calculator1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractSurface6)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'logViscosity'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'logViscosity'
tTKMorseSmaleComplex1.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint2.Radius = 0.1

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)
threshold3.Scalars = ['POINTS', 'CellDimension']
threshold3.ThresholdRange = [2.0, 2.0]

# create a new 'Threshold'
lARGE_MAXIMA_THRESHOLD = Threshold(Input=threshold3)
lARGE_MAXIMA_THRESHOLD.Scalars = ['POINTS', 'ManifoldSize']
lARGE_MAXIMA_THRESHOLD.ThresholdRange = [75.0, 9999.0]

# create a new 'Append Datasets'
pERSISTENT_MINIMA_AND_LARGE_MAXIMA = AppendDatasets(Input=[pERSISTENT_MINIMA, lARGE_MAXIMA_THRESHOLD])

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=tTKTopologicalSimplification1,
    Constraints=pERSISTENT_MINIMA_AND_LARGE_MAXIMA)
tTKTopologicalSimplification2.ScalarField = 'logViscosity'
tTKTopologicalSimplification2.UseInputOffsetField = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=tTKTopologicalSimplification2)
tTKPersistenceDiagram2.ScalarField = 'logViscosity'
tTKPersistenceDiagram2.UseInputOffsetField = 1

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram2)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [-0.1, 101.0]

# create a new 'Threshold'
threshold5 = Threshold(Input=threshold4)
threshold5.Scalars = ['CELLS', 'PairType']
threshold5.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator2 = Calculator(Input=threshold5)
calculator2.ResultArrayName = 'SaddleValue'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
sADDLE_VALUE_THRESHOLD = Threshold(Input=calculator2)
sADDLE_VALUE_THRESHOLD.Scalars = ['POINTS', 'SaddleValue']
sADDLE_VALUE_THRESHOLD.ThresholdRange = [-0.2, 1.75]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=sADDLE_VALUE_THRESHOLD)

# create a new 'Threshold'
lARGE_MAXIMA_LOW_SADDLE = Threshold(Input=tTKSphereFromPoint3)
lARGE_MAXIMA_LOW_SADDLE.Scalars = ['POINTS', 'NodeType']
lARGE_MAXIMA_LOW_SADDLE.ThresholdRange = [4.0, 4.0]

# create a new 'Append Datasets'
lARGE_MAXIMA_LOW_SADDLE_AND_PERSISTENT_MINIMA = AppendDatasets(Input=[pERSISTENT_MINIMA, lARGE_MAXIMA_LOW_SADDLE])

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification3 = TTKTopologicalSimplification(Domain=tTKTopologicalSimplification2,
    Constraints=lARGE_MAXIMA_LOW_SADDLE_AND_PERSISTENT_MINIMA)
tTKTopologicalSimplification3.ScalarField = 'logViscosity'
tTKTopologicalSimplification3.UseInputOffsetField = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=tTKTopologicalSimplification3)
tTKPersistenceDiagram3.ScalarField = 'logViscosity'
tTKPersistenceDiagram3.UseInputOffsetField = 1

# create a new 'Threshold'
threshold7 = Threshold(Input=tTKPersistenceDiagram3)
threshold7.Scalars = ['CELLS', 'PairIdentifier']
threshold7.ThresholdRange = [-0.1, 799.0]

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=threshold7)

# create a new 'Transform'
transform1 = Transform(Input=extractSurface4)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [3.5, 1.0, 1.0]

# create a new 'Tube'
tube3 = Tube(Input=transform1)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=transform1)
tTKSphereFromPoint5.Radius = 0.1

# create a new 'Threshold'
threshold8 = Threshold(Input=tTKPersistenceDiagram3)
threshold8.Scalars = ['CELLS', 'PairIdentifier']
threshold8.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold8)

# create a new 'Transform'
transform2 = Transform(Input=extractSurface3)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Scale = [3.5, 1.0, 1.0]

# create a new 'Tube'
tube2 = Tube(Input=transform2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.05

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification3)
tTKMorseSmaleComplex2.ScalarField = 'logViscosity'
tTKMorseSmaleComplex2.UseInputOffsetField = 1

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold6 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2_1,1))
threshold6.Scalars = ['CELLS', 'CriticalPointIndex']

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold6)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface2)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex2)
tTKSphereFromPoint4.Radius = 0.05

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(Input=OutputPort(tTKMorseSmaleComplex2_2,3))
tTKIdentifierRandomizer1.ScalarField = 'AscendingManifold'

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(Input=tTKIdentifierRandomizer1)

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=cleantoGrid2)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface5)

# ----------------------------------------------------------------
# setup the visualization in view 'histogramView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, histogramView1)

# trace defaults for the display properties.
calculator1Display.SelectInputArray = ['POINTS', 'logViscosity']
calculator1Display.HistogramColor = [0.0, 0.333333333333333, 0.498039215686275]
calculator1Display.CustomBinRanges = [-0.780387709364896, 4.40448904431455]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# find source
tTKMorseSmaleComplex2_3 = FindSource('TTKMorseSmaleComplex2')

# show data from tTKMorseSmaleComplex2_3
tTKMorseSmaleComplex2Display = Show(OutputPort(tTKMorseSmaleComplex2, 2), renderView1)

# trace defaults for the display properties.
tTKMorseSmaleComplex2Display.Representation = 'Surface'
tTKMorseSmaleComplex2Display.ColorArrayName = [None, '']
tTKMorseSmaleComplex2Display.Specular = 1.0
tTKMorseSmaleComplex2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex2Display.ScaleFactor = -2e+298
tTKMorseSmaleComplex2Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex2Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex2Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex2Display.GaussianRadius = -1e+298
tTKMorseSmaleComplex2Display.CustomShader = ''
tTKMorseSmaleComplex2Display.SetScaleArray = [None, '']
tTKMorseSmaleComplex2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.OpacityArray = [None, '']
tTKMorseSmaleComplex2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex2Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex2Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex2Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint4
tTKSphereFromPoint4Display = Show(tTKSphereFromPoint4, renderView1)

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint4Display.Representation = 'Surface'
tTKSphereFromPoint4Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint4Display.LookupTable = cellDimensionLUT
tTKSphereFromPoint4Display.Specular = 1.0
tTKSphereFromPoint4Display.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint4Display.ScaleFactor = 0.539041829109192
tTKSphereFromPoint4Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint4Display.GlyphType = 'Arrow'
tTKSphereFromPoint4Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint4Display.GaussianRadius = 0.269520914554596
tTKSphereFromPoint4Display.CustomShader = ''
tTKSphereFromPoint4Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint4Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint4Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint4Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint4Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 0.448193502426147
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 0.224096751213074
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
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

# show data from generateSurfaceNormals2
generateSurfaceNormals2Display = Show(generateSurfaceNormals2, renderView1)

# get color transfer function/color map for 'logViscosity'
logViscosityLUT = GetColorTransferFunction('logViscosity')
logViscosityLUT.RGBPoints = [-0.780387709364896, 0.0, 0.129412, 0.584314, 1.81205066747483, 0.917647, 0.941176, 0.788235, 4.40448904431455, 0.0, 0.431373, 0.0]
logViscosityLUT.ColorSpace = 'RGB'
logViscosityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
logViscosityLUT.NanColor = [0.0, 0.0, 0.0]
logViscosityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals2Display.Representation = 'Surface'
generateSurfaceNormals2Display.ColorArrayName = ['POINTS', 'logViscosity']
generateSurfaceNormals2Display.LookupTable = logViscosityLUT
generateSurfaceNormals2Display.Opacity = 0.96
generateSurfaceNormals2Display.Specular = 1.0
generateSurfaceNormals2Display.OSPRayScaleArray = 'logViscosity'
generateSurfaceNormals2Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.SelectOrientationVectors = 'Velocity'
generateSurfaceNormals2Display.ScaleFactor = 0.439538097381592
generateSurfaceNormals2Display.SelectScaleArray = 'logViscosity'
generateSurfaceNormals2Display.GlyphType = 'Arrow'
generateSurfaceNormals2Display.GlyphTableIndexArray = 'logViscosity'
generateSurfaceNormals2Display.GaussianRadius = 0.219769048690796
generateSurfaceNormals2Display.CustomShader = ''
generateSurfaceNormals2Display.SetScaleArray = ['POINTS', 'logViscosity']
generateSurfaceNormals2Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.OpacityArray = ['POINTS', 'logViscosity']
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
tube1Display_1 = Show(tube1, renderView2)

# trace defaults for the display properties.
tube1Display_1.Representation = 'Surface'
tube1Display_1.ColorArrayName = [None, '']
tube1Display_1.Specular = 1.0
tube1Display_1.OSPRayScaleArray = 'CellDimension'
tube1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display_1.SelectOrientationVectors = 'CellDimension'
tube1Display_1.ScaleFactor = 0.441905641555786
tube1Display_1.SelectScaleArray = 'CellDimension'
tube1Display_1.GlyphType = 'Arrow'
tube1Display_1.GlyphTableIndexArray = 'CellDimension'
tube1Display_1.GaussianRadius = 0.220952820777893
tube1Display_1.CustomShader = ''
tube1Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display_1.OpacityArray = ['POINTS', 'CellDimension']
tube1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube1Display_1.SelectionCellLabelFontFile = ''
tube1Display_1.SelectionPointLabelFontFile = ''
tube1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display_1.DataAxesGrid.XTitleFontFile = ''
tube1Display_1.DataAxesGrid.YTitleFontFile = ''
tube1Display_1.DataAxesGrid.ZTitleFontFile = ''
tube1Display_1.DataAxesGrid.XLabelFontFile = ''
tube1Display_1.DataAxesGrid.YLabelFontFile = ''
tube1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView2)

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.RGBPoints = [0.0, 0.278431372549, 0.278431372549, 0.858823529412, 6.435, 0.0, 0.0, 0.360784313725, 12.825, 0.0, 1.0, 1.0, 19.305, 0.0, 0.501960784314, 0.0, 25.695, 1.0, 1.0, 0.0, 32.13, 1.0, 0.380392156863, 0.0, 38.565, 0.419607843137, 0.0, 0.0, 45.0, 0.878431372549, 0.301960784314, 0.301960784314]
ascendingManifoldLUT.ColorSpace = 'RGB'
ascendingManifoldLUT.AboveRangeColor = [1.0, 1.0, 1.0]
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
generateSurfaceNormals1Display.LookupTable = ascendingManifoldLUT
generateSurfaceNormals1Display.Opacity = 0.925
generateSurfaceNormals1Display.Specular = 1.0
generateSurfaceNormals1Display.OSPRayScaleArray = 'logViscosity'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'Velocity'
generateSurfaceNormals1Display.ScaleFactor = 0.439538097381592
generateSurfaceNormals1Display.SelectScaleArray = 'logViscosity'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'logViscosity'
generateSurfaceNormals1Display.GaussianRadius = 0.219769048690796
generateSurfaceNormals1Display.CustomShader = ''
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'logViscosity']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'logViscosity']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals1Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals1Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals1Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tube3
tube3Display = Show(tube3, renderView3)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'Coordinates'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Coordinates'
tube3Display.ScaleFactor = 1.02842507362366
tube3Display.SelectScaleArray = 'Coordinates'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'Coordinates'
tube3Display.GaussianRadius = 0.514212536811829
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', 'NodeType']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'NodeType']
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

# show data from tTKSphereFromPoint5
tTKSphereFromPoint5Display = Show(tTKSphereFromPoint5, renderView3)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')
nodeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 2.0, 0.917647, 0.941176, 0.788235, 4.0, 0.0, 0.431373, 0.0]
nodeTypeLUT.ColorSpace = 'RGB'
nodeTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
nodeTypeLUT.NanColor = [0.0, 0.0, 0.0]
nodeTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint5Display.Representation = 'Surface'
tTKSphereFromPoint5Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint5Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint5Display.Specular = 1.0
tTKSphereFromPoint5Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint5Display.ScaleFactor = 1.0481232881546
tTKSphereFromPoint5Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint5Display.GlyphType = 'Arrow'
tTKSphereFromPoint5Display.GlyphTableIndexArray = 'NodeType'
tTKSphereFromPoint5Display.GaussianRadius = 0.524061644077301
tTKSphereFromPoint5Display.CustomShader = ''
tTKSphereFromPoint5Display.SetScaleArray = ['POINTS', 'NodeType']
tTKSphereFromPoint5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.OpacityArray = ['POINTS', 'NodeType']
tTKSphereFromPoint5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint5Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint5Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint5Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint5Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display = Show(tube2, renderView3)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'Coordinates'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Coordinates'
tube2Display.ScaleFactor = 1.01036033630371
tube2Display.SelectScaleArray = 'Coordinates'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'Coordinates'
tube2Display.GaussianRadius = 0.505180168151856
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

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [0.0, 0.0, 0.5, 0.0, 45.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'logViscosity'
logViscosityPWF = GetOpacityTransferFunction('logViscosity')
logViscosityPWF.Points = [-0.780387709364896, 0.0, 0.5, 0.0, 4.40448904431455, 1.0, 0.5, 0.0]
logViscosityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
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
tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))
tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKTopologicalSimplification3.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification3, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification3.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification3)))
tTKPersistenceDiagram3.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram3, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram3.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram3)))
tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))
tTKMorseSmaleComplex2.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex2, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex2.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex2)))
tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))
tTKIdentifierRandomizer1.DebugLevel = int(debugLevel)
if tTKIdentifierRandomizer1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIdentifierRandomizer1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIdentifierRandomizer1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIdentifierRandomizer1, i)))
else:
	SaveData(outputDirectory + 'tTKIdentifierRandomizer1.vtu',
		CleantoGrid(OutputPort(tTKIdentifierRandomizer1)))
