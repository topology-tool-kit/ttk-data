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

# ----------------------------------------------------------------
# restore active view
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
# ----------------------------------------------------------------

# show data from tTKPointDataSelector1

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

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKPointDataSelector2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from threshold2

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

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from threshold3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tTKPointDataSelector3

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from threshold5

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from threshold6

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube1

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'

# show data from tube2

# trace defaults for the display properties.

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

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
