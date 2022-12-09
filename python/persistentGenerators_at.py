#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(FileName=["at.vti"])

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=atvti)
tTKPersistentGenerators1.ScalarField = ["POINTS", "density"]

SaveData("PersistentGeneratorsAt.vtp", tTKPersistentGenerators1)
