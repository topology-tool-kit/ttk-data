#!/usr/bin/env pvpython

import os
from paraview.simple import *
from vtk import vtkSMTrace

if len(sys.argv) == 3:
    stateFile = sys.argv[1]
    outputDir = sys.argv[2]
else:
    print("Error! Missing mandatory arguments!")
    print("Usage:")
    print("  ", sys.argv[0], " <input state file> <output directory>")
    sys.exit()

LoadState(stateFile)

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

f = open(outputDir + "/pythonScript.py", 'w')
f.write(vtkSMTrace.GetState(1, 1))
f.close()
