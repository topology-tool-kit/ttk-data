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

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
approximation = CreateView('RenderView')
approximation.ViewSize = [2257, 941]
approximation.AxesGrid = 'GridAxes3DActor'
approximation.CenterOfRotation = [0.05098852515220642, 0.007757805287837982, -0.007515609264373779]
approximation.StereoType = 0
approximation.CameraPosition = [0.32342304404218813, -0.15114741444504645, -0.8529719175670936]
approximation.CameraFocalPoint = [0.06943215176799095, -0.00637974759677277, 0.000372383563338938]
approximation.CameraViewUp = [-0.03505261349533795, 0.9835347185206385, -0.17728725772506898]
approximation.CameraParallelScale = 0.4910007305932758
approximation.Background = [0.32, 0.34, 0.43]
approximation.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
approximation.AxesGrid.XTitleFontFile = ''
approximation.AxesGrid.YTitleFontFile = ''
approximation.AxesGrid.ZTitleFontFile = ''
approximation.AxesGrid.XLabelFontFile = ''
approximation.AxesGrid.YLabelFontFile = ''
approximation.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
depthImages = CreateView('RenderView')
depthImages.ViewSize = [1026, 1920]
depthImages.InteractionMode = '2D'
depthImages.AxesGrid = 'GridAxes3DActor'
depthImages.OrientationAxesVisibility = 0
depthImages.CenterOfRotation = [127.5, 127.5, 0.0]
depthImages.StereoType = 0
depthImages.CameraPosition = [1172.3026274315816, 2852.8544594840146, 10000.0]
depthImages.CameraFocalPoint = [1172.3026274315816, 2852.8544594840146, 0.0]
depthImages.CameraParallelScale = 2776.9659647601684
depthImages.Background = [0.32, 0.34, 0.43]
depthImages.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
depthImages.AxesGrid.XTitleFontFile = ''
depthImages.AxesGrid.YTitleFontFile = ''
depthImages.AxesGrid.ZTitleFontFile = ''
depthImages.AxesGrid.XLabelFontFile = ''
depthImages.AxesGrid.YLabelFontFile = ''
depthImages.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
groundTruth = CreateView('RenderView')
groundTruth.ViewSize = [2257, 941]
groundTruth.AxesGrid = 'GridAxes3DActor'
groundTruth.CenterOfRotation = [0.05098852515220642, 0.007757805287837982, -0.007515609264373779]
groundTruth.StereoType = 0
groundTruth.CameraPosition = [0.32342304404218813, -0.15114741444504645, -0.8529719175670936]
groundTruth.CameraFocalPoint = [0.06943215176799095, -0.00637974759677277, 0.000372383563338938]
groundTruth.CameraViewUp = [-0.03505261349533795, 0.9835347185206385, -0.17728725772506898]
groundTruth.CameraParallelScale = 0.4910007305932758
groundTruth.Background = [0.32, 0.34, 0.43]
groundTruth.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
groundTruth.AxesGrid.XTitleFontFile = ''
groundTruth.AxesGrid.YTitleFontFile = ''
groundTruth.AxesGrid.ZTitleFontFile = ''
groundTruth.AxesGrid.XLabelFontFile = ''
groundTruth.AxesGrid.YLabelFontFile = ''
groundTruth.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(approximation)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML PolyData Reader'
streamlinesvtp = XMLPolyDataReader(FileName=['GroundWater.cdb/streamlines.vtp'])

# create a new 'XML PolyData Reader'
stonevtp = XMLPolyDataReader(FileName=['GroundWater.cdb/stone.vtp'])

# create a new 'TTK IcoSphere'
tTKIcoSphere1 = TTKIcoSphere()
tTKIcoSphere1.Subdivisions = 1
tTKIcoSphere1.Radius = 0.6

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKIcoSphere1)
tTKSphereFromPoint1.Radius = 0.005

# create a new 'Elevation'
fakeShadow = Elevation(Input=stonevtp)
fakeShadow.LowPoint = [0.13294358695786565, 0.08882809227819845, -0.018024881743751362]
fakeShadow.HighPoint = [0.06742407365289238, 0.018398674549435334, 0.138207120609427]

# create a new 'TTK CinemaImaging'
tTKCinemaImaging1 = TTKCinemaImaging(Dataset=fakeShadow,
    SamplingGrid=tTKIcoSphere1)
tTKCinemaImaging1.Resolution = [512, 512]

