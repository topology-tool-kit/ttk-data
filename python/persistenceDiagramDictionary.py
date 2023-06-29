# state file generated using paraview version 5.11.1
import paraview

#### import the simple module from the paraview
from paraview.simple import *

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(registrationName='TTKCinemaReader1', DatabasePath='/home/keanu/ttk-data/Isabel.cdb')

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=tTKCinemaReader1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=tTKCinemaProductReader1)
calculator1.ResultArrayName = 'opposite'
calculator1.Function = '-velocityMag'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'opposite']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'opposite']
tTKPersistenceDiagram1.IgnoreBoundary = 1
tTKPersistenceDiagram1.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram1.Saddlesaddlediagramdimension1slowest = 0
tTKPersistenceDiagram1.Saddlemaximumdiagramdimensiond1 = 0
tTKPersistenceDiagram1.ClearDiscreteGradientCache = 1

# create a new 'TTK PersistenceDiagramDictionary'
tTKPersistenceDiagramDictionary1 = TTKPersistenceDiagramDictionary(registrationName='TTKPersistenceDiagramDictionary1', Input=tTKPersistenceDiagram1,
    optionalinput=None)
tTKPersistenceDiagramDictionary1.percentthreshold = 1.0
tTKPersistenceDiagramDictionary1.Compressionfactor = 5.0
tTKPersistenceDiagramDictionary1.Progressiveapproach = 1
tTKPersistenceDiagramDictionary1.ThreadNumber = 12

SaveData("PD-Dictionary_dict.vtm", OutputPort(tTKPersistenceDiagramDictionary1, 0))
SaveData("PD-Dictionary_weights.csv", OutputPort(tTKPersistenceDiagramDictionary1, 1))