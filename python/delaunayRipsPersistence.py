#!/usr/bin/env python

from paraview.simple import *

comet67PChuryumovGerasimenkovtp = XMLPolyDataReader(FileName=['67P-Churyumov-Gerasimenko.vtp'])
tTKDelaunayRipsPersistenceGenerators1 = TTKDelaunayRipsPersistenceGenerators(Input=comet67PChuryumovGerasimenkovtp)
threshold1 = Threshold(Input=OutputPort(tTKDelaunayRipsPersistenceGenerators1,2))
threshold1.Set(Scalars=['CELLS', 'ClassPersistence'], LowerThreshold=1, UpperThreshold=2)
SaveData("67PChuryumovGerasimenko_generator.obj", threshold1)
SaveData("67PChuryumovGerasimenko_diagram.csv", OutputPort(tTKDelaunayRipsPersistenceGenerators1,0))

k4csv = CSVReader(FileName=['K4.csv'])
tableToPoints2 = TableToPoints(Input=k4csv)
tableToPoints2.Set(XColumn='x', YColumn='y', ZColumn='z')
tTKDelaunayRipsPersistenceGenerators2 = TTKDelaunayRipsPersistenceGenerators(Input=tableToPoints2)
SaveData("K4_diagram.csv", OutputPort(tTKDelaunayRipsPersistenceGenerators2,0))

hypersphere5Dcsv = CSVReader(FileName=['hypersphere5D.csv'])
hypersphere5Dcsv.HaveHeaders = 0
tTKDelaunayRipsPersistenceDiagram3 = TTKDelaunayRipsPersistenceDiagram(Input=hypersphere5Dcsv)
tTKDelaunayRipsPersistenceDiagram3.InputColumns = ['Field 0', 'Field 1', 'Field 2', 'Field 3', 'Field 4']
SaveData("hypersphere5D_diagram.csv", tTKDelaunayRipsPersistenceDiagram3)