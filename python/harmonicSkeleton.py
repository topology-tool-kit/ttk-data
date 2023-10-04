#!/usr/bin/env python

#### import the simple module from the paraview
from paraview.simple import *

# load the pegasus dataset by creating a'XML Unstructured Grid Reader'
pegasusvtu = XMLUnstructuredGridReader(FileName=["pegasus.vtu"])

# create a new 'Elevation' on the dataset
elevation1 = Elevation(Input=pegasusvtu)
elevation1.LowPoint = [55.58376886060912, -88.42696707641238, -1166.7651999539546]
elevation1.HighPoint = [-27.56680371810648, 70.65296514617846, -1072.7592471929715]

# create a new 'Generate Ids'
generateIds1 = GenerateIds(Input=elevation1)
generateIds1.PointIdsArrayName = "ttkVertexScalarField"

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(
    SourceDataArrays=elevation1, DestinationMesh=generateIds1
)
resampleWithDataset1.PassPointArrays = 1
resampleWithDataset1.CellLocator = "Static Cell Locator"

# create a new 'Extract Selection', creating its query first and clearing it afterwards
Show()
QuerySelect(
    QueryString="(ttkVertexScalarField == 29019)",
    FieldType="POINT",
    InsideOut=0,
    Source=resampleWithDataset1,
)
extractSelection1 = ExtractSelection(Input=resampleWithDataset1)
ClearSelection()

# create a new 'Extract Selection', creating its query first and clearing it afterwards
QuerySelect(
    QueryString="(ttkVertexScalarField == 171102)",
    FieldType="POINT",
    InsideOut=0,
    Source=resampleWithDataset1,
)
extractSelection2 = ExtractSelection(Input=resampleWithDataset1)
ClearSelection()

# create a new 'Extract Selection', creating its query first and clearing it afterwards
QuerySelect(
    QueryString="(ttkVertexScalarField == 204530)",
    FieldType="POINT",
    InsideOut=0,
    Source=resampleWithDataset1,
)
extractSelection3 = ExtractSelection(Input=resampleWithDataset1)
ClearSelection()

# create a new 'Extract Selection', creating its query first and clearing it afterwards
QuerySelect(
    QueryString="(ttkVertexScalarField == 216852)",
    FieldType="POINT",
    InsideOut=0,
    Source=resampleWithDataset1,
)
extractSelection4 = ExtractSelection(Input=resampleWithDataset1)
ClearSelection()

# create a new 'Extract Selection', creating its query first and clearing it afterwards
QuerySelect(
    QueryString="(ttkVertexScalarField == 219572)",
    FieldType="POINT",
    InsideOut=0,
    Source=resampleWithDataset1,
)
extractSelection5 = ExtractSelection(Input=resampleWithDataset1)
ClearSelection()

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(
    Input=[
        extractSelection1,
        extractSelection2,
        extractSelection3,
        extractSelection4,
        extractSelection5,
    ]
)

# create a new 'TTK HarmonicField'
tTKHarmonicField1 = TTKHarmonicField(
    Domain=resampleWithDataset1, Constraints=appendDatasets1
)
tTKHarmonicField1.ScalarField = ["POINTS", "Elevation"]
tTKHarmonicField1.ConstraintVerticesIdentifiers = ["POINTS", "Elevation"]

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKHarmonicField1)
calculator1.ResultArrayName = "ScaledHarmonic"
calculator1.Function = "OutputHarmonicField^2.375"

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = ["POINTS", "ScaledHarmonic"]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKScalarFieldNormalizer1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "ScaledHarmonic"]
tTKPersistenceDiagram1.EmbedinDomain = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "Persistence"]
threshold1.ThresholdMethod = "Between"
threshold1.LowerThreshold = 0.001
threshold1.UpperThreshold = 999999999

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tTKScalarFieldNormalizer1, Constraints=threshold1
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "ScaledHarmonic"]

# create a new 'TTK Reeb Graph'
tTKReebgraphFTR1 = TTKReebGraph(Input=tTKTopologicalSimplification1)
tTKReebgraphFTR1.ScalarField = ["POINTS", "ScaledHarmonic"]
tTKReebgraphFTR1.ArcSampling = 20
tTKReebgraphFTR1.UseAllCores = False

# create a new 'TTK GeometrySmoother' taking the reeb graph edges for input
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=OutputPort(tTKReebgraphFTR1, 1))
tTKGeometrySmoother1.IterationNumber = 20

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube' representing the reep graph edges
tube1 = Tube(Input=extractSurface2)
tube1.Radius = 0.75

# create a new 'TTK IcospheresFromPoints' representing the reeb graph nodes
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(Input=tTKReebgraphFTR1)
tTKIcospheresFromPoints1.Radius = 2.0

SaveData("ReebGraphNodes.vtp", tTKIcospheresFromPoints1)
SaveData("ReebGraphArcs.vtp", tube1)
