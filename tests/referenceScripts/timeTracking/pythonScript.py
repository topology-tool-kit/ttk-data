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
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1437, 1216]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.OrientationAxesOutlineColor = [0.501960784313725, 0.490196078431372, 0.490196078431372]
renderView1.CenterOfRotation = [3.53203153610229, 0.0, 3.72175534255803]
renderView1.StereoType = 0
renderView1.CameraPosition = [-4.1810633457895, -11.596373367697, 12.2437062937574]
renderView1.CameraFocalPoint = [3.97527186280502, 0.939438262790558, 2.95052388527141]
renderView1.CameraViewUp = [0.225676576530991, 0.481143284745888, 0.847095757485061]
renderView1.CameraParallelScale = 5.51426197343358
renderView1.Background = [0.188235294117647, 0.184313725490196, 0.184313725490196]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1
renderView1.AxesGrid.XTitle = 'Birth'
renderView1.AxesGrid.YTitle = 'Death'
renderView1.AxesGrid.ZTitle = ''
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView1.AxesGrid.ShowEdges = 0
renderView1.AxesGrid.ShowTicks = 0
renderView1.AxesGrid.AxesToLabel = 0
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
timeTrackingvti = XMLImageDataReader(FileName=['timeTracking.vti'])
timeTrackingvti.CellArrayStatus = []
timeTrackingvti.PointArrayStatus = ['000', '002', '004', '006', '008', '010', '012', '014', '016', '018', '020', '022', '024', '026', '028', '030', '032', '034', '036', '038', '040', '042', '044', '046', '048', '050', '052', '054', '056', '058', '060', '062', '064', '066', '068', '070', '072', '074', '076', '078', '080', '082', '084', '086', '088', '090', '092', '094', '096', '098', '100', '102', '104', '106', '108', '110', '112', '114', '116', '118']

# create a new 'TTK PointDataSelector'
tTKPointDataSelector2 = TTKPointDataSelector(Input=timeTrackingvti)
tTKPointDataSelector2.ScalarFields = ['000']
tTKPointDataSelector2.Renameselectedfield = 1

# create a new 'TTK TrackingFromFields'
tTKTrackingFromFields1 = TTKTrackingFromFields(Input=timeTrackingvti)
tTKTrackingFromFields1.ForceZtranslation = 1
tTKTrackingFromFields1.ZTranslation = 0.125

# create a new 'Threshold'
latefeatures = Threshold(Input=tTKTrackingFromFields1)
latefeatures.Scalars = ['POINTS', 'TimeStep']
latefeatures.ThresholdRange = [55.0, 58.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKTrackingFromFields1)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'ConnectedComponentId']
tube2.Vectors = [None, '']
tube2.Radius = 0.025

# create a new 'Transform'
transform2 = Transform(Input=timeTrackingvti)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [0.0, 0.0, 3.5]

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=transform2)

# create a new 'TTK PointDataSelector'
tTKPointDataSelector3 = TTKPointDataSelector(Input=tetrahedralize2)
tTKPointDataSelector3.ScalarFields = ['056']
tTKPointDataSelector3.Renameselectedfield = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=tTKPointDataSelector3)
tTKPersistenceDiagram2.ScalarField = 'SelectedField'
tTKPersistenceDiagram2.InputOffsetField = 'SelectedField'
tTKPersistenceDiagram2.EmbedinDomain = 1

# create a new 'Transform'
transform1 = Transform(Input=timeTrackingvti)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.0, 0.0, 7.375]

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=transform1)

# create a new 'TTK PointDataSelector'
tTKPointDataSelector1 = TTKPointDataSelector(Input=tetrahedralize1)
tTKPointDataSelector1.ScalarFields = ['118']
tTKPointDataSelector1.Renameselectedfield = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKPointDataSelector1)
tTKPersistenceDiagram1.ScalarField = 'SelectedField'
tTKPersistenceDiagram1.InputOffsetField = 'SelectedField'
tTKPersistenceDiagram1.EmbedinDomain = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'Persistence']
threshold1.ThresholdRange = [0.5, 44.9597725588668]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=threshold1)
tTKSphereFromPoint1.Radius = 0.075

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKSphereFromPoint1)
threshold2.Scalars = ['POINTS', 'CriticalType']

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram2)
threshold4.Scalars = ['CELLS', 'Persistence']
threshold4.ThresholdRange = [0.5, 44.5332099569223]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=threshold4)
tTKSphereFromPoint2.Radius = 0.075

