#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
ttkCinemaReader = TTKCinemaReader(DatabasePath='./heatedCylinder/heatedCylinder_2D_raw.cdb')

# create a new 'TTK CinemaQuery'
ttkCinemaQuery = TTKCinemaQuery(InputTable=ttkCinemaReader)
ttkCinemaQuery.SQLStatement = """SELECT * FROM InputTable0 WHERE time=4.2"""

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader = TTKCinemaProductReader(Input=ttkCinemaQuery)

# create a new 'TTK TopologicalSimplificationByPersistence'
ttkTopologicalSimplificationByPersistence = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence', Input=ttkCinemaProductReader)
ttkTopologicalSimplificationByPersistence.InputArray = ['POINTS', 'nrrd']
ttkTopologicalSimplificationByPersistence.PersistenceThreshold = 0.05

# create a new 'TTK Merge and Contour Tree (FTM)'
ttkMergeandContourTreeFTM = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM', Input=ttkTopologicalSimplificationByPersistence)
ttkMergeandContourTreeFTM.ScalarField = ['POINTS', 'nrrd']

# create a new 'TTK ContourTreeAlignment'
contourTreeAlignment = TTKContourTreeAlignment(Input=OutputPort(ttkMergeandContourTreeFTM,1),
    ExportPath='')
contourTreeAlignment.ScalarField = ['POINTS', 'Scalar']
contourTreeAlignment.Regionsizearray = ['CELLS', 'RegionSize']
contourTreeAlignment.SegmentationIDarrayforCT = ['CELLS', 'SegmentationId']
contourTreeAlignment.SegmentIDarrayforsegmentation = ['POINTS', 'Scalar']

# create a new 'TTK PlanarGraphLayout'
alignmentLayout = TTKPlanarGraphLayout(Input=contourTreeAlignment)
alignmentLayout.SequenceArray = ['POINTS', 'Scalar']
alignmentLayout.SizeArray = ['POINTS', 'BranchIDs']
alignmentLayout.UseBranches = 1
alignmentLayout.BranchArray = ['POINTS', 'BranchIDs']
alignmentLayout.LevelArray = ['POINTS', 'BranchIDs']

# create a new 'Calculator'
alignmentEdges = Calculator(Input=alignmentLayout)
alignmentEdges.CoordinateResults = 1
alignmentEdges.Function = 'iHat*Layout_Y+jHat*Scalar*3'

# save the output
SaveData('ContourTreeAlignment.vtu', alignmentEdges)
