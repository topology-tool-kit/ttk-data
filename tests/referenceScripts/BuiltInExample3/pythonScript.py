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

# create a new 'XML Image Data Reader'
example3vti = XMLImageDataReader(FileName=['BuiltInExample3.vti'])
example3vti.PointArrayStatus = ['lowerBoundField', 'upperBoundField']

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=example3vti)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram2.ScalarField = 'upperBoundField'
tTKPersistenceDiagram2.InputOffsetField = ''

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram2)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=diagonal)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'lowerBoundField'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
persistencePairs = Threshold(Input=tTKPersistenceDiagram1)
persistencePairs.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs.ThresholdRange = [-0.1, 98.0]

# create a new 'Threshold'
diagonal_1 = Threshold(Input=tTKPersistenceDiagram1)
diagonal_1.Scalars = ['CELLS', 'PairIdentifier']
diagonal_1.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal_1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(Input=example3vti)
tTKMandatoryCriticalPoints1.LowerBoundField = 'lowerBoundField'
tTKMandatoryCriticalPoints1.UpperBoundField = 'upperBoundField'

# find source
tTKMandatoryCriticalPoints1_1 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=OutputPort(tTKMandatoryCriticalPoints1_1,5))

# create a new 'Tube'
tube6 = Tube(Input=extractSurface6)
tube6.Scalars = ['POINTS', 'ComponentId']
tube6.Vectors = [None, '']
tube6.Radius = 0.01

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold1.Scalars = ['POINTS', 'MinimumComponents']
threshold1.ThresholdRange = [-0.1, 21.0]

# find source
tTKMandatoryCriticalPoints1_2 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=OutputPort(tTKMandatoryCriticalPoints1_2,4))

# create a new 'Tube'
tube5 = Tube(Input=extractSurface5)
tube5.Scalars = ['POINTS', 'ComponentId']
tube5.Vectors = [None, '']
tube5.Radius = 0.01

# find source
tTKMandatoryCriticalPoints1_3 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1_3,3))
threshold2.Scalars = ['POINTS', 'MaximumComponents']
threshold2.ThresholdRange = [-0.1, 27.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint6 = TTKSphereFromPoint(Input=OutputPort(tTKMandatoryCriticalPoints1_1,5))
tTKSphereFromPoint6.Radius = 0.025

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=OutputPort(tTKMandatoryCriticalPoints1_2,4))
tTKSphereFromPoint5.Radius = 0.025

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=persistencePairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.0, 1.37]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.0136209940910339

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 0.025

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint1)
tTKTopologicalSimplification1.ScalarField = 'lowerBoundField'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = 'lowerBoundField'
tTKScalarFieldCriticalPoints1.Withvertexidentifiers = 0
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 3.5

# create a new 'Threshold'
maxima = Threshold(Input=tTKSphereFromPoint2)
maxima.Scalars = ['POINTS', 'CriticalIndex']
maxima.ThresholdRange = [1.9, 2.0]

# create a new 'Threshold'
minima = Threshold(Input=tTKSphereFromPoint2)
minima.Scalars = ['POINTS', 'CriticalIndex']
minima.ThresholdRange = [0.0, 0.1]

# create a new 'Threshold'
persistencePairs_1 = Threshold(Input=tTKPersistenceDiagram2)
persistencePairs_1.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs_1.ThresholdRange = [-0.1, 108.0]

# create a new 'Threshold'
persistenceThreshold_1 = Threshold(Input=persistencePairs_1)
persistenceThreshold_1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold_1.ThresholdRange = [0.0, 1.38]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=persistenceThreshold_1)
tTKSphereFromPoint3.Radius = 0.025

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint3)
tTKTopologicalSimplification2.ScalarField = 'upperBoundField'
tTKTopologicalSimplification2.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints2 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification2)
tTKScalarFieldCriticalPoints2.ScalarField = 'upperBoundField'

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints2)
tTKSphereFromPoint4.Radius = 3.5

# create a new 'Threshold'
minima_1 = Threshold(Input=tTKSphereFromPoint4)
minima_1.Scalars = ['POINTS', 'CriticalIndex']
minima_1.ThresholdRange = [0.0, 0.1]

# create a new 'Threshold'
maxima_1 = Threshold(Input=tTKSphereFromPoint4)
maxima_1.Scalars = ['POINTS', 'CriticalIndex']
maxima_1.ThresholdRange = [1.9, 2.0]

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=persistenceThreshold_1)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'NodeType']
tube4.Vectors = [None, '']
tube4.Radius = 0.0136209940910339

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = [None, '']
tube3.Radius = 0.02

# create a new 'Transform'
transform1 = Transform(Input=threshold1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.0, 0.0, 0.0001]

# ----------------------------------------------------------------
tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))
tTKMandatoryCriticalPoints1.DebugLevel = int(debugLevel)
if tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1)))
tTKSphereFromPoint6.DebugLevel = int(debugLevel)
if tTKSphereFromPoint6.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint6.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint6_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint6, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint6.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint6)))
tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))
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
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))
tTKScalarFieldCriticalPoints2.DebugLevel = int(debugLevel)
if tTKScalarFieldCriticalPoints2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldCriticalPoints2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints2, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints2.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints2)))
tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))
