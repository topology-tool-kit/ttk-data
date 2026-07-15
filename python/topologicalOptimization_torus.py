#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
torusvtu = XMLUnstructuredGridReader(FileName=["torus.vtu"])

# create a new 'TTK SignedDistanceField'
tTKSignedDistanceField1 = TTKSignedDistanceField(Input=torusvtu)
tTKSignedDistanceField1.SamplingDimensions = [64, 64, 64]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKSignedDistanceField1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "signedDistanceField"]

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ["CELLS", "IsFinite"]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tTKSignedDistanceField1, Constraints=threshold2
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "signedDistanceField"]
tTKTopologicalSimplification1.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification1.StoppingConditionCoefficient = 0.001
tTKTopologicalSimplification1.MaximumIterationNumber = 2000
tTKTopologicalSimplification1.CancellationPrimitive = "Cut-only"
tTKTopologicalSimplification1.GradientStepSize = 0.9

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=tTKTopologicalSimplification1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "signedDistanceField"]

# create a new 'Contour'
contour1 = Contour(Input=tTKScalarFieldSmoother1)
contour1.ContourBy = ["POINTS", "signedDistanceField"]
contour1.Isosurfaces = [0.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(
    Domain=tTKSignedDistanceField1, Constraints=threshold2
)
tTKTopologicalSimplification2.ScalarField = ["POINTS", "signedDistanceField"]
tTKTopologicalSimplification2.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification2.StoppingConditionCoefficient = 0.001
tTKTopologicalSimplification2.MaximumIterationNumber = 2000
tTKTopologicalSimplification2.CancellationPrimitive = "Fill-only"
tTKTopologicalSimplification2.GradientStepSize = 0.9
tTKTopologicalSimplification2.ConstraintAveraging = 0

# create a new 'Contour'
contour2 = Contour(Input=tTKTopologicalSimplification2)
contour2.ContourBy = ["POINTS", "signedDistanceField"]
contour2.Isosurfaces = [0.0]

SaveData("topoOpt_torus_cut.vtp", contour1)
SaveData("topoOpt_torus_fill.vtp", contour2)
