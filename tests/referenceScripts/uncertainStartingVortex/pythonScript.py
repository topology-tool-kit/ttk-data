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
uncertainStartingVortexvti = XMLImageDataReader(FileName=['uncertainStartingVortex.vti'])
uncertainStartingVortexvti.PointArrayStatus = ['lowerBoundField', 'upperBoundField']

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(Input=uncertainStartingVortexvti)
randomAttributes1.DataType = 'Double'
randomAttributes1.ComponentRange = [0.0, 0.999]
randomAttributes1.GeneratePointScalars = 1
randomAttributes1.GenerateCellVectors = 0

# create a new 'Calculator'
calculator1 = Calculator(Input=randomAttributes1)
calculator1.ResultArrayName = 'realization0'
calculator1.Function = 'lowerBoundField+(upperBoundField-lowerBoundField)*RandomPointScalars'

# create a new 'Random Attributes'
randomAttributes2 = RandomAttributes(Input=calculator1)
randomAttributes2.DataType = 'Float'
randomAttributes2.ComponentRange = [0.0, 1.0]
randomAttributes2.GeneratePointScalars = 1
randomAttributes2.GenerateCellVectors = 0

# create a new 'Calculator'
calculator2 = Calculator(Input=randomAttributes2)
calculator2.ResultArrayName = 'realization1'
calculator2.Function = 'lowerBoundField+(upperBoundField-lowerBoundField)*RandomPointScalars'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=calculator2)
tTKPersistenceDiagram2.ScalarField = 'realization1'
tTKPersistenceDiagram2.InputOffsetField = ''

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram2)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold3)

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram2)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [0.0, 185964.0]

# create a new 'Threshold'
persistenceThreshold2 = Threshold(Input=threshold4)
persistenceThreshold2.Scalars = ['CELLS', 'Persistence']
persistenceThreshold2.ThresholdRange = [0.05, 1.77902963800645]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=persistenceThreshold2)
tTKSphereFromPoint3.Radius = 0.025
tTKSphereFromPoint3.ThetaResolution = 8
tTKSphereFromPoint3.PhiResolution = 8

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=persistenceThreshold2)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=calculator2,
    Constraints=persistenceThreshold2)
tTKTopologicalSimplification2.ScalarField = 'realization1'
tTKTopologicalSimplification2.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints2 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification2)
tTKScalarFieldCriticalPoints2.ScalarField = 'realization1'
tTKScalarFieldCriticalPoints2.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints2.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints2)
tTKSphereFromPoint4.Radius = 0.002
tTKSphereFromPoint4.ThetaResolution = 8
tTKSphereFromPoint4.PhiResolution = 8

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(Input=uncertainStartingVortexvti)
tTKMandatoryCriticalPoints1.LowerBoundField = 'lowerBoundField'
tTKMandatoryCriticalPoints1.UpperBoundField = 'upperBoundField'
tTKMandatoryCriticalPoints1.NormalizedThreshold = 0.02

# create a new 'Threshold'
threshold6 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold6.Scalars = ['POINTS', 'MinimumComponents']
threshold6.ThresholdRange = [0.0, 2.0]

# find source
tTKMandatoryCriticalPoints1_1 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1_1,3))
threshold5.Scalars = ['POINTS', 'MaximumComponents']
threshold5.ThresholdRange = [0.0, 8.0]

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'NodeType']
tube4.Vectors = [None, '']
tube4.Radius = 0.01

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = [None, '']
tube3.Radius = 0.015

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = 'realization0'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [0.0, 185374.0]

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold2)
persistenceThreshold1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold1.ThresholdRange = [0.05, 1.75475390406744]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold1)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.01

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold1)
tTKSphereFromPoint1.Radius = 0.025
tTKSphereFromPoint1.ThetaResolution = 8
tTKSphereFromPoint1.PhiResolution = 8

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1,
    Constraints=persistenceThreshold1)
tTKTopologicalSimplification1.ScalarField = 'realization0'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = 'realization0'
tTKScalarFieldCriticalPoints1.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 0.002
tTKSphereFromPoint2.ThetaResolution = 8
tTKSphereFromPoint2.PhiResolution = 8

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.015

# ----------------------------------------------------------------
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
tTKMandatoryCriticalPoints1.DebugLevel = int(debugLevel)
if tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1)))
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
