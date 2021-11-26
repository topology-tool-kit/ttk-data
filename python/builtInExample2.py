#### import the simple module from the paraview
from paraview.simple import *

# create a new 'XML Image Data Reader'
example2vti = XMLImageDataReader(FileName=['BuiltInExample2.vti'])
example2vti.PointArrayStatus = ['log(Rho)', 'log(s)']

# create a new 'Contour'
contour2 = Contour(Input=example2vti)
contour2.ContourBy = ['POINTS', 'log(Rho)']
contour2.Isosurfaces = [1.57]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour3 = Contour(Input=example2vti)
contour3.ContourBy = ['POINTS', 'log(s)']
contour3.Isosurfaces = [-0.575]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'TTK ContinuousScatterPlot'
tTKContinuousScatterPlot1 = TTKContinuousScatterPlot(Input=example2vti)
tTKContinuousScatterPlot1.ScalarField1 = ['POINTS', 'log(Rho)']
tTKContinuousScatterPlot1.ScalarField2 = ['POINTS', 'log(s)']

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKContinuousScatterPlot1)
threshold1.Scalars = ['POINTS', 'ValidPointMask']
threshold1.ThresholdRange = [0.1, 1.0]

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField1 = TTKProjectionFromField(Input=contour2)
tTKProjectionFromField1.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField1.VComponent = ['POINTS', 'log(s)']
tTKProjectionFromField1.a3DCoordinates = [None, '']

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=tTKProjectionFromField1)

# create a new 'Tube'
tube1 = Tube(Input=extractEdges1)
tube1.Scalars = ['POINTS', 'log(Rho)']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.02

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField2 = TTKProjectionFromField(Input=contour3)
tTKProjectionFromField2.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField2.VComponent = ['POINTS', 'log(s)']
tTKProjectionFromField2.a3DCoordinates = [None, '']

# create a new 'Extract Edges'
extractEdges2 = ExtractEdges(Input=tTKProjectionFromField2)

# create a new 'Tube'
tube2 = Tube(Input=extractEdges2)
tube2.Scalars = ['POINTS', 'log(Rho)']
tube2.Vectors = ['POINTS', 'Normals']
tube2.Radius = 0.02

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=example2vti)

rangePolygonsCoordinates = [
    [1.89657, -0.278516, 0.0, 2.06003, -0.24493, 0.0, 2.15538, -0.278516, 0.0, 2.21441, -0.416216, 0.0],
    [1.3744, 0.000242441, 0.0, 1.51061, -0.00983316, 0.0, 1.65137, -0.0434185, 0.0, 1.70586, -0.181118, 0.0],
    [1.21547, -0.701691, 0.0, 1.27904, -0.614369, 0.0, 1.51061, -0.607652, 0.0, 1.52878, -1.16853, 0.0, 1.53786, -0.688257, 0.0],
    [-0.310174, -0.325535, 0.0, -0.0150337, -0.124023, 0.0, 0.216538, -0.140816, 0.0, 0.466272, -0.399423, 0.0]
]

polygonTubes = []
fiberSurfaces = []

for coords in rangePolygonsCoordinates:
    # create a new 'Poly Line Source'
    polyLineSource1 = PolyLineSource()
    polyLineSource1.Points = coords
    
    # create a new 'Resample With Dataset'
    resampleWithDataset1 = ResampleWithDataset(SourceDataArrays=tTKContinuousScatterPlot1,
        DestinationMesh=polyLineSource1)
    resampleWithDataset1.CellLocator = 'Static Cell Locator'

    # create a new 'Tetrahedralize'
    tetrahedralize2 = Tetrahedralize(Input=resampleWithDataset1)

    # create a new 'TTK FiberSurface'
    tTKFiberSurface1 = TTKFiberSurface(InputDomain=tetrahedralize1,
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

    # create a new 'Tube'
    tube3 = Tube(Input=extractSurface1)
    tube3.Scalars = ['POINTS', 'Density']
    tube3.Vectors = ['POINTS', '']
    tube3.Radius = 0.03
    
    polygonTubes.append(tube3)

# create a new 'TTK JacobiSet'
tTKJacobiSet1 = TTKJacobiSet(Input=tetrahedralize1)
tTKJacobiSet1.UComponent = ['POINTS', 'log(Rho)']
tTKJacobiSet1.VComponent = ['POINTS', 'log(s)']
tTKJacobiSet1.UOffsetField = ['POINTS', '']
tTKJacobiSet1.VOffsetField = ['POINTS', '']
tTKJacobiSet1.Withedgeidentifiers = 1
tTKJacobiSet1.Withvertexscalars = 1

# create a new 'TTK ProjectionFromField'
tTKProjectionFromField3 = TTKProjectionFromField(Input=tTKJacobiSet1)
tTKProjectionFromField3.UComponent = ['POINTS', 'log(Rho)']
tTKProjectionFromField3.VComponent = ['POINTS', 'log(s)']
tTKProjectionFromField3.a3DCoordinates = [None, '']

# save the output
SaveData('logRhoIsosurfaceAtoms.vtp', contour2)
SaveData('logSIsosurfaceBonds.vtp', contour3)

SaveData('ContinuousScatterPlot.vtu', threshold1)
SaveData('logRhoIsosurfaceRangeProjection.vtp', tube1)
SaveData('logSIsosurfaceRangeProjection.vtp', tube2)
SaveData('OxygenAtomsRangePolygon.vtp', polygonTubes[0])
SaveData('CarbonAtomsRangePolygon.vtp', polygonTubes[1])
SaveData('CovalentBondsRangePolygon.vtp', polygonTubes[2])
SaveData('NonCovalentIntercationSiteRangePolygon.vtp', polygonTubes[3])

SaveData('OxygenAtomsFiberSurface.vtp', fiberSurfaces[0])
SaveData('CarbonAtomsFiberSurface.vtp', fiberSurfaces[1])
SaveData('CovalentBondsFiberSurface.vtp', fiberSurfaces[2])
SaveData('NonCovalentIntercationSiteFiberSurface.vtp', fiberSurfaces[3])

SaveData('JacobiSetRangeProjection.vtu', tTKProjectionFromField3)
