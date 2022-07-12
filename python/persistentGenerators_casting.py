#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
castingvtu = XMLUnstructuredGridReader(FileName=["casting.vtu"])
castingvtu.CellArrayStatus = ["GroupIds"]
castingvtu.TimeArray = "None"

# create a new 'TTK EigenField'
tTKEigenField1 = TTKEigenField(InputGeometry=castingvtu)
tTKEigenField1.Numberofeigenfunctions = 98
tTKEigenField1.Computestatistics = 1
tTKEigenField1.Outputscalarfieldname = "E"

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKEigenField1)
calculator1.Function = "Statistics_EigenMagnitude"

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=calculator1)
tTKPersistentGenerators1.ScalarField = ["POINTS", "Result"]
tTKPersistentGenerators1.InputOffsetField = ["POINTS", "Result"]
tTKPersistentGenerators1.PruneHandlesGenerators = 1

SaveData("PersistentGeneratorsCasting.vtp", tTKPersistentGenerators1)
