#!/usr/bin/env python

import sys

from paraview.simple import *

# ----------------------------------------------------------------
# Choose the resampling dimension for the example
# ----------------------------------------------------------------

if len(sys.argv) == 2:
    dim = int(sys.argv[1])
else:
    dim = 256

# create a new 'XML Image Data Reader'
atvti = XMLImageDataReader(FileName=["at.vti"])
atvti.PointArrayStatus = ["density"]

calculator1 = Calculator(Input=atvti)
calculator1.ResultArrayType = "Float"
calculator1.ResultArrayName = "density"
calculator1.Function = "density"

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=calculator1)
computeDerivatives1.Scalars = ["POINTS", "density"]
computeDerivatives1.Vectors = ["POINTS", "1"]

# create a new 'Calculator'
calculator2 = Calculator(Input=computeDerivatives1)
calculator2.AttributeType = "Cell Data"
calculator2.ResultArrayName = "gradientMagnitude"
calculator2.Function = "mag(ScalarGradient)"
calculator2.ResultArrayType = "Float"


# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=calculator2)
cellDatatoPointData1.CellDataArraytoprocess = ["gradientMagnitude"]

# create a new 'TTK PointDataSelector'
tTKPointDataSelector1 = TTKPointDataSelector(Input=cellDatatoPointData1)
tTKPointDataSelector1.ScalarFields = ["density", "gradientMagnitude"]
tTKPointDataSelector1.RangeId = [0, 2]

# create a new 'Cell Data to Point Data'
cellDatatoPointData2 = CellDatatoPointData(Input=tTKPointDataSelector1)
cellDatatoPointData2.CellDataArraytoprocess = ["ScalarGradient", "gradientMagnitude"]

# create a new 'Resample To Image'
resampleToImage1 = ResampleToImage(Input=cellDatatoPointData2)
resampleToImage1.SamplingDimensions = [dim, dim, dim]
resampleToImage1.SamplingBounds = [0.0, 176.0, 0.0, 94.0, 0.0, 47.0]

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(Input=resampleToImage1)
tTKScalarFieldSmoother1.ScalarField = ["POINTS", "density"]
tTKScalarFieldSmoother1.IterationNumber = 1

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother2 = TTKScalarFieldSmoother(Input=tTKScalarFieldSmoother1)
tTKScalarFieldSmoother2.ScalarField = ["POINTS", "gradientMagnitude"]
tTKScalarFieldSmoother2.IterationNumber = 10

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer2 = TTKScalarFieldNormalizer(Input=tTKScalarFieldSmoother2)
tTKScalarFieldNormalizer2.ScalarField = ["POINTS", "density"]

# create a new 'TTK ArrayPreconditioning'
tTKArrayPreconditioning1 = TTKArrayPreconditioning(Input=tTKScalarFieldNormalizer2)
tTKArrayPreconditioning1.PointDataArrays = ["density"]

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints2 = TTKScalarFieldCriticalPoints(
    Input=tTKArrayPreconditioning1
)
tTKScalarFieldCriticalPoints2.ScalarField = ["POINTS", "density"]
tTKScalarFieldCriticalPoints2.Backend = "Default generic backend"

# create a new 'Mask Points'
maskPoints2 = MaskPoints(Input=tTKScalarFieldCriticalPoints2)
maskPoints2.OnRatio = 1
maskPoints2.MaximumNumberofPoints = 99999999
maskPoints2.ProportionallyDistributeMaximumNumberOfPoints = 1
maskPoints2.RandomSampling = 1
maskPoints2.RandomSamplingMode = "Random Sampling"
maskPoints2.GenerateVertices = 1
maskPoints2.SingleVertexPerCell = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=maskPoints2)
threshold1.Scalars = ["POINTS", "CriticalType"]
threshold1.LowerThreshold = 1.0
threshold1.UpperThreshold = 1.0

# create a new 'Threshold'
threshold4 = Threshold(Input=threshold1)
threshold4.Scalars = ["POINTS", "IsOnBoundary"]

# create a new 'TTK IntegralLines'
tTKIntegralLines1 = TTKIntegralLines(Domain=tTKArrayPreconditioning1, Seeds=threshold4)
tTKIntegralLines1.ScalarField = ["POINTS", "density"]
tTKIntegralLines1.Direction = "Backward"
tTKIntegralLines1.Vertexidentifierfield = ["POINTS", "CriticalType"]
tTKIntegralLines1.EnableForking = 1

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKIntegralLines1)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=cleantoGrid1)
tTKGeometrySmoother2.IterationNumber = 200

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(
    SourceDataArrays=cellDatatoPointData1, DestinationMesh=tTKGeometrySmoother2
)
resampleWithDataset1.CellLocator = "Static Cell Locator"
resampleWithDataset1.PassCellArrays = 1
resampleWithDataset1.PassPointArrays = 1

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=resampleWithDataset1)
tTKScalarFieldCriticalPoints1.ScalarField = ["POINTS", "gradientMagnitude"]
tTKScalarFieldCriticalPoints1.Backend = "Default generic backend"

UpdatePipeline()

# To save the output to disk, uncomment the two lines below.
#SaveData("integralLines.pvtu", tTKGeometrySmoother2)
#SaveData("criticalPoints.pvtp", tTKScalarFieldCriticalPoints1)

# WARNING: due to a reported ParaView issue, when saving the output to disk in
# MPI mode, pvbatch will execute the pipeline twice in a row (instead of one).
