#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
uncertainStartingVortexvti = XMLImageDataReader(FileName=['uncertainStartingVortex.vti'])
uncertainStartingVortexvti.PointArrayStatus = ['lowerBoundField', 'upperBoundField']

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(Input=uncertainStartingVortexvti)
tTKMandatoryCriticalPoints1.LowerBoundField = ['POINTS', 'lowerBoundField']
tTKMandatoryCriticalPoints1.UpperBoundField = ['POINTS', 'upperBoundField']
tTKMandatoryCriticalPoints1.NormalizedThreshold = 0.02

# create a new 'Threshold' for the Minimas
threshold6 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold6.Scalars = ['POINTS', 'MinimumComponents']
threshold6.ThresholdRange = [0.0, 2.0]

# create a new 'Threshold' for the maximas
threshold5 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1,3))
threshold5.Scalars = ['POINTS', 'MaximumComponents']
threshold5.ThresholdRange = [0.0, 8.0]

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

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'realization0']
tTKPersistenceDiagram1.InputOffsetField = [None, '']

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [0.0, 185374.0]

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold2)
persistenceThreshold1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold1.ThresholdRange = [0.05, 1.75475390406744]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1,
    Constraints=persistenceThreshold1)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'realization0']
tTKTopologicalSimplification1.InputOffsetField = [None, '']
tTKTopologicalSimplification1.VertexIdentifierField = [None, '']

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'realization0']
tTKScalarFieldCriticalPoints1.InputOffsetField = ['POINTS', 'OutputOffsetScalarField']
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

SaveData('PersistenceDiagram.vtu', tTKPersistenceDiagram1)
SaveData('CriticalPoints.vtp', tTKScalarFieldCriticalPoints1)
SaveData('MandatoryCriticalMinima.csv', OutputPort(tTKMandatoryCriticalPoints1, 0))
SaveData('MandatoryCriticalMaxima.csv', OutputPort(tTKMandatoryCriticalPoints1, 3))
