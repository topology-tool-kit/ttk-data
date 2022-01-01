#### import the simple module from the paraview
from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility ===========================================
def ThresholdBetween(threshold, lower, upper):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [lower, upper]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Between"
        threshold.LowerThreshold = lower
        threshold.UpperThreshold = upper
# end of comphatibility ========================================================

# Load the scalar fields using 'XML Image Data Reader'
example2vti = XMLImageDataReader(FileName=['BuiltInExample2.vti'])

### Univariate data analysis using isosurfaces

# create a new 'Contour' for 'log(Rho)' to identify atoms
contour2 = Contour(Input=example2vti)
contour2.ContourBy = ['POINTS', 'log(Rho)']
contour2.Isosurfaces = [1.57]

# create a new 'Contour' for 'log(s)' to identify atoms
contour3 = Contour(Input=example2vti)
contour3.ContourBy = ['POINTS', 'log(s)']
contour3.Isosurfaces = [-0.575]

### Bivariate data analysis using isosurfaces

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot1 = TTKContinuousScatterPlot(Input=example2vti)
tTKContinuousScatterPlot1.ScalarField1 = ['POINTS', 'log(Rho)']
tTKContinuousScatterPlot1.ScalarField2 = ['POINTS', 'log(s)']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKContinuousScatterPlot1)
threshold1.Scalars = ['POINTS', 'ValidPointMask']
ThresholdBetween(threshold1, 0.1, 999999999)

# create a new 'TTK ProjectionFromField' to project the 'log(Rho)' contour onto the range space
tTKProjectionFromField1 = TTKProjectionFromField(Input=contour2)
tTKProjectionFromField1.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField1.VComponent = ['POINTS', 'log(s)']

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=tTKProjectionFromField1)

# create a new 'TTK ProjectionFromField' to project the 'log(s)' contour onto the range space
tTKProjectionFromField2 = TTKProjectionFromField(Input=contour3)
tTKProjectionFromField2.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField2.VComponent = ['POINTS', 'log(s)']

# create a new 'Extract Edges'
extractEdges2 = ExtractEdges(Input=tTKProjectionFromField2)

# Four manually created polylines in the range space to select regions corresponding to 
# Oxygen and carbon atoms, followed by covalent and non-covalent bonds
rangePolygonsCoordinates = [
    [1.89657, -0.278516, 0.0, 2.06003, -0.24493, 0.0, 2.15538, -0.278516, 0.0, 2.21441, -0.416216, 0.0],
    [1.3744, 0.000242441, 0.0, 1.51061, -0.00983316, 0.0, 1.65137, -0.0434185, 0.0, 1.70586, -0.181118, 0.0],
    [1.21547, -0.701691, 0.0, 1.27904, -0.614369, 0.0, 1.51061, -0.607652, 0.0, 1.52878, -1.16853, 0.0, 1.53786, -0.688257, 0.0],
    [-0.310174, -0.325535, 0.0, -0.0150337, -0.124023, 0.0, 0.216538, -0.140816, 0.0, 0.466272, -0.399423, 0.0]
]

# Save the four range space control polygons
polygons = []

# Save the corresponding four fiber surfaces
fiberSurfaces = []

for coords in rangePolygonsCoordinates:
    # create a new 'Poly Line Source'
    polyLineSource1 = PolyLineSource()
    polyLineSource1.Points = coords
    
    # create a new 'Resample With Dataset'
    resampleWithDataset1 = ResampleWithDataset(SourceDataArrays=tTKContinuousScatterPlot1,
        DestinationMesh=polyLineSource1)
        
    # create a new 'Tetrahedralize'
    tetrahedralize2 = Tetrahedralize(Input=resampleWithDataset1)
    
    # create a new 'TTK FiberSurface'
    tTKFiberSurface1 = TTKFiberSurface(InputDomain=example2vti,
        RangePolygon=tetrahedralize2)
    tTKFiberSurface1.DomainUComponent = ['POINTS', 'log(Rho)']
    tTKFiberSurface1.DomainVComponent = ['POINTS', 'log(s)']
    tTKFiberSurface1.PolygonUComponent = ['POINTS', 'log(Rho)']
    tTKFiberSurface1.PolygonVComponent = ['POINTS', 'log(s)']
    tTKFiberSurface1.WithPointMerging = 1

    # create a new 'Generate Surface Normals'
    generateSurfaceNormals1 = GenerateSurfaceNormals(Input=tTKFiberSurface1)
    
    fiberSurfaces.append(generateSurfaceNormals1)

    # create a new 'Extract Surface'
    extractSurface1 = ExtractSurface(Input=resampleWithDataset1)
    
    polygons.append(extractSurface1)

# compute 'TTK JacobiSet' for the bivariate data
tTKJacobiSet1 = TTKJacobiSet(Input=example2vti)
tTKJacobiSet1.UComponent = ['POINTS', 'log(Rho)']
tTKJacobiSet1.VComponent = ['POINTS', 'log(s)']
tTKJacobiSet1.Withedgeidentifiers = 1
tTKJacobiSet1.Withvertexscalars = 1

# project the Jacobi set onto the range space using 'TTK ProjectionFromField'
tTKProjectionFromField3 = TTKProjectionFromField(Input=tTKJacobiSet1)
tTKProjectionFromField3.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField3.VComponent = ['POINTS', 'log(s)']

# save the output
SaveData('logRhoIsosurfaceAtoms.vtp', contour2)
SaveData('logSIsosurfaceBonds.vtp', contour3)

SaveData('ContinuousScatterPlot.vtu', threshold1)
SaveData('logRhoIsosurfaceRangeProjection.vtp', extractEdges1)
SaveData('logSIsosurfaceRangeProjection.vtp', extractEdges2)
SaveData('OxygenAtomsRangePolygon.vtp', polygons[0])
SaveData('CarbonAtomsRangePolygon.vtp', polygons[1])
SaveData('CovalentBondsRangePolygon.vtp', polygons[2])
SaveData('NonCovalentIntercationSiteRangePolygon.vtp', polygons[3])

SaveData('OxygenAtomsFiberSurface.vtp', fiberSurfaces[0])
SaveData('CarbonAtomsFiberSurface.vtp', fiberSurfaces[1])
SaveData('CovalentBondsFiberSurface.vtp', fiberSurfaces[2])
SaveData('NonCovalentIntercationSiteFiberSurface.vtp', fiberSurfaces[3])

SaveData('JacobiSetRangeProjection.vtu', tTKProjectionFromField3)
