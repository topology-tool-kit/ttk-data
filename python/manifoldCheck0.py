#!/usr/bin/env python
from paraview.simple import *

# create a new 'XML Unstructured Grid Reader'
manifoldCheck0vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck0.vtu'])

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=manifoldCheck0vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck1 = TTKManifoldCheck(Input=tetrahedralize1)

# create a new 'Mask Points'
maskPoints1 = MaskPoints(Input=tTKManifoldCheck1)
maskPoints1.OnRatio = 1
maskPoints1.MaximumNumberofPoints = 1000
maskPoints1.GenerateVertices = 1
maskPoints1.SingleVertexPerCell = 1

# create a new 'Threshold'
# this extracts non-manifold vertices
threshold1 = Threshold(Input=maskPoints1)
threshold1.Scalars = ['POINTS', 'VertexLinkComponentNumber']
threshold1.LowerThreshold = 2.0
threshold1.UpperThreshold = 2.0

# save the output
SaveData('manifoldCheck0_check.vtu', tTKManifoldCheck1)
SaveData('manifoldCheck0_non_manifold.vtu', threshold1)
