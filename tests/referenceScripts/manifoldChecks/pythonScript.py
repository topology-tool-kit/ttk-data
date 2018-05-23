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
manifoldCheck2vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck2.vtu'])

# create a new 'XML Unstructured Grid Reader'
manifoldCheck1vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck1.vtu'])

# create a new 'XML Unstructured Grid Reader'
manifoldCheck0vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck0.vtu'])

# create a new 'Tetrahedralize'
tetrahedralize3 = Tetrahedralize(Input=manifoldCheck2vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck3 = TTKManifoldCheck(Input=tetrahedralize3)

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKManifoldCheck3)
threshold3.Scalars = ['CELLS', 'TriangleLinkComponentNumber']
threshold3.ThresholdRange = [3.0, 3.0]

# create a new 'TTK Identifiers'
tTKIdentifiers1 = TTKIdentifiers(Input=threshold3)

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKIdentifiers1)
threshold4.Scalars = ['CELLS', 'CellIdentifiers']
threshold4.ThresholdRange = [0.0, 1.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold4)

# create a new 'Threshold'
threshold5 = Threshold(Input=extractSurface2)
threshold5.Scalars = ['POINTS', 'TriangleLinkComponentNumber']
threshold5.ThresholdRange = [3.0, 3.0]

# create a new 'Extract Edges'
extractEdges3 = ExtractEdges(Input=threshold5)

# create a new 'Tube'
tube4 = Tube(Input=extractEdges3)
tube4.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube4.Vectors = [None, '']
tube4.Radius = 0.05

# create a new 'Extract Edges'
extractEdges4 = ExtractEdges(Input=tTKManifoldCheck3)

# create a new 'Tube'
tube5 = Tube(Input=extractEdges4)
tube5.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube5.Vectors = [None, '']
tube5.Radius = 0.0075

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=manifoldCheck1vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck2 = TTKManifoldCheck(Input=tetrahedralize2)

# create a new 'Extract Edges'
extractEdges2 = ExtractEdges(Input=tTKManifoldCheck2)

# create a new 'Threshold'
threshold2 = Threshold(Input=extractEdges2)
threshold2.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
threshold2.ThresholdRange = [2.0, 2.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold2)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface1)
tube3.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube3.Vectors = [None, '']
tube3.Radius = 0.05

# create a new 'Tube'
tube2 = Tube(Input=extractEdges2)
tube2.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube2.Vectors = [None, '']
tube2.Radius = 0.0075

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=manifoldCheck0vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck1 = TTKManifoldCheck(Input=tetrahedralize1)

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=tTKManifoldCheck1)

# create a new 'Tube'
tube1 = Tube(Input=extractEdges1)
tube1.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube1.Vectors = [None, '']
tube1.Radius = 0.0075

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKManifoldCheck1)
tTKSphereFromPoint1.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKManifoldCheck3)
tTKSphereFromPoint4.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tTKManifoldCheck2)
tTKSphereFromPoint3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKManifoldCheck1)
tTKSphereFromPoint2.Radius = 0.1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKSphereFromPoint2)
threshold1.Scalars = ['POINTS', 'VertexLinkComponentNumber']
threshold1.ThresholdRange = [2.0, 2.0]

# ----------------------------------------------------------------
tTKManifoldCheck3.DebugLevel = int(debugLevel)
if tTKManifoldCheck3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKManifoldCheck3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKManifoldCheck3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKManifoldCheck3, i)))
else:
	SaveData(outputDirectory + 'tTKManifoldCheck3.vtu',
		CleantoGrid(OutputPort(tTKManifoldCheck3)))
tTKIdentifiers1.DebugLevel = int(debugLevel)
if tTKIdentifiers1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKIdentifiers1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKIdentifiers1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKIdentifiers1, i)))
else:
	SaveData(outputDirectory + 'tTKIdentifiers1.vtu',
		CleantoGrid(OutputPort(tTKIdentifiers1)))
tTKManifoldCheck2.DebugLevel = int(debugLevel)
if tTKManifoldCheck2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKManifoldCheck2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKManifoldCheck2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKManifoldCheck2, i)))
else:
	SaveData(outputDirectory + 'tTKManifoldCheck2.vtu',
		CleantoGrid(OutputPort(tTKManifoldCheck2)))
tTKManifoldCheck1.DebugLevel = int(debugLevel)
if tTKManifoldCheck1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKManifoldCheck1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKManifoldCheck1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKManifoldCheck1, i)))
else:
	SaveData(outputDirectory + 'tTKManifoldCheck1.vtu',
		CleantoGrid(OutputPort(tTKManifoldCheck1)))
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))
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
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
