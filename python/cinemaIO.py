#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
viscousFingerscdb = TTKCinemaReader(DatabasePath='ViscousFingers.cdb')

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=viscousFingerscdb)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Sim='run01' AND Time%10=0
ORDER BY Time
LIMIT 8 OFFSET 1"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'Slice'
slice1 = Slice(Input=tTKCinemaProductReader1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [31.5, 31.5, 31.5]

# create a new 'TTK GridLayout'
tTKGridLayout1 = TTKGridLayout(Input=slice1)
tTKGridLayout1.ColumnAxis = 'Y'
tTKGridLayout1.ColumnGap = 8.0
tTKGridLayout1.RowAxis = 'Z'
tTKGridLayout1.NumberofRows = 1

# create a new 'TTK ForEach'
tTKForEach1 = TTKForEach(Input=tTKGridLayout1)
tTKForEach1.IterationMode = 'Block'
tTKForEach1.InputArray = ['POINTS', 'ImageFile']
tTKForEach1.OutputType = 'vtkPolyData'

# create a new 'TTK ArrayEditor'
tTKArrayEditor1 = TTKArrayEditor(Target=tTKForEach1,
    Source=None)
tTKArrayEditor1.TargetAttributeType = 'Field Data'
tTKArrayEditor1.DataString = 'SampleInterval, 10'
tTKArrayEditor1.TargetArray = ['POINTS', 'ImageFile']

# create a new 'TTK CinemaWriter'
tTKCinemaWriter1 = TTKCinemaWriter(Input=tTKArrayEditor1,
    DatabasePath='ViscousFingersSampled.cdb')
tTKCinemaWriter1.ScalarField = ['POINTS', 'ImageFile']

# create a new 'TTK EndFor'
tTKEndFor1 = TTKEndFor(Data=tTKCinemaWriter1,
    For=tTKForEach1)

UpdatePipeline()