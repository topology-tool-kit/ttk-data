#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML PolyData Reader'
ds14_scivis_0128_e4_dt04_10000vtp = XMLPolyDataReader(
    FileName=["./ds14_scivis_0128_e4_dt04_1.0000.vtp"]
)
ds14_scivis_0128_e4_dt04_10000vtp.PointArrayStatus = ["DarkMatter_Phi"]

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=ds14_scivis_0128_e4_dt04_10000vtp)
gaussianResampling1.ResampleField = ["POINTS", "DarkMatter_Phi"]
gaussianResampling1.ResamplingGrid = [256, 256, 256]
gaussianResampling1.GaussianSplatRadius = 0.008
gaussianResampling1.ScaleSplats = 0
gaussianResampling1.EllipticalSplats = 0
gaussianResampling1.FillVolumeBoundary = 0

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=gaussianResampling1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "SplatterValues"]
tTKScalarFieldSmoother1.IterationNumber = 5

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tTKScalarFieldSmoother1)
tTKPersistenceDiagram1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ["CELLS", "Persistence"]
threshold1.LowerThreshold = 0.25
threshold1.UpperThreshold = 2.0

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(
    Domain=tTKScalarFieldSmoother1, Constraints=threshold1
)
tTKTopologicalSimplification1.ScalarField = ["POINTS", "SplatterValues"]
tTKTopologicalSimplification1.Backend = "Topological Optimization (IEEE VIS 2024)"
tTKTopologicalSimplification1.StoppingConditionCoefficient = 0.0001
tTKTopologicalSimplification1.GradientStepSize = 0.75

# save the output
SaveData("darkSky_optimized.vti", tTKTopologicalSimplification1)
