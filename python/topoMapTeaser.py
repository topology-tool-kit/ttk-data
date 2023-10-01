#!/usr/bin/env python

from paraview.simple import *

# create a new 'CSV Reader'
a3blobscsv = CSVReader(FileName=['3blobs.csv'])

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=a3blobscsv, ModulePath='default')
tTKDimensionReduction1.InputColumns = ['x', 'y', 'z']
tTKDimensionReduction1.Method = 'Topological Mapper'
tTKDimensionReduction1.Anglessamplingfrequency = 3

SaveData('3blobs_topoMap.csv', tTKDimensionReduction1)

# create a new 'CSV Reader'
a3ringscsv = CSVReader(FileName=['3rings.csv'])

# create a new 'TTK DimensionReduction'
tTKDimensionReduction2 = TTKDimensionReduction(Input=a3ringscsv, ModulePath='default')
tTKDimensionReduction2.InputColumns = ['x', 'y', 'z']
tTKDimensionReduction2.Method = 'Topological Mapper'
tTKDimensionReduction2.Anglessamplingfrequency = 3

SaveData('3rings_topoMap.csv', tTKDimensionReduction2)

# create a new 'CSV Reader'
a2cavitiescsv = CSVReader(FileName=['2cavities.csv'])

# create a new 'TTK DimensionReduction'
tTKDimensionReduction3 = TTKDimensionReduction(Input=a2cavitiescsv, ModulePath='default')
tTKDimensionReduction3.InputColumns = ['X', 'Y', 'Z']
tTKDimensionReduction3.Method = 'Topological Mapper'
tTKDimensionReduction3.Anglessamplingfrequency = 3

SaveData('2cavities_topoMap.csv', tTKDimensionReduction3)