# create a new 'Threshold'
threshold5 = Threshold(Input=tTKSphereFromPoint2)
threshold5.Scalars = ['POINTS', 'CriticalType']

# create a new 'Threshold'
threshold6 = Threshold(Input=tTKSphereFromPoint2)
threshold6.Scalars = ['POINTS', 'CriticalType']
threshold6.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint1)
threshold3.Scalars = ['POINTS', 'CriticalType']
threshold3.ThresholdRange = [3.0, 3.0]

# create a new 'Threshold'
earlyfeatures = Threshold(Input=tTKTrackingFromFields1)
earlyfeatures.Scalars = ['POINTS', 'TimeStep']
earlyfeatures.ThresholdRange = [0.0, 55.0]

# create a new 'Threshold'
longtrajectories = Threshold(Input=earlyfeatures)
longtrajectories.Scalars = ['CELLS', 'ComponentLength']
longtrajectories.ThresholdRange = [5.0, 60.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[longtrajectories, latefeatures])

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=appendDatasets1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'ConnectedComponentId']
tube1.Vectors = [None, '']
tube1.Radius = 0.025

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKPointDataSelector1
tTKPointDataSelector1Display = Show(tTKPointDataSelector1, renderView1)

# get color transfer function/color map for 'SelectedField'
selectedFieldLUT = GetColorTransferFunction('SelectedField')
selectedFieldLUT.RGBPoints = [-22.0015973664814, 0.0, 0.129412, 0.584314, -4.49752408306022, 0.0, 0.129412, 0.584314, 0.481469098741833, 0.917647, 0.941176, 0.788235, 4.50374912943535, 0.0, 0.431373, 0.0, 22.9645355639652, 0.0, 0.431373, 0.0]
selectedFieldLUT.ColorSpace = 'RGB'
selectedFieldLUT.NanColor = [0.0, 0.0, 0.0]
selectedFieldLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SelectedField'
selectedFieldPWF = GetOpacityTransferFunction('SelectedField')
selectedFieldPWF.Points = [-22.0015973664814, 0.0, 0.5, 0.0, 22.9645355639652, 1.0, 0.5, 0.0]
selectedFieldPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKPointDataSelector1Display.Representation = 'Surface'
tTKPointDataSelector1Display.AmbientColor = [0.501960784313725, 0.490196078431372, 0.490196078431372]
tTKPointDataSelector1Display.ColorArrayName = ['POINTS', 'SelectedField']
tTKPointDataSelector1Display.LookupTable = selectedFieldLUT
tTKPointDataSelector1Display.Specular = 1.0
tTKPointDataSelector1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKPointDataSelector1Display.OSPRayScaleArray = 'SelectedField'
tTKPointDataSelector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPointDataSelector1Display.SelectOrientationVectors = 'None'
tTKPointDataSelector1Display.ScaleFactor = 0.8
tTKPointDataSelector1Display.SelectScaleArray = 'None'
tTKPointDataSelector1Display.GlyphType = 'Arrow'
tTKPointDataSelector1Display.GlyphTableIndexArray = 'None'
tTKPointDataSelector1Display.GaussianRadius = 0.04
tTKPointDataSelector1Display.SetScaleArray = ['POINTS', 'SelectedField']
tTKPointDataSelector1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector1Display.OpacityArray = ['POINTS', 'SelectedField']
tTKPointDataSelector1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPointDataSelector1Display.SelectionCellLabelFontFile = ''
tTKPointDataSelector1Display.SelectionPointLabelFontFile = ''
tTKPointDataSelector1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPointDataSelector1Display.ScalarOpacityFunction = selectedFieldPWF
tTKPointDataSelector1Display.ScalarOpacityUnitDistance = 0.152314415769319

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPointDataSelector1Display.ScaleTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, 22.9581751923854, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPointDataSelector1Display.OpacityTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, 22.9581751923854, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKPointDataSelector1Display.DataAxesGrid.XTitleFontFile = ''
tTKPointDataSelector1Display.DataAxesGrid.YTitleFontFile = ''
tTKPointDataSelector1Display.DataAxesGrid.ZTitleFontFile = ''
tTKPointDataSelector1Display.DataAxesGrid.XLabelFontFile = ''
tTKPointDataSelector1Display.DataAxesGrid.YLabelFontFile = ''
tTKPointDataSelector1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKPointDataSelector1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKPointDataSelector1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKPointDataSelector1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKPointDataSelector1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKPointDataSelector2
tTKPointDataSelector2Display = Show(tTKPointDataSelector2, renderView1)

