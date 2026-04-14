#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
pegasusvtu = XMLUnstructuredGridReader(FileName=["pegasus.vtu"])

# create a new 'Clip'
clip1 = Clip(Input=pegasusvtu)
clip1.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [29.7661, 0.0, 0.0]
clip1.ClipType.Normal = [-1.0, 0.0, 0.0]

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.0, -40.2344, 0.0]
clip2.ClipType.Normal = [0.0, -1.0, 0.0]

# create a new 'Clip'
clip3 = Clip(Input=clip2)
clip3.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.0, 0.0, -1141.19]
clip3.ClipType.Normal = [0.0, 0.0, -1.0]

# create a new 'Clip'
clip4 = Clip(Input=clip3)
clip4.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [35.8833, 0.0, 0.0]

# create a new 'Clip'
clip5 = Clip(Input=clip4)
clip5.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip5.ClipType.Origin = [0.0, -28.6559, 0.0]
clip5.ClipType.Normal = [0.0, 1.0, 0.0]

# create a new 'Clip'
clip6 = Clip(Input=clip5)
clip6.ClipType = "Plane"

# init the 'Plane' selected for 'ClipType'
clip6.ClipType.Origin = [0.0, 0.0, -1133.85]
clip6.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=clip6)

# create a new 'TTK SignedDistanceField'
tTKSignedDistanceField1 = TTKSignedDistanceField(Input=tetrahedralize1)
tTKSignedDistanceField1.SamplingDimensions = [68, 128, 81]
tTKSignedDistanceField1.ExpandBox = 0

# create a new 'Calculator'
calculator2 = Calculator(Input=tTKSignedDistanceField1)
calculator2.Function = "-signedDistanceField"

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=calculator2)
tTKPersistenceDiagram3.ScalarField = ["POINTS", "Result"]

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram3)
threshold4.Scalars = ["CELLS", "Persistence"]
threshold4.LowerThreshold = 0.277
threshold4.UpperThreshold = 0.278
threshold4.Invert = 1

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(
    Domain=calculator2, Constraints=threshold4
)
tTKTopologicalSimplification2.ScalarField = ["POINTS", "Result"]
tTKTopologicalSimplification2.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification2.StoppingConditionCoefficient = 1e-05
tTKTopologicalSimplification2.MaximumIterationNumber = 125
tTKTopologicalSimplification2.CancellationPrimitive = "Fill-only"
tTKTopologicalSimplification2.GradientStepSize = 1.252

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=calculator2, Constraints=threshold4
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "Result"]
tTKTopologicalSimplification1.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification1.StoppingConditionCoefficient = 1e-05
tTKTopologicalSimplification1.MaximumIterationNumber = 125
tTKTopologicalSimplification1.CancellationPrimitive = "Cut-only"
tTKTopologicalSimplification1.GradientStepSize = 1.1

# save the output
SaveData("topoOpt_pegasus_fill.vti", tTKTopologicalSimplification2)
SaveData("topoOpt_pegasus_cut.vti", tTKTopologicalSimplification1)
