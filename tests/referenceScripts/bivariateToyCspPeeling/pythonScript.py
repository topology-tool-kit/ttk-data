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
