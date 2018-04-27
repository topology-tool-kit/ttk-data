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
renderView1.ViewSize = [797, 590]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [123.0, 61.5, -76.5133018493652]
renderView1.StereoType = 0
renderView1.CameraPosition = [123.475600190615, 55.5003489433595, 457.099681146434]
renderView1.CameraFocalPoint = [123.475600190615, 55.5003489433595, -76.5133018493652]
renderView1.CameraParallelScale = 94.3304437629127
renderView1.CameraParallelProjection = 1
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitle = 'Birth'
renderView1.AxesGrid.YTitle = 'Death'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView1.AxesGrid.ShowGrid = 1
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [796, 590]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [123.0, 61.5, 76.5133018493652]
renderView2.StereoType = 0
renderView2.CameraPosition = [-36.0532170929598, -114.091382108486, 263.41136713235]
renderView2.CameraFocalPoint = [111.291080216305, 56.344817398489, 63.4888918407025]
renderView2.CameraViewUp = [0.463910925091856, 0.475619833689914, 0.747377031612022]
renderView2.CameraParallelScale = 138.109202713281
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitle = 'Birth'
renderView2.AxesGrid.YTitle = 'Death'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView2.AxesGrid.ShowGrid = 1
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [796, 590]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [305.703536987305, 306.053207397461, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [305.098802636758, 304.037426228973, 10000.0]
renderView3.CameraFocalPoint = [305.098802636758, 304.037426228973, 0.0]
renderView3.CameraParallelScale = 59.4655444704077
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

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [797, 590]
renderView5.InteractionMode = '2D'
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [123.0, 61.5, -76.5133018493652]
renderView5.StereoType = 0
renderView5.CameraPosition = [123.475600190615, 55.5003489433595, 457.099681146434]
renderView5.CameraFocalPoint = [123.475600190615, 55.5003489433595, -76.5133018493652]
renderView5.CameraParallelScale = 94.3304437629127
renderView5.CameraParallelProjection = 1
renderView5.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView5.AxesGrid.XTitle = 'Birth'
renderView5.AxesGrid.YTitle = 'Death'
renderView5.AxesGrid.XTitleFontFile = ''
renderView5.AxesGrid.YTitleFontFile = ''
renderView5.AxesGrid.ZTitleFontFile = ''
renderView5.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView5.AxesGrid.ShowGrid = 1
renderView5.AxesGrid.XLabelFontFile = ''
renderView5.AxesGrid.YLabelFontFile = ''
renderView5.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PNG Series Reader'
tributepng = PNGSeriesReader(FileNames=['tribute.png'])

# create a new 'Calculator'
calculator1 = Calculator(Input=tributepng)
calculator1.ResultArrayName = 'originalData'
calculator1.Function = 'sqrt(PNGImage_X*PNGImage_X+PNGImage_Y*PNGImage_Y)'

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=calculator1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'originalData'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram1)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-1.0, -0.1]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 3560.0]

# create a new 'Threshold'
minimumPairs = Threshold(Input=threshold1)
minimumPairs.Scalars = ['CELLS', 'PairType']
minimumPairs.ThresholdRange = [-1.0, 0.0]

# create a new 'Threshold'
maximumPairs = Threshold(Input=threshold1)
maximumPairs.Scalars = ['CELLS', 'PairType']
maximumPairs.ThresholdRange = [1.0, 1.0]

# create a new 'Calculator'
calculator2 = Calculator(Input=maximumPairs)
calculator2.ResultArrayName = 'Birth'
calculator2.Function = 'coordsX'

# create a new 'Threshold'
birthThreshold = Threshold(Input=calculator2)
birthThreshold.Scalars = ['POINTS', 'Birth']
birthThreshold.ThresholdRange = [257.390747070312, 297.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[minimumPairs, birthThreshold])

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=appendDatasets1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [8.5, 102.106426713382]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint2.Radius = 1.0

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'originalData'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=tTKTopologicalSimplification1)
warpByScalar1.Scalars = ['POINTS', 'originalData']
warpByScalar1.ScaleFactor = 0.25

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=warpByScalar1)

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tetrahedralize2)
tTKMorseSmaleComplex2.ScalarField = 'originalData'
tTKMorseSmaleComplex2.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex2)
tTKSphereFromPoint4.Radius = 1.0

# create a new 'Calculator'
calculator5 = Calculator(Input=tTKMorseSmaleComplex2)
calculator5.CoordinateResults = 1
calculator5.ResultArrayName = 'newCoords'
calculator5.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=calculator5)
tTKSphereFromPoint3.Radius = 1.0

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer2 = TTKIdentifierRandomizer(OutputPort(tTKMorseSmaleComplex2,3))
tTKIdentifierRandomizer2.ScalarField = 'AscendingManifold'

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKIdentifierRandomizer2)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface1)

