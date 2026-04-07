#!/usr/bin/env python
from paraview.simple import *

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(DatabasePath="molecularVibration.cdb")

# create a new 'TTK CinemaQuery'
tTKCinemaQuery1 = TTKCinemaQuery(InputTable=tTKCinemaReader1)
tTKCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE ModeId=0 and GeomID in (10, 0, 20)"""

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaQuery1)

# create a new 'Calculator'
calculator1 = Calculator(Input=tTKCinemaProductReader1)
calculator1.ResultArrayName = "opposite"
calculator1.Function = "-rho"

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(Input=calculator1)
tTKScalarFieldNormalizer1.ScalarField = ["POINTS", "opposite"]

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(
    Input=tTKScalarFieldNormalizer1
)
tTKTopologicalSimplificationByPersistence1.InputArray = ["POINTS", "opposite"]
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 5e-05

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(
    Input=tTKTopologicalSimplificationByPersistence1
)
tTKMorseSmaleComplex1.ScalarField = ["POINTS", "opposite"]
tTKMorseSmaleComplex1.DiscreteGradientBackend = "Stochastic algorithm (IEEE TVCG 2012)"
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 2.5e-05

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1, 1))
threshold1.Scalars = ["CELLS", "SeparatrixType"]
threshold1.LowerThreshold = 0
threshold1.UpperThreshold = 0

# create a new 'TTK SeparatrixStability'
tTKSeparatrixStability1 = TTKSeparatrixStability(Input=threshold1)

# Extract the entry #1, corresponding to the equilibrium state
extractBlock11 = ExtractBlock(Input=tTKSeparatrixStability1)
extractBlock11.Assembly = "Hierarchy"
extractBlock11.Selectors = ["/Root/Block1"]

SaveData("bondOccurrenceRate.vtm", extractBlock11)
