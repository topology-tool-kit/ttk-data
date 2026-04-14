#!/usr/bin/env python

from paraview.simple import *

# create a new 'TTK CinemaReader'
ttkCinemaReader = TTKCinemaReader(
    DatabasePath="./heatedCylinder/heatedCylinder_2D_raw.cdb"
)

# create a new 'TTK CinemaQuery'
ttkCinemaQuery = TTKCinemaQuery(InputTable=ttkCinemaReader)
ttkCinemaQuery.SQLStatement = """SELECT * FROM InputTable0 WHERE time=4.2"""

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader = TTKCinemaProductReader(Input=ttkCinemaQuery)

# create a new 'TTK TopologicalSimplificationByPersistence'
ttkTopologicalSimplificationByPersistence = TTKTopologicalSimplificationByPersistence(
    Input=ttkCinemaProductReader
)
ttkTopologicalSimplificationByPersistence.InputArray = ["POINTS", "nrrd"]
ttkTopologicalSimplificationByPersistence.PersistenceThreshold = 0.05
ttkTopologicalSimplificationByPersistence.ThresholdIsAbsolute = True

# create a new 'TTK Merge and Contour Tree ()'
ttkMergeandContourTree = TTKContourTree(
    Input=ttkTopologicalSimplificationByPersistence
)
ttkMergeandContourTree.ScalarField = ["POINTS", "nrrd"]

# create a new 'TTK ContourTreeAlignment'
contourTreeAlignment = TTKContourTreeAlignment(
    Input=OutputPort(ttkMergeandContourTree, 1), ExportPath=""
)
contourTreeAlignment.ScalarField = ["POINTS", "Scalar"]
contourTreeAlignment.Regionsizearray = ["CELLS", "RegionSize"]
contourTreeAlignment.SegmentationIDarrayforCT = ["CELLS", "SegmentationId"]
contourTreeAlignment.SegmentIDarrayforsegmentation = ["POINTS", "Scalar"]
contourTreeAlignment.Seed = 35

# create a new 'TTK PlanarGraphLayout'
alignmentLayout = TTKPlanarGraphLayout(Input=contourTreeAlignment)
alignmentLayout.SequenceArray = ["POINTS", "Scalar"]
alignmentLayout.SizeArray = ["POINTS", "BranchIDs"]
alignmentLayout.UseBranches = 1
alignmentLayout.BranchArray = ["POINTS", "BranchIDs"]
alignmentLayout.LevelArray = ["POINTS", "BranchIDs"]

# create a new 'Calculator'
alignmentEdges = Calculator(Input=alignmentLayout)
alignmentEdges.CoordinateResults = 1
alignmentEdges.Function = "iHat*Layout_Y+jHat*Scalar*3"

# create a query selection
Show()
QuerySelect(
    QueryString="(id == 16)", Source=alignmentEdges, FieldType="POINT", InsideOut=0
)

# create a new 'Extract Selection'
selectedVertex = ExtractSelection(Input=alignmentEdges)

# create a new 'TTK GridLayout'
segmentationsGrid = TTKGridLayout(Input=OutputPort(ttkMergeandContourTree, 2))
segmentationsGrid.ColumnGap = 10.0
segmentationsGrid.RowGap = 10.0

# create a new 'TTK ForEach'
ttkForEach = TTKForEach(Input=segmentationsGrid)
ttkForEach.InputArray = ["POINTS", "SegmentationId"]
ttkForEach.ImageExtent = [0, 127, 0, 255, 0, 0]

# create a new 'Merge Blocks'
mergeBlocks = MergeBlocks(Input=ttkForEach)

# create a new 'TTK ArrayEditor'
passSegmentationIDs = TTKArrayEditor(Target=mergeBlocks, Source=selectedVertex)
passSegmentationIDs.EditorMode = "Add Arrays from Source"
passSegmentationIDs.TargetAttributeType = "Field Data"
passSegmentationIDs.SourcePointDataArrays = ["segmentationIDs"]
passSegmentationIDs.TargetArray = ["POINTS", "SegmentationId"]

# create a new 'TTK Extract'
extractMatchedGeometry = TTKExtract(Input=passSegmentationIDs)
extractMatchedGeometry.ExtractionMode = "Geometry"
extractMatchedGeometry.Expression = "{segmentationIDs[{_ttk_IterationInfo[0]}]}"
extractMatchedGeometry.ImageExtent = [
    2147483647,
    -2147483647,
    2147483647,
    -2147483647,
    2147483647,
    -2147483647,
]
extractMatchedGeometry.InputArray = ["POINTS", "SegmentationId"]

# create a new 'TTK BlockAggregator'
ttkBlockAggregator = TTKBlockAggregator(Input=extractMatchedGeometry)

# create a new 'TTK EndFor'
ttkEndFor = TTKEndFor(Data=ttkBlockAggregator, For=ttkForEach)

# save the output
SaveData("ContourTreeAlignment.vtu", alignmentEdges)
SaveData("Segmentations.vtm", segmentationsGrid)
SaveData("MatchedRegions.vtm", ttkEndFor)