# create a new 'Calculator'
calculator3 = Calculator(Input=tTKIdentifierRandomizer2)
calculator3.CoordinateResults = 1
calculator3.ResultArrayName = 'newCoords'
calculator3.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2,1))
threshold4.Scalars = ['CELLS', 'CriticalPointIndex']

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=threshold4)

# create a new 'Clip'
clip1 = Clip(Input=extractSurface4)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'CellDimension']
clip1.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [123.0, 66.0, 87.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Calculator'
calculator4 = Calculator(Input=clip1)
calculator4.CoordinateResults = 1
calculator4.ResultArrayName = 'newCoords'
calculator4.Function = 'iHat*coordsX+coordsY*jHat+0*kHat'

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=calculator4)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface5)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.75

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=clip1)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface6)
tube4.Scalars = ['POINTS', 'CellDimension']
tube4.Vectors = [None, '']
tube4.Radius = 0.75

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.5

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold3)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.75

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification1
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView1)

# get color transfer function/color map for 'originalData'
originalDataLUT = GetColorTransferFunction('originalData')
originalDataLUT.RGBPoints = [255.0, 0.0, 0.129412, 0.584314, 306.053213356691, 0.917647, 0.941176, 0.788235, 357.106426713382, 0.0, 0.431373, 0.0]
originalDataLUT.ColorSpace = 'RGB'
originalDataLUT.AboveRangeColor = [1.0, 1.0, 1.0]
originalDataLUT.NanColor = [0.0, 0.0, 0.0]
originalDataLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'originalData'
originalDataPWF = GetOpacityTransferFunction('originalData')
originalDataPWF.Points = [255.0, 0.0, 0.5, 0.0, 357.106426713382, 1.0, 0.5, 0.0]
originalDataPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Surface'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', 'originalData']
tTKTopologicalSimplification1Display.LookupTable = originalDataLUT
tTKTopologicalSimplification1Display.Specular = 1.0
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'originalData'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification1Display.ScaleFactor = 24.6
tTKTopologicalSimplification1Display.SelectScaleArray = 'originalData'
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.GlyphTableIndexArray = 'originalData'
tTKTopologicalSimplification1Display.GaussianRadius = 12.3
tTKTopologicalSimplification1Display.CustomShader = ''
tTKTopologicalSimplification1Display.SetScaleArray = ['POINTS', 'originalData']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = ['POINTS', 'originalData']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification1Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification1Display.ScalarOpacityFunction = originalDataPWF
tTKTopologicalSimplification1Display.ScalarOpacityUnitDistance = 7.00540705728485

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTopologicalSimplification1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from calculator4
calculator4Display = Show(calculator4, renderView1)

# trace defaults for the display properties.
calculator4Display.Representation = 'Surface'
calculator4Display.ColorArrayName = [None, '']
calculator4Display.DiffuseColor = [1.0, 0.0, 0.0]
calculator4Display.Specular = 1.0
calculator4Display.OSPRayScaleArray = 'CellDimension'
calculator4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator4Display.SelectOrientationVectors = 'CellDimension'
calculator4Display.ScaleFactor = 24.6
calculator4Display.SelectScaleArray = 'CellDimension'
calculator4Display.GlyphType = 'Arrow'
calculator4Display.GlyphTableIndexArray = 'CellDimension'
calculator4Display.GaussianRadius = 12.3
calculator4Display.CustomShader = ''
calculator4Display.SetScaleArray = ['POINTS', 'CellDimension']
calculator4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator4Display.OpacityArray = ['POINTS', 'CellDimension']
calculator4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator4Display.SelectionCellLabelFontFile = ''
calculator4Display.SelectionPointLabelFontFile = ''
calculator4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator4Display.DataAxesGrid.XTitleFontFile = ''
calculator4Display.DataAxesGrid.YTitleFontFile = ''
calculator4Display.DataAxesGrid.ZTitleFontFile = ''
calculator4Display.DataAxesGrid.XLabelFontFile = ''
calculator4Display.DataAxesGrid.YLabelFontFile = ''
calculator4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator4Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator4Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator4Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView2)

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.RGBPoints = [-1.0, 0.278431372549, 0.278431372549, 0.858823529412, 20.021, 0.0, 0.0, 0.360784313725, 40.895, 0.0, 1.0, 1.0, 62.063, 0.0, 0.501960784314, 0.0, 82.937, 1.0, 1.0, 0.0, 103.958, 1.0, 0.380392156863, 0.0, 124.979, 0.419607843137, 0.0, 0.0, 146.0, 0.878431372549, 0.301960784314, 0.301960784314]
ascendingManifoldLUT.ColorSpace = 'RGB'
ascendingManifoldLUT.AboveRangeColor = [1.0, 1.0, 1.0]
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
generateSurfaceNormals1Display.LookupTable = ascendingManifoldLUT
generateSurfaceNormals1Display.Specular = 1.0
generateSurfaceNormals1Display.OSPRayScaleArray = 'originalData'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'AscendingManifold'
generateSurfaceNormals1Display.ScaleFactor = 24.6
generateSurfaceNormals1Display.SelectScaleArray = 'originalData'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'originalData'
generateSurfaceNormals1Display.GaussianRadius = 12.3
generateSurfaceNormals1Display.CustomShader = ''
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'originalData']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'originalData']
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

