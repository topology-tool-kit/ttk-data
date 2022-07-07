#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
fertilityvtu = XMLUnstructuredGridReader(FileName=['fertility.vtu'])
fertilityvtu.TimeArray = 'None'

# create a new 'TTK EigenField'
tTKEigenField1 = TTKEigenField(InputGeometry=fertilityvtu)
tTKEigenField1.Numberofeigenfunctions = 100
tTKEigenField1.Computestatistics = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKEigenField1)
calculator1.Function = '"OutputEigenFunctions_4"'

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=calculator1)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'Result']
tTKPersistentGenerators1.InputOffsetField = ['POINTS', 'Result']
tTKPersistentGenerators1.PruneHandlesGenerators = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistentGenerators1)
threshold1.Scalars = ['CELLS', 'IsFinite']

SaveData("PersistentGeneratorsFertility.vtu", threshold1)