# create a new 'TTK CinemaLayout'
tTKCinemaLayout1 = TTKCinemaLayout(Input=tTKCinemaImaging1)
tTKCinemaLayout1.ColumnGap = 5.0
tTKCinemaLayout1.RowGap = 5.0
tTKCinemaLayout1.NumberofRows = 10

# create a new 'TTK DepthImageBasedGeometryApproximation'
tTKDepthImageBasedGeometryApproximation1 = TTKDepthImageBasedGeometryApproximation(Input=tTKCinemaImaging1)
tTKDepthImageBasedGeometryApproximation1.DepthValues = 'Depth'

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKDepthImageBasedGeometryApproximation1)
threshold1.Scalars = ['CELLS', 'Distortion']
threshold1.ThresholdRange = [0.0, 0.01]

# ----------------------------------------------------------------
# setup the visualization in view 'approximation'
# ----------------------------------------------------------------

# show data from threshold1

# get color transfer function/color map for 'Elevation'
elevationLUT = GetColorTransferFunction('Elevation')
elevationLUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
elevationLUT.ColorSpace = 'RGB'
elevationLUT.NanColor = [1.0, 0.0, 0.0]
elevationLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Elevation'
elevationPWF = GetOpacityTransferFunction('Elevation')
elevationPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from streamlinesvtp

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKIcoSphere1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# setup the visualization in view 'depthImages'
# ----------------------------------------------------------------

# show data from tTKCinemaLayout1

# get color transfer function/color map for 'Depth'
depthLUT = GetColorTransferFunction('Depth')
depthLUT.RGBPoints = [0.019294383004307747, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
depthLUT.ColorSpace = 'RGB'
depthLUT.NanColor = [1.0, 0.0, 0.0]
depthLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Depth'
depthPWF = GetOpacityTransferFunction('Depth')
depthPWF.Points = [0.019294383004307747, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
depthPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# setup the color legend parameters for each legend in this view

# get color legend/bar for depthLUT in view depthImages
depthLUTColorBar = GetScalarBar(depthLUT, depthImages)
depthLUTColorBar.Title = 'Depth'
depthLUTColorBar.ComponentTitle = ''
depthLUTColorBar.TitleFontFile = ''
depthLUTColorBar.LabelFontFile = ''

# set color bar visibility
depthLUTColorBar.Visibility = 1

# show color legend

# ----------------------------------------------------------------
# setup the visualization in view 'groundTruth'
# ----------------------------------------------------------------

# show data from tTKIcoSphere1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from streamlinesvtp

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKSphereFromPoint1

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from fakeShadow

# trace defaults for the display properties.

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKIcoSphere1.DebugLevel = int(debugLevel)
if tTKIcoSphere1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIcoSphere1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIcoSphere1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIcoSphere1, i)))
else:
	SaveData(outputDirectory + 'tTKIcoSphere1.vtu',
		CleantoGrid(OutputPort(tTKIcoSphere1)))


tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))


tTKCinemaImaging1.DebugLevel = int(debugLevel)
if tTKCinemaImaging1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKCinemaImaging1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKCinemaImaging1_' + str(i) + '.vtm',
			CleantoGrid(OutputPort(tTKCinemaImaging1, i)))
else:
	SaveData(outputDirectory + 'tTKCinemaImaging1.vtm',
		CleantoGrid(OutputPort(tTKCinemaImaging1)))


tTKCinemaLayout1.DebugLevel = int(debugLevel)
if tTKCinemaLayout1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKCinemaLayout1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKCinemaLayout1_' + str(i) + '.vtm',
			CleantoGrid(OutputPort(tTKCinemaLayout1, i)))
else:
	SaveData(outputDirectory + 'tTKCinemaLayout1.vtm',
		CleantoGrid(OutputPort(tTKCinemaLayout1)))


tTKDepthImageBasedGeometryApproximation1.DebugLevel = int(debugLevel)
if tTKDepthImageBasedGeometryApproximation1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDepthImageBasedGeometryApproximation1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDepthImageBasedGeometryApproximation1_' + str(i) + '.vtm',
			CleantoGrid(OutputPort(tTKDepthImageBasedGeometryApproximation1, i)))
else:
	SaveData(outputDirectory + 'tTKDepthImageBasedGeometryApproximation1.vtm',
		CleantoGrid(OutputPort(tTKDepthImageBasedGeometryApproximation1)))