# show data from tTKSphereFromPoint4
tTKSphereFromPoint4Display = Show(tTKSphereFromPoint4, renderView2)

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
tTKSphereFromPoint4Display.ScaleFactor = 24.799316650629
tTKSphereFromPoint4Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint4Display.GlyphType = 'Arrow'
tTKSphereFromPoint4Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint4Display.GaussianRadius = 12.3996583253145
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

# show data from tube4
tube4Display = Show(tube4, renderView2)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = [None, '']
tube4Display.Specular = 1.0
tube4Display.OSPRayScaleArray = 'CellDimension'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'CellDimension'
tube4Display.ScaleFactor = 25.0387038469315
tube4Display.SelectScaleArray = 'CellDimension'
tube4Display.GlyphType = 'Arrow'
tube4Display.GlyphTableIndexArray = 'CellDimension'
tube4Display.GaussianRadius = 12.5193519234657
tube4Display.CustomShader = ''
tube4Display.SetScaleArray = ['POINTS', 'CellDimension']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'CellDimension']
tube4Display.OpacityTransferFunction = 'PiecewiseFunction'
tube4Display.DataAxesGrid = 'GridAxesRepresentation'
tube4Display.SelectionCellLabelFontFile = ''
tube4Display.SelectionPointLabelFontFile = ''
tube4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube4Display.DataAxesGrid.XTitleFontFile = ''
tube4Display.DataAxesGrid.YTitleFontFile = ''
tube4Display.DataAxesGrid.ZTitleFontFile = ''
tube4Display.DataAxesGrid.XLabelFontFile = ''
tube4Display.DataAxesGrid.YLabelFontFile = ''
tube4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube4Display.PolarAxes.PolarAxisTitleFontFile = ''
tube4Display.PolarAxes.PolarAxisLabelFontFile = ''
tube4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tTKPersistenceDiagram1
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView3)

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'
tTKPersistenceDiagram1Display.ColorArrayName = [None, '']
tTKPersistenceDiagram1Display.Opacity = 0.3
tTKPersistenceDiagram1Display.Specular = 1.0
tTKPersistenceDiagram1Display.OSPRayScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.SelectOrientationVectors = 'Coordinates'
tTKPersistenceDiagram1Display.ScaleFactor = 10.2106414794922
tTKPersistenceDiagram1Display.SelectScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.GlyphType = 'Arrow'
tTKPersistenceDiagram1Display.GlyphTableIndexArray = 'Coordinates'
tTKPersistenceDiagram1Display.GaussianRadius = 5.10532073974609
tTKPersistenceDiagram1Display.CustomShader = ''
tTKPersistenceDiagram1Display.SetScaleArray = ['POINTS', 'NodeType']
tTKPersistenceDiagram1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.OpacityArray = ['POINTS', 'NodeType']
tTKPersistenceDiagram1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistenceDiagram1Display.SelectionCellLabelFontFile = ''
tTKPersistenceDiagram1Display.SelectionPointLabelFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistenceDiagram1Display.ScalarOpacityUnitDistance = 9.42286119973464

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistenceDiagram1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistenceDiagram1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistenceDiagram1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKPersistenceDiagram1Display.DataAxesGrid.XTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.YTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.ZTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.XLabelFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.YLabelFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKPersistenceDiagram1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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
tube2Display.ScaleFactor = 10.2649063110352
tube2Display.SelectScaleArray = 'Coordinates'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'Coordinates'
tube2Display.GaussianRadius = 5.13245315551758
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

