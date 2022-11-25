#!/usr/bin/env python

from paraview.simple import *

# create a new 'XML PolyData Reader'
ds14_scivis_0128_e4_dt04_06800vtp = XMLPolyDataReader(
    FileName=["ds14_scivis_0128_e4_dt04_1.0000.vtp"]
)

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=ds14_scivis_0128_e4_dt04_06800vtp)
gaussianResampling1.ResampleField = ["POINTS", "DarkMatter_Phi"]
gaussianResampling1.ResamplingGrid = [200, 200, 200]
gaussianResampling1.GaussianSplatRadius = 0.008

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=gaussianResampling1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "SplatterValues"]
tTKScalarFieldSmoother1.IterationNumber = 7

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKScalarFieldSmoother1)
calculator1.ResultArrayName = "SplatterValues"
calculator1.Function = "-SplatterValues"

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(Input=calculator1)
tTKPersistentGenerators1.ScalarField = ["POINTS", "SplatterValues"]

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistentGenerators1)
threshold1.Scalars = ["CELLS", "Persistence"]
threshold1.LowerThreshold = 0.24
threshold1.UpperThreshold = 0.2863966089734687

SaveData("PersistentGeneratorsDarkSky.vtu", threshold1)
