#!/usr/bin/env python

#### import the simple module from the paraview
from paraview.simple import *

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML PolyData Reader'
ds14_scivis_0128_e4_dt04_10000vtp = XMLPolyDataReader(
    FileName=["ds14_scivis_0128_e4_dt04_1.0000.vtp"]
)

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=ds14_scivis_0128_e4_dt04_10000vtp)
gaussianResampling1.ResampleField = ["POINTS", "DarkMatter_Phi"]
gaussianResampling1.ResamplingGrid = [64, 64, 64]
gaussianResampling1.SplatAccumulationMode = "Max"
gaussianResampling1.GaussianSplatRadius = 0.0125
gaussianResampling1.ScaleSplats = 0

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=gaussianResampling1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "SplatterValues"]
tTKScalarFieldSmoother1.IterationNumber = 1

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=tTKScalarFieldSmoother1)
tTKScalarFieldNormalizer1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(
    Input=tTKScalarFieldNormalizer1
)
tTKTopologicalSimplificationByPersistence1.InputArray = ["POINTS", "SplatterValues"]
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.3

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(
    Input=tTKTopologicalSimplificationByPersistence1
)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "SplatterValues"]
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.3
tTKMorseSmaleComplex1.Forceloopfreegradient = 0

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold3.Scalars = ["CELLS", "SeparatrixType"]
threshold3.LowerThreshold = 2.0
threshold3.UpperThreshold = 2.0

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(
    registrationName="TTKGeometrySmoother2", Input=threshold3
)
tTKGeometrySmoother2.IterationNumber = 10

SaveData("cosmicWeb.vtu", tTKGeometrySmoother2)