# trace defaults for the display properties.
tTKPointDataSelector2Display.Representation = 'Slice'
tTKPointDataSelector2Display.ColorArrayName = ['POINTS', 'SelectedField']
tTKPointDataSelector2Display.LookupTable = selectedFieldLUT
tTKPointDataSelector2Display.OSPRayScaleArray = 'SelectedField'
tTKPointDataSelector2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPointDataSelector2Display.SelectOrientationVectors = 'None'
tTKPointDataSelector2Display.ScaleFactor = 0.7999999999873
tTKPointDataSelector2Display.SelectScaleArray = 'None'
tTKPointDataSelector2Display.GlyphType = 'Arrow'
tTKPointDataSelector2Display.GlyphTableIndexArray = 'None'
tTKPointDataSelector2Display.GaussianRadius = 0.039999999999365
tTKPointDataSelector2Display.SetScaleArray = ['POINTS', 'SelectedField']
tTKPointDataSelector2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector2Display.OpacityArray = ['POINTS', 'SelectedField']
tTKPointDataSelector2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPointDataSelector2Display.SelectionCellLabelFontFile = ''
tTKPointDataSelector2Display.SelectionPointLabelFontFile = ''
tTKPointDataSelector2Display.PolarAxes = 'PolarAxesRepresentation'
tTKPointDataSelector2Display.ScalarOpacityUnitDistance = 0.191904138627202
tTKPointDataSelector2Display.ScalarOpacityFunction = selectedFieldPWF
tTKPointDataSelector2Display.Shade = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPointDataSelector2Display.ScaleTransferFunction.Points = [-11.2869258583145, 0.0, 0.5, 0.0, 11.1315880724948, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPointDataSelector2Display.OpacityTransferFunction.Points = [-11.2869258583145, 0.0, 0.5, 0.0, 11.1315880724948, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKPointDataSelector2Display.DataAxesGrid.XTitleFontFile = ''
tTKPointDataSelector2Display.DataAxesGrid.YTitleFontFile = ''
tTKPointDataSelector2Display.DataAxesGrid.ZTitleFontFile = ''
tTKPointDataSelector2Display.DataAxesGrid.XLabelFontFile = ''
tTKPointDataSelector2Display.DataAxesGrid.YLabelFontFile = ''
tTKPointDataSelector2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKPointDataSelector2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKPointDataSelector2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKPointDataSelector2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKPointDataSelector2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold2
threshold2Display = Show(threshold2, renderView1)

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.500244140625, 0.917647, 0.941176, 0.788235, 3.00048828125, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.00048828125, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', 'CriticalType']
threshold2Display.LookupTable = criticalTypeLUT
threshold2Display.Specular = 1.0
threshold2Display.OSPRayScaleArray = 'Birth'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'Birth'
threshold2Display.ScaleFactor = 0.738403728231788
threshold2Display.SelectScaleArray = 'Birth'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'Birth'
threshold2Display.GaussianRadius = 0.0369201864115894
threshold2Display.SetScaleArray = ['POINTS', 'Birth']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'Birth']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.SelectionCellLabelFontFile = ''
threshold2Display.SelectionPointLabelFontFile = ''
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = criticalTypePWF
threshold2Display.ScalarOpacityUnitDistance = 0.341949836205129

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, -2.64326977421603, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, -2.64326977421603, 1.0, 0.5, 0.0]

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