# show data from tTKSphereFromPoint2
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView3)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')
nodeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 2.0, 0.917647, 0.941176, 0.788235, 4.0, 0.0, 0.431373, 0.0]
nodeTypeLUT.ColorSpace = 'RGB'
nodeTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
nodeTypeLUT.NanColor = [0.0, 0.0, 0.0]
nodeTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint2Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint2Display.ScaleFactor = 10.4099578857422
tTKSphereFromPoint2Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GlyphTableIndexArray = 'NodeType'
tTKSphereFromPoint2Display.GaussianRadius = 5.20497894287109
tTKSphereFromPoint2Display.CustomShader = ''
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'NodeType']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'NodeType']
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
tube3Display = Show(tube3, renderView3)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', '']
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'Coordinates'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Coordinates'
tube3Display.ScaleFactor = 10.2106414794922
tube3Display.SelectScaleArray = 'Coordinates'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'Coordinates'
tube3Display.GaussianRadius = 5.10532073974609
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView5)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.LookupTable = cellDimensionLUT
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint3Display.ScaleFactor = 24.799316650629
tTKSphereFromPoint3Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint3Display.GaussianRadius = 12.3996583253145
tTKSphereFromPoint3Display.CustomShader = ''
tTKSphereFromPoint3Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint3Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint3Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from calculator3
calculator3Display = Show(calculator3, renderView5)

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [-1.0, 0.0, 0.5, 0.0, 146.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'AscendingManifold']
calculator3Display.LookupTable = ascendingManifoldLUT
calculator3Display.Specular = 1.0
calculator3Display.OSPRayScaleArray = 'originalData'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'AscendingManifold'
calculator3Display.ScaleFactor = 24.6
calculator3Display.SelectScaleArray = 'originalData'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.GlyphTableIndexArray = 'originalData'
calculator3Display.GaussianRadius = 12.3
calculator3Display.CustomShader = ''
calculator3Display.SetScaleArray = ['POINTS', 'originalData']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'originalData']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator3Display.SelectionCellLabelFontFile = ''
calculator3Display.SelectionPointLabelFontFile = ''
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityFunction = ascendingManifoldPWF
calculator3Display.ScalarOpacityUnitDistance = 7.00540705728485

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator3Display.DataAxesGrid.XTitleFontFile = ''
calculator3Display.DataAxesGrid.YTitleFontFile = ''
calculator3Display.DataAxesGrid.ZTitleFontFile = ''
calculator3Display.DataAxesGrid.XLabelFontFile = ''
calculator3Display.DataAxesGrid.YLabelFontFile = ''
calculator3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator3Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator3Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator3Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from calculator5
calculator5Display = Show(calculator5, renderView5)

# trace defaults for the display properties.
calculator5Display.Representation = 'Surface'
calculator5Display.ColorArrayName = [None, '']
calculator5Display.Specular = 1.0
calculator5Display.OSPRayScaleArray = 'CellDimension'
calculator5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator5Display.SelectOrientationVectors = 'CellDimension'
calculator5Display.ScaleFactor = 24.6
calculator5Display.SelectScaleArray = 'CellDimension'
calculator5Display.GlyphType = 'Arrow'
calculator5Display.GlyphTableIndexArray = 'CellDimension'
calculator5Display.GaussianRadius = 12.3
calculator5Display.CustomShader = ''
calculator5Display.SetScaleArray = ['POINTS', 'CellDimension']
calculator5Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator5Display.OpacityArray = ['POINTS', 'CellDimension']
calculator5Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator5Display.SelectionCellLabelFontFile = ''
calculator5Display.SelectionPointLabelFontFile = ''
calculator5Display.PolarAxes = 'PolarAxesRepresentation'
calculator5Display.ScalarOpacityUnitDistance = 271.13096466468

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator5Display.DataAxesGrid.XTitleFontFile = ''
calculator5Display.DataAxesGrid.YTitleFontFile = ''
calculator5Display.DataAxesGrid.ZTitleFontFile = ''
calculator5Display.DataAxesGrid.XLabelFontFile = ''
calculator5Display.DataAxesGrid.YLabelFontFile = ''
calculator5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator5Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator5Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator5Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView5)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 24.9327156364918
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 12.4663578182459
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

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
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
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKIdentifierRandomizer2.DebugLevel = int(debugLevel)
if tTKIdentifierRandomizer2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIdentifierRandomizer2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIdentifierRandomizer2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIdentifierRandomizer2, i)))
else:
	SaveData(outputDirectory + 'tTKIdentifierRandomizer2.vtu',
		CleantoGrid(OutputPort(tTKIdentifierRandomizer2)))
