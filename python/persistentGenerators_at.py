#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(FileName=["at.vti"])
atvti.PointArrayStatus = ["density"]

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=atvti)
tTKPersistentGenerators1.ScalarField = ["POINTS", "density"]
tTKPersistentGenerators1.InputOffsetField = ["POINTS", "density"]
tTKPersistentGenerators1.PruneHandlesGenerators = 1

SaveData("PersistentGeneratorsAt.vtp", tTKPersistentGenerators1)