# show data from threshold3
threshold3Display = Show(threshold3, renderView1)

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['POINTS', 'CriticalType']
threshold3Display.LookupTable = criticalTypeLUT
threshold3Display.Specular = 1.0
threshold3Display.OSPRayScaleArray = 'Birth'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'Birth'
threshold3Display.ScaleFactor = 0.75869748853147
threshold3Display.SelectScaleArray = 'Birth'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'Birth'
threshold3Display.GaussianRadius = 0.0379348744265735
threshold3Display.SetScaleArray = ['POINTS', 'Birth']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'Birth']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.SelectionCellLabelFontFile = ''
threshold3Display.SelectionPointLabelFontFile = ''
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = criticalTypePWF
threshold3Display.ScalarOpacityUnitDistance = 0.343375032452256

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, 16.622253335393, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [-22.0015973664814, 0.0, 0.5, 0.0, 16.622253335393, 1.0, 0.5, 0.0]

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

# show data from tTKPointDataSelector3
tTKPointDataSelector3Display = Show(tTKPointDataSelector3, renderView1)

# trace defaults for the display properties.
tTKPointDataSelector3Display.Representation = 'Surface'
tTKPointDataSelector3Display.ColorArrayName = ['POINTS', 'SelectedField']
tTKPointDataSelector3Display.LookupTable = selectedFieldLUT
tTKPointDataSelector3Display.Specular = 1.0
tTKPointDataSelector3Display.OSPRayScaleArray = 'SelectedField'
tTKPointDataSelector3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPointDataSelector3Display.SelectOrientationVectors = 'None'
tTKPointDataSelector3Display.ScaleFactor = 0.8
tTKPointDataSelector3Display.SelectScaleArray = 'None'
tTKPointDataSelector3Display.GlyphType = 'Arrow'
tTKPointDataSelector3Display.GlyphTableIndexArray = 'None'
tTKPointDataSelector3Display.GaussianRadius = 0.04
tTKPointDataSelector3Display.SetScaleArray = ['POINTS', 'SelectedField']
tTKPointDataSelector3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector3Display.OpacityArray = ['POINTS', 'SelectedField']
tTKPointDataSelector3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPointDataSelector3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPointDataSelector3Display.SelectionCellLabelFontFile = ''
tTKPointDataSelector3Display.SelectionPointLabelFontFile = ''
tTKPointDataSelector3Display.PolarAxes = 'PolarAxesRepresentation'
tTKPointDataSelector3Display.ScalarOpacityFunction = selectedFieldPWF
tTKPointDataSelector3Display.ScalarOpacityUnitDistance = 0.152314415769319

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPointDataSelector3Display.ScaleTransferFunction.Points = [-21.6316016097649, 0.0, 0.5, 0.0, 22.9645355639652, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPointDataSelector3Display.OpacityTransferFunction.Points = [-21.6316016097649, 0.0, 0.5, 0.0, 22.9645355639652, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKPointDataSelector3Display.DataAxesGrid.XTitleFontFile = ''
tTKPointDataSelector3Display.DataAxesGrid.YTitleFontFile = ''
tTKPointDataSelector3Display.DataAxesGrid.ZTitleFontFile = ''
tTKPointDataSelector3Display.DataAxesGrid.XLabelFontFile = ''
tTKPointDataSelector3Display.DataAxesGrid.YLabelFontFile = ''
tTKPointDataSelector3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKPointDataSelector3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKPointDataSelector3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKPointDataSelector3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKPointDataSelector3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold5
threshold5Display = Show(threshold5, renderView1)

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = ['POINTS', 'CriticalType']
threshold5Display.LookupTable = criticalTypeLUT
threshold5Display.Specular = 1.0
threshold5Display.OSPRayScaleArray = 'Birth'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'Birth'
threshold5Display.ScaleFactor = 0.00999999642372131
threshold5Display.SelectScaleArray = 'Birth'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GlyphTableIndexArray = 'Birth'
threshold5Display.GaussianRadius = 0.000499999821186066
threshold5Display.SetScaleArray = ['POINTS', 'Birth']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'Birth']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.SelectionCellLabelFontFile = ''
threshold5Display.SelectionPointLabelFontFile = ''
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityFunction = criticalTypePWF
threshold5Display.ScalarOpacityUnitDistance = 0.0192808844313789

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display.ScaleTransferFunction.Points = [-16.5644995786495, 0.0, 0.5, 0.0, -1.16099901633567, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display.OpacityTransferFunction.Points = [-16.5644995786495, 0.0, 0.5, 0.0, -1.16099901633567, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold5Display.DataAxesGrid.XTitleFontFile = ''
threshold5Display.DataAxesGrid.YTitleFontFile = ''
threshold5Display.DataAxesGrid.ZTitleFontFile = ''
threshold5Display.DataAxesGrid.XLabelFontFile = ''
threshold5Display.DataAxesGrid.YLabelFontFile = ''
threshold5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold5Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold5Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold5Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold6
threshold6Display = Show(threshold6, renderView1)

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['POINTS', 'CriticalType']
threshold6Display.LookupTable = criticalTypeLUT
threshold6Display.Specular = 1.0
threshold6Display.OSPRayScaleArray = 'Birth'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'None'
threshold6Display.ScaleFactor = 0.00999999642372131
threshold6Display.SelectScaleArray = 'None'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GlyphTableIndexArray = 'None'
threshold6Display.GaussianRadius = 0.000499999821186066
threshold6Display.SetScaleArray = ['POINTS', 'Birth']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'Birth']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.SelectionCellLabelFontFile = ''
threshold6Display.SelectionPointLabelFontFile = ''
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityFunction = criticalTypePWF
threshold6Display.ScalarOpacityUnitDistance = 0.0192808844313789

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display.ScaleTransferFunction.Points = [-21.4808408073486, 0.0, 0.5, 0.0, 13.7679796875201, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display.OpacityTransferFunction.Points = [-21.4808408073486, 0.0, 0.5, 0.0, 13.7679796875201, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold6Display.DataAxesGrid.XTitleFontFile = ''
threshold6Display.DataAxesGrid.YTitleFontFile = ''
threshold6Display.DataAxesGrid.ZTitleFontFile = ''
threshold6Display.DataAxesGrid.XLabelFontFile = ''
threshold6Display.DataAxesGrid.YLabelFontFile = ''
threshold6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold6Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold6Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold6Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['POINTS', 'CriticalType']
tube1Display.LookupTable = criticalTypeLUT
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'ConnectedComponentId'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'ConnectedComponentId'
tube1Display.ScaleFactor = 0.765032261610031
tube1Display.SelectScaleArray = 'ConnectedComponentId'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'ConnectedComponentId'
tube1Display.GaussianRadius = 0.0382516130805016
tube1Display.SetScaleArray = ['POINTS', 'ConnectedComponentId']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'ConnectedComponentId']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.0, 1.0, 0.5, 0.0]

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

# show data from tube2
tube2Display = Show(tube2, renderView1)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Opacity = 0.5
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'ConnectedComponentId'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'ConnectedComponentId'
tube2Display.ScaleFactor = 0.756290140748024
tube2Display.SelectScaleArray = 'ConnectedComponentId'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'ConnectedComponentId'
tube2Display.GaussianRadius = 0.0378145070374012
tube2Display.SetScaleArray = ['POINTS', 'ConnectedComponentId']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'ConnectedComponentId']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.SelectionCellLabelFontFile = ''
tube2Display.SelectionPointLabelFontFile = ''
tube2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.0, 1.0, 0.5, 0.0]

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

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKPointDataSelector2.DebugLevel = int(debugLevel)
if tTKPointDataSelector2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPointDataSelector2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPointDataSelector2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPointDataSelector2, i)))
else:
	SaveData(outputDirectory + 'tTKPointDataSelector2.vtu',
		CleantoGrid(OutputPort(tTKPointDataSelector2)))


tTKTrackingFromFields1.DebugLevel = int(debugLevel)
if tTKTrackingFromFields1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTrackingFromFields1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTrackingFromFields1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTrackingFromFields1, i)))
else:
	SaveData(outputDirectory + 'tTKTrackingFromFields1.vtu',
		CleantoGrid(OutputPort(tTKTrackingFromFields1)))


tTKPointDataSelector3.DebugLevel = int(debugLevel)
if tTKPointDataSelector3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPointDataSelector3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPointDataSelector3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPointDataSelector3, i)))
else:
	SaveData(outputDirectory + 'tTKPointDataSelector3.vtu',
		CleantoGrid(OutputPort(tTKPointDataSelector3)))


tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))


tTKPointDataSelector1.DebugLevel = int(debugLevel)
if tTKPointDataSelector1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPointDataSelector1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPointDataSelector1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPointDataSelector1, i)))
else:
	SaveData(outputDirectory + 'tTKPointDataSelector1.vtu',
		CleantoGrid(OutputPort(tTKPointDataSelector1)))


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


tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
