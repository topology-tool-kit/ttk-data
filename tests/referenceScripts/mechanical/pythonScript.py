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
