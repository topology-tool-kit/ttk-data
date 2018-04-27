# state file generated using paraview version 5.5.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.5.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [825, 611]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [56.9999965503812, 57.5000003650784, 66.4999965578318]
renderView1.StereoType = 0
renderView1.CameraPosition = [197.265991768346, 3.14460701845322, -7.24021078739247]
renderView1.CameraFocalPoint = [-4.1661574058079, 83.8596302709368, 108.856696124015]
renderView1.CameraViewUp = [-0.285272946444876, -0.944686405261375, 0.161823798438305]
renderView1.CameraParallelScale = 138.561432248195
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [825, 610]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [56.9999965503812, 57.5000003650784, 66.4999965578318]
renderView2.StereoType = 0
renderView2.CameraPosition = [197.265991768346, 3.14460701845322, -7.24021078739247]
renderView2.CameraFocalPoint = [-4.1661574058079, 83.8596302709368, 108.856696124015]
renderView2.CameraViewUp = [-0.285272946444876, -0.944686405261375, 0.161823798438305]
renderView2.CameraParallelScale = 138.561432248195
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [825, 610]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [56.9999965503812, 57.5000003650784, 66.4999965578318]
renderView3.StereoType = 0
renderView3.CameraPosition = [197.265991768346, 3.14460701845322, -7.24021078739247]
renderView3.CameraFocalPoint = [-4.1661574058079, 83.8596302709368, 108.856696124015]
renderView3.CameraViewUp = [-0.285272946444876, -0.944686405261375, 0.161823798438305]
renderView3.CameraParallelScale = 138.561432248195
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [825, 611]
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [56.9999965503812, 57.5000003650784, 66.4999965578318]
renderView4.StereoType = 0
renderView4.CameraPosition = [197.265991768346, 3.14460701845322, -7.24021078739247]
renderView4.CameraFocalPoint = [-4.1661574058079, 83.8596302709368, 108.856696124015]
renderView4.CameraViewUp = [-0.285272946444876, -0.944686405261375, 0.161823798438305]
renderView4.CameraParallelScale = 138.561432248195
renderView4.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.XTitleFontFile = ''
renderView4.AxesGrid.YTitleFontFile = ''
renderView4.AxesGrid.ZTitleFontFile = ''
renderView4.AxesGrid.XLabelFontFile = ''
renderView4.AxesGrid.YLabelFontFile = ''
renderView4.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
builtInExamplevti = XMLImageDataReader(FileName=['BuiltInExample2.vti'])
builtInExamplevti.PointArrayStatus = ['Rho', 'log(Rho)', 'log(s)']

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(Input=builtInExamplevti)
computeDerivatives1.Scalars = ['POINTS', 'log(Rho)']
computeDerivatives1.Vectors = [None, '']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=builtInExamplevti)
tTKMorseSmaleComplex1.ScalarField = 'log(Rho)'
tTKMorseSmaleComplex1.InputOffsetField = ''
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.Descending2Separatrices = 1

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,2))
threshold5.Scalars = ['CELLS', 'CriticalPointIndex']
threshold5.ThresholdRange = [2.0, 2.0]

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,2))
threshold4.Scalars = ['CELLS', 'CriticalPointIndex']
threshold4.ThresholdRange = [1.0, 1.0]

# create a new 'Clean to Grid'
cleantoGrid2 = CleantoGrid(Input=threshold4)

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=cleantoGrid2)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tetrahedralize1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint2.Radius = 3.0

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKSphereFromPoint2)
threshold3.Scalars = ['POINTS', 'CellDimension']
threshold3.ThresholdRange = [3.0, 3.0]

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold1 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold1.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'Threshold'
threshold2 = Threshold(Input=threshold1)
threshold2.Scalars = ['CELLS', 'CriticalPointIndex']
threshold2.ThresholdRange = [2.0, 2.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint1.Radius = 1.5

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 50

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=tTKGeometrySmoother1)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cleantoGrid1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 1.25

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=extractSurface2)
tTKGeometrySmoother2.IterationNumber = 20

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=computeDerivatives1,
    SeedType='Point Source')
streamTracer1.Vectors = ['CELLS', 'ScalarGradient']
streamTracer1.IntegrationDirection = 'FORWARD'
streamTracer1.MaximumStreamlineLength = 133.0

# init the 'Point Source' selected for 'SeedType'
streamTracer1.SeedType.Center = [57.0177693769277, 35.7637631216166, 73.6417192169949]
streamTracer1.SeedType.Radius = 0.5

# create a new 'Tube'
tube4 = Tube(Input=streamTracer1)
tube4.Scalars = ['POINTS', 'log(s)']
tube4.Vectors = ['POINTS', 'Normals']

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=computeDerivatives1,
    SeedType='Point Source')
streamTracer2.Vectors = ['CELLS', 'ScalarGradient']
streamTracer2.IntegrationDirection = 'FORWARD'
streamTracer2.MaximumStreamlineLength = 133.0

# init the 'Point Source' selected for 'SeedType'
streamTracer2.SeedType.Center = [56.9955364629553, 35.7177590290303, 76.44491140625]
streamTracer2.SeedType.Radius = 0.5

# create a new 'Tube'
tube3 = Tube(Input=streamTracer2)
tube3.Scalars = ['POINTS', 'IntegrationTime']
tube3.Vectors = ['POINTS', 'Normals']

# create a new 'Threshold'
threshold8 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold8.Scalars = ['CELLS', 'CriticalPointIndex']
threshold8.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold9 = Threshold(Input=threshold8)
threshold9.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'Threshold'
threshold10 = Threshold(Input=threshold9)
threshold10.Scalars = ['CELLS', 'SeparatrixId']
threshold10.ThresholdRange = [77.0, 78.0]

# create a new 'Threshold'
threshold11 = Threshold(Input=threshold9)
threshold11.Scalars = ['CELLS', 'SeparatrixId']
threshold11.ThresholdRange = [78.0, 80.0]

# create a new 'Append Datasets'
appendDatasets1 = AppendDatasets(Input=[threshold10, threshold11])

# create a new 'Clean to Grid'
cleantoGrid4 = CleantoGrid(Input=appendDatasets1)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother4 = TTKGeometrySmoother(Input=cleantoGrid4)
tTKGeometrySmoother4.IterationNumber = 10

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKGeometrySmoother4)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Vectors = [None, '']
tube2.Radius = 0.75

# create a new 'Point Source'
pointSource1 = PointSource()
pointSource1.Center = [57.0177693769277, 35.7177590290303, 74.44491140625]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=pointSource1)
tTKSphereFromPoint3.Radius = 3.0

# create a new 'Threshold'
threshold6 = Threshold(Input=threshold5)
threshold6.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold6.ThresholdRange = [4.0, 4.0]

# create a new 'Threshold'
threshold7 = Threshold(Input=threshold6)
threshold7.Scalars = ['CELLS', 'SeparatrixId']
threshold7.ThresholdRange = [22.0, 22.0]

# create a new 'Clean to Grid'
cleantoGrid3 = CleantoGrid(Input=threshold7)

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=cleantoGrid3)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=tetrahedralize2)
tTKGeometrySmoother3.IterationNumber = 20

# create a new 'Contour'
contour1 = Contour(Input=builtInExamplevti)
contour1.ContourBy = ['POINTS', 'log(Rho)']
contour1.ComputeScalars = 1
contour1.Isosurfaces = [1.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1Display = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView1)

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Outline'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'log(s)'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex1Display.ScaleFactor = 13.3
tTKMorseSmaleComplex1Display.SelectScaleArray = 'log(s)'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.SetScaleArray = [None, '']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = [None, '']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display.ScalarOpacityUnitDistance = 1.74099266343913
tTKMorseSmaleComplex1Display.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex1Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5078125, 0.917647, 0.941176, 0.788235, 3.015625, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.LookupTable = cellDimensionLUT
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint1Display.ScaleFactor = 13.7
tTKSphereFromPoint1Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GaussianRadius = 6.85
tTKSphereFromPoint1Display.CustomShader = ''
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint1Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from contour1
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface With Edges'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.Opacity = 0.15
contour1Display.Specular = 1.0
contour1Display.OSPRayScaleArray = 'log(Rho)'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 11.046505355835
contour1Display.SelectScaleArray = 'log(Rho)'
contour1Display.GlyphType = 'Arrow'
contour1Display.GaussianRadius = 5.52325267791748
contour1Display.CustomShader = ''
contour1Display.SetScaleArray = ['POINTS', 'log(Rho)']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'log(Rho)']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 8.49540901184082
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GaussianRadius = 4.24770450592041
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display.DataAxesGrid.XTitleFontFile = ''
tube1Display.DataAxesGrid.YTitleFontFile = ''
tube1Display.DataAxesGrid.ZTitleFontFile = ''
tube1Display.DataAxesGrid.XLabelFontFile = ''
tube1Display.DataAxesGrid.YLabelFontFile = ''
tube1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold3
threshold3Display = Show(threshold3, renderView1)

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.015625, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['POINTS', 'CellDimension']
threshold3Display.LookupTable = cellDimensionLUT
threshold3Display.Specular = 1.0
threshold3Display.OSPRayScaleArray = 'CellDimension'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'CellDimension'
threshold3Display.ScaleFactor = 8.97187900543213
threshold3Display.SelectScaleArray = 'CellDimension'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GaussianRadius = 4.48593950271606
threshold3Display.CustomShader = ''
threshold3Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.SelectionCellLabelFontFile = ''
threshold3Display.SelectionPointLabelFontFile = ''
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = cellDimensionPWF
threshold3Display.ScalarOpacityUnitDistance = 6.96479929698372

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold3Display.DataAxesGrid.XTitleFontFile = ''
threshold3Display.DataAxesGrid.YTitleFontFile = ''
threshold3Display.DataAxesGrid.ZTitleFontFile = ''
threshold3Display.DataAxesGrid.XLabelFontFile = ''
threshold3Display.DataAxesGrid.YLabelFontFile = ''
threshold3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold3Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold3Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold3Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display = Show(tube2, renderView1)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.DiffuseColor = [0.36078431372549, 0.36078431372549, 0.36078431372549]
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'CellDimension'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'CellDimension'
tube2Display.ScaleFactor = 11.6271851181984
tube2Display.SelectScaleArray = 'CellDimension'
tube2Display.GlyphType = 'Arrow'
tube2Display.GaussianRadius = 5.8135925590992
tube2Display.CustomShader = ''
tube2Display.SetScaleArray = ['POINTS', 'CellDimension']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'CellDimension']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.SelectionCellLabelFontFile = ''
tube2Display.SelectionPointLabelFontFile = ''
tube2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display.DataAxesGrid.XTitleFontFile = ''
tube2Display.DataAxesGrid.YTitleFontFile = ''
tube2Display.DataAxesGrid.ZTitleFontFile = ''
tube2Display.DataAxesGrid.XLabelFontFile = ''
tube2Display.DataAxesGrid.YLabelFontFile = ''
tube2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from computeDerivatives1
computeDerivatives1Display = Show(computeDerivatives1, renderView1)

# get color transfer function/color map for 'logs'
logsLUT = GetColorTransferFunction('logs')
logsLUT.RGBPoints = [-1.91412099848454, 0.0, 0.431373, 0.0, -0.702321887016296, 0.00784313725490196, 0.435294117647059, 0.00784313725490196, -0.529207766056061, 0.917647, 0.941176, 0.788235, -0.333011716604233, 0.113725490196078, 0.231372549019608, 0.611764705882353, 1.70973540651281, 0.0, 0.129412, 0.584314]
logsLUT.ColorSpace = 'RGB'
logsLUT.AboveRangeColor = [1.0, 1.0, 1.0]
logsLUT.NanColor = [0.0, 0.0, 0.0]
logsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'logs'
logsPWF = GetOpacityTransferFunction('logs')
logsPWF.Points = [-1.91412099848454, 0.0, 0.5, 0.0, -0.956222653388977, 0.0, 0.5, 0.0, -0.748485684394836, 0.0657894760370255, 0.5, 0.0, -0.575371503829956, 0.0, 0.5, 0.0, -0.37917548418045, 0.085526317358017, 0.5, 0.0, -0.14835659526702, 0.0, 0.5, 0.0, 1.10960627685938, 0.0, 0.5, 0.0, 1.70973540651281, 0.0, 0.5, 0.0]
logsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
computeDerivatives1Display.Representation = 'Volume'
computeDerivatives1Display.ColorArrayName = ['POINTS', 'log(s)']
computeDerivatives1Display.LookupTable = logsLUT
computeDerivatives1Display.OSPRayScaleArray = 'log(s)'
computeDerivatives1Display.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display.SelectOrientationVectors = 'ScalarGradient'
computeDerivatives1Display.ScaleFactor = 13.3
computeDerivatives1Display.SelectScaleArray = 'log(s)'
computeDerivatives1Display.GlyphType = 'Arrow'
computeDerivatives1Display.SetScaleArray = [None, '']
computeDerivatives1Display.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.OpacityArray = [None, '']
computeDerivatives1Display.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display.SelectionCellLabelFontFile = ''
computeDerivatives1Display.SelectionPointLabelFontFile = ''
computeDerivatives1Display.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display.ScalarOpacityUnitDistance = 1.74099266343913
computeDerivatives1Display.ScalarOpacityFunction = logsPWF
computeDerivatives1Display.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
computeDerivatives1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
computeDerivatives1Display.DataAxesGrid.XTitleFontFile = ''
computeDerivatives1Display.DataAxesGrid.YTitleFontFile = ''
computeDerivatives1Display.DataAxesGrid.ZTitleFontFile = ''
computeDerivatives1Display.DataAxesGrid.XLabelFontFile = ''
computeDerivatives1Display.DataAxesGrid.YLabelFontFile = ''
computeDerivatives1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
computeDerivatives1Display.PolarAxes.PolarAxisTitleFontFile = ''
computeDerivatives1Display.PolarAxes.PolarAxisLabelFontFile = ''
computeDerivatives1Display.PolarAxes.LastRadialAxisTextFontFile = ''
computeDerivatives1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from builtInExamplevti
builtInExamplevtiDisplay = Show(builtInExamplevti, renderView2)

# get color transfer function/color map for 'Rho'
rhoLUT = GetColorTransferFunction('Rho')
rhoLUT.RGBPoints = [3.25430009979755e-05, 0.0, 0.129412, 0.584314, 8411.5000162715, 0.917647, 0.941176, 0.788235, 16823.0, 0.0, 0.431373, 0.0]
rhoLUT.ColorSpace = 'RGB'
rhoLUT.AboveRangeColor = [1.0, 1.0, 1.0]
rhoLUT.NanColor = [0.0, 0.0, 0.0]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Rho'
rhoPWF = GetOpacityTransferFunction('Rho')
rhoPWF.Points = [3.25430009979755e-05, 0.0, 0.5, 0.0, 16823.0, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
builtInExamplevtiDisplay.Representation = 'Outline'
builtInExamplevtiDisplay.ColorArrayName = ['POINTS', 'Rho']
builtInExamplevtiDisplay.LookupTable = rhoLUT
builtInExamplevtiDisplay.OSPRayScaleArray = 'log(s)'
builtInExamplevtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay.SelectOrientationVectors = 'None'
builtInExamplevtiDisplay.ScaleFactor = 13.3
builtInExamplevtiDisplay.SelectScaleArray = 'log(s)'
builtInExamplevtiDisplay.GlyphType = 'Arrow'
builtInExamplevtiDisplay.SetScaleArray = [None, '']
builtInExamplevtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay.OpacityArray = [None, '']
builtInExamplevtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
builtInExamplevtiDisplay.SelectionCellLabelFontFile = ''
builtInExamplevtiDisplay.SelectionPointLabelFontFile = ''
builtInExamplevtiDisplay.PolarAxes = 'PolarAxesRepresentation'
builtInExamplevtiDisplay.ScalarOpacityUnitDistance = 1.74099266343913
builtInExamplevtiDisplay.ScalarOpacityFunction = rhoPWF
builtInExamplevtiDisplay.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
builtInExamplevtiDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
builtInExamplevtiDisplay.DataAxesGrid.XTitleFontFile = ''
builtInExamplevtiDisplay.DataAxesGrid.YTitleFontFile = ''
builtInExamplevtiDisplay.DataAxesGrid.ZTitleFontFile = ''
builtInExamplevtiDisplay.DataAxesGrid.XLabelFontFile = ''
builtInExamplevtiDisplay.DataAxesGrid.YLabelFontFile = ''
builtInExamplevtiDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
builtInExamplevtiDisplay.PolarAxes.PolarAxisTitleFontFile = ''
builtInExamplevtiDisplay.PolarAxes.PolarAxisLabelFontFile = ''
builtInExamplevtiDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
builtInExamplevtiDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from contour1
contour1Display_1 = Show(contour1, renderView2)

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface With Edges'
contour1Display_1.ColorArrayName = ['POINTS', '']
contour1Display_1.Opacity = 0.15
contour1Display_1.Specular = 1.0
contour1Display_1.OSPRayScaleArray = 'log(Rho)'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = 11.046505355835
contour1Display_1.SelectScaleArray = 'log(Rho)'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GaussianRadius = 5.52325267791748
contour1Display_1.CustomShader = ''
contour1Display_1.SetScaleArray = ['POINTS', 'log(Rho)']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = ['POINTS', 'log(Rho)']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.SelectionCellLabelFontFile = ''
contour1Display_1.SelectionPointLabelFontFile = ''
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display_1.DataAxesGrid.XTitleFontFile = ''
contour1Display_1.DataAxesGrid.YTitleFontFile = ''
contour1Display_1.DataAxesGrid.ZTitleFontFile = ''
contour1Display_1.DataAxesGrid.XLabelFontFile = ''
contour1Display_1.DataAxesGrid.YLabelFontFile = ''
contour1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold3
threshold3Display_1 = Show(threshold3, renderView2)

# trace defaults for the display properties.
threshold3Display_1.Representation = 'Surface'
threshold3Display_1.ColorArrayName = ['POINTS', 'CellDimension']
threshold3Display_1.LookupTable = cellDimensionLUT
threshold3Display_1.Specular = 1.0
threshold3Display_1.OSPRayScaleArray = 'CellDimension'
threshold3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display_1.SelectOrientationVectors = 'CellDimension'
threshold3Display_1.ScaleFactor = 8.97187900543213
threshold3Display_1.SelectScaleArray = 'CellDimension'
threshold3Display_1.GlyphType = 'Arrow'
threshold3Display_1.GaussianRadius = 4.48593950271606
threshold3Display_1.CustomShader = ''
threshold3Display_1.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display_1.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display_1.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display_1.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display_1.SelectionCellLabelFontFile = ''
threshold3Display_1.SelectionPointLabelFontFile = ''
threshold3Display_1.PolarAxes = 'PolarAxesRepresentation'
threshold3Display_1.ScalarOpacityFunction = cellDimensionPWF
threshold3Display_1.ScalarOpacityUnitDistance = 6.96479929698372

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold3Display_1.DataAxesGrid.XTitleFontFile = ''
threshold3Display_1.DataAxesGrid.YTitleFontFile = ''
threshold3Display_1.DataAxesGrid.ZTitleFontFile = ''
threshold3Display_1.DataAxesGrid.XLabelFontFile = ''
threshold3Display_1.DataAxesGrid.YLabelFontFile = ''
threshold3Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold3Display_1.PolarAxes.PolarAxisTitleFontFile = ''
threshold3Display_1.PolarAxes.PolarAxisLabelFontFile = ''
threshold3Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
threshold3Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display_1 = Show(tube1, renderView2)

# trace defaults for the display properties.
tube1Display_1.Representation = 'Surface'
tube1Display_1.ColorArrayName = [None, '']
tube1Display_1.Specular = 1.0
tube1Display_1.OSPRayScaleArray = 'CellDimension'
tube1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display_1.SelectOrientationVectors = 'CellDimension'
tube1Display_1.ScaleFactor = 8.65759143829346
tube1Display_1.SelectScaleArray = 'CellDimension'
tube1Display_1.GlyphType = 'Arrow'
tube1Display_1.GaussianRadius = 4.32879571914673
tube1Display_1.CustomShader = ''
tube1Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display_1.OpacityArray = ['POINTS', 'CellDimension']
tube1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube1Display_1.SelectionCellLabelFontFile = ''
tube1Display_1.SelectionPointLabelFontFile = ''
tube1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display_1.DataAxesGrid.XTitleFontFile = ''
tube1Display_1.DataAxesGrid.YTitleFontFile = ''
tube1Display_1.DataAxesGrid.ZTitleFontFile = ''
tube1Display_1.DataAxesGrid.XLabelFontFile = ''
tube1Display_1.DataAxesGrid.YLabelFontFile = ''
tube1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display_1 = Show(tube2, renderView2)

# trace defaults for the display properties.
tube2Display_1.Representation = 'Surface'
tube2Display_1.ColorArrayName = [None, '']
tube2Display_1.DiffuseColor = [0.36078431372549, 0.36078431372549, 0.36078431372549]
tube2Display_1.Specular = 1.0
tube2Display_1.OSPRayScaleArray = 'CellDimension'
tube2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display_1.SelectOrientationVectors = 'CellDimension'
tube2Display_1.ScaleFactor = 11.5992790222168
tube2Display_1.SelectScaleArray = 'CellDimension'
tube2Display_1.GlyphType = 'Arrow'
tube2Display_1.GaussianRadius = 5.7996395111084
tube2Display_1.CustomShader = ''
tube2Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tube2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display_1.OpacityArray = ['POINTS', 'CellDimension']
tube2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tube2Display_1.SelectionCellLabelFontFile = ''
tube2Display_1.SelectionPointLabelFontFile = ''
tube2Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display_1.DataAxesGrid.XTitleFontFile = ''
tube2Display_1.DataAxesGrid.YTitleFontFile = ''
tube2Display_1.DataAxesGrid.ZTitleFontFile = ''
tube2Display_1.DataAxesGrid.XLabelFontFile = ''
tube2Display_1.DataAxesGrid.YLabelFontFile = ''
tube2Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display_1 = Show(tTKSphereFromPoint1, renderView2)

# trace defaults for the display properties.
tTKSphereFromPoint1Display_1.Representation = 'Surface'
tTKSphereFromPoint1Display_1.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_1.LookupTable = cellDimensionLUT
tTKSphereFromPoint1Display_1.Specular = 1.0
tTKSphereFromPoint1Display_1.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_1.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint1Display_1.ScaleFactor = 13.5
tTKSphereFromPoint1Display_1.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_1.GlyphType = 'Arrow'
tTKSphereFromPoint1Display_1.GaussianRadius = 6.75
tTKSphereFromPoint1Display_1.CustomShader = ''
tTKSphereFromPoint1Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_1.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display_1.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display_1.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint1Display_1.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint1Display_1.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint1Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint1Display_1.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint1Display_1.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKGeometrySmoother3
tTKGeometrySmoother3Display = Show(tTKGeometrySmoother3, renderView2)

# trace defaults for the display properties.
tTKGeometrySmoother3Display.Representation = 'Surface'
tTKGeometrySmoother3Display.ColorArrayName = [None, '']
tTKGeometrySmoother3Display.DiffuseColor = [0.0, 0.431372549019608, 0.0]
tTKGeometrySmoother3Display.Opacity = 0.5
tTKGeometrySmoother3Display.Specular = 1.0
tTKGeometrySmoother3Display.OSPRayScaleArray = 'CriticalPointIndex'
tTKGeometrySmoother3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother3Display.ScaleFactor = 12.9609578847885
tTKGeometrySmoother3Display.SelectScaleArray = 'None'
tTKGeometrySmoother3Display.GlyphType = 'Arrow'
tTKGeometrySmoother3Display.GaussianRadius = 6.48047894239426
tTKGeometrySmoother3Display.CustomShader = ''
tTKGeometrySmoother3Display.SetScaleArray = [None, '']
tTKGeometrySmoother3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.OpacityArray = [None, '']
tTKGeometrySmoother3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother3Display.SelectionCellLabelFontFile = ''
tTKGeometrySmoother3Display.SelectionPointLabelFontFile = ''
tTKGeometrySmoother3Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother3Display.ScalarOpacityUnitDistance = 5.69618600387321

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKGeometrySmoother3Display.DataAxesGrid.XTitleFontFile = ''
tTKGeometrySmoother3Display.DataAxesGrid.YTitleFontFile = ''
tTKGeometrySmoother3Display.DataAxesGrid.ZTitleFontFile = ''
tTKGeometrySmoother3Display.DataAxesGrid.XLabelFontFile = ''
tTKGeometrySmoother3Display.DataAxesGrid.YLabelFontFile = ''
tTKGeometrySmoother3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKGeometrySmoother3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKGeometrySmoother3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKGeometrySmoother3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKGeometrySmoother3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from computeDerivatives1
computeDerivatives1Display_1 = Show(computeDerivatives1, renderView2)

# trace defaults for the display properties.
computeDerivatives1Display_1.Representation = 'Volume'
computeDerivatives1Display_1.ColorArrayName = ['POINTS', 'log(s)']
computeDerivatives1Display_1.LookupTable = logsLUT
computeDerivatives1Display_1.OSPRayScaleArray = 'log(s)'
computeDerivatives1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display_1.SelectOrientationVectors = 'ScalarGradient'
computeDerivatives1Display_1.ScaleFactor = 13.3
computeDerivatives1Display_1.SelectScaleArray = 'log(s)'
computeDerivatives1Display_1.GlyphType = 'Arrow'
computeDerivatives1Display_1.SetScaleArray = [None, '']
computeDerivatives1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_1.OpacityArray = [None, '']
computeDerivatives1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_1.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display_1.SelectionCellLabelFontFile = ''
computeDerivatives1Display_1.SelectionPointLabelFontFile = ''
computeDerivatives1Display_1.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display_1.ScalarOpacityUnitDistance = 1.74099266343913
computeDerivatives1Display_1.ScalarOpacityFunction = logsPWF
computeDerivatives1Display_1.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
computeDerivatives1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
computeDerivatives1Display_1.DataAxesGrid.XTitleFontFile = ''
computeDerivatives1Display_1.DataAxesGrid.YTitleFontFile = ''
computeDerivatives1Display_1.DataAxesGrid.ZTitleFontFile = ''
computeDerivatives1Display_1.DataAxesGrid.XLabelFontFile = ''
computeDerivatives1Display_1.DataAxesGrid.YLabelFontFile = ''
computeDerivatives1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
computeDerivatives1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
computeDerivatives1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
computeDerivatives1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
computeDerivatives1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView2)

# get color transfer function/color map for 'IntegrationTime'
integrationTimeLUT = GetColorTransferFunction('IntegrationTime')
integrationTimeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 352.253347569038, 0.917647, 0.941176, 0.788235, 704.506695138077, 0.0, 0.431373, 0.0]
integrationTimeLUT.ColorSpace = 'RGB'
integrationTimeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
integrationTimeLUT.NanColor = [0.0, 0.0, 0.0]
integrationTimeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'IntegrationTime']
streamTracer1Display.LookupTable = integrationTimeLUT
streamTracer1Display.Specular = 1.0
streamTracer1Display.OSPRayScaleArray = 'log(s)'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 2.95543022155762
streamTracer1Display.SelectScaleArray = 'log(s)'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GaussianRadius = 1.47771511077881
streamTracer1Display.CustomShader = ''
streamTracer1Display.SetScaleArray = ['POINTS', 'log(s)']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'log(s)']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.SelectionCellLabelFontFile = ''
streamTracer1Display.SelectionPointLabelFontFile = ''
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer1Display.DataAxesGrid.XTitleFontFile = ''
streamTracer1Display.DataAxesGrid.YTitleFontFile = ''
streamTracer1Display.DataAxesGrid.ZTitleFontFile = ''
streamTracer1Display.DataAxesGrid.XLabelFontFile = ''
streamTracer1Display.DataAxesGrid.YLabelFontFile = ''
streamTracer1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer1Display.PolarAxes.PolarAxisTitleFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisLabelFontFile = ''
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFile = ''
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from streamTracer2
streamTracer2Display = Show(streamTracer2, renderView2)

# trace defaults for the display properties.
streamTracer2Display.Representation = 'Surface'
streamTracer2Display.ColorArrayName = ['POINTS', 'IntegrationTime']
streamTracer2Display.LookupTable = integrationTimeLUT
streamTracer2Display.Specular = 1.0
streamTracer2Display.OSPRayScaleArray = 'log(s)'
streamTracer2Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer2Display.SelectOrientationVectors = 'Normals'
streamTracer2Display.ScaleFactor = 3.05943222045898
streamTracer2Display.SelectScaleArray = 'log(s)'
streamTracer2Display.GlyphType = 'Arrow'
streamTracer2Display.GaussianRadius = 1.52971611022949
streamTracer2Display.CustomShader = ''
streamTracer2Display.SetScaleArray = ['POINTS', 'log(s)']
streamTracer2Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer2Display.OpacityArray = ['POINTS', 'log(s)']
streamTracer2Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer2Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer2Display.SelectionCellLabelFontFile = ''
streamTracer2Display.SelectionPointLabelFontFile = ''
streamTracer2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer2Display.DataAxesGrid.XTitleFontFile = ''
streamTracer2Display.DataAxesGrid.YTitleFontFile = ''
streamTracer2Display.DataAxesGrid.ZTitleFontFile = ''
streamTracer2Display.DataAxesGrid.XLabelFontFile = ''
streamTracer2Display.DataAxesGrid.YLabelFontFile = ''
streamTracer2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer2Display.PolarAxes.PolarAxisTitleFontFile = ''
streamTracer2Display.PolarAxes.PolarAxisLabelFontFile = ''
streamTracer2Display.PolarAxes.LastRadialAxisTextFontFile = ''
streamTracer2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView2)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = [None, '']
tTKSphereFromPoint3Display.DiffuseColor = [0.0, 0.0, 0.0]
tTKSphereFromPoint3Display.Opacity = 0.5
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint3Display.ScaleFactor = 0.6
tTKSphereFromPoint3Display.SelectScaleArray = 'None'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GaussianRadius = 0.3
tTKSphereFromPoint3Display.CustomShader = ''
tTKSphereFromPoint3Display.SetScaleArray = [None, '']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = [None, '']
tTKSphereFromPoint3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint3Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint3Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint3Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from builtInExamplevti
builtInExamplevtiDisplay_1 = Show(builtInExamplevti, renderView3)

# trace defaults for the display properties.
builtInExamplevtiDisplay_1.Representation = 'Outline'
builtInExamplevtiDisplay_1.ColorArrayName = ['POINTS', '']
builtInExamplevtiDisplay_1.OSPRayScaleArray = 'log(s)'
builtInExamplevtiDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_1.SelectOrientationVectors = 'None'
builtInExamplevtiDisplay_1.ScaleFactor = 13.3
builtInExamplevtiDisplay_1.SelectScaleArray = 'log(s)'
builtInExamplevtiDisplay_1.GlyphType = 'Arrow'
builtInExamplevtiDisplay_1.SetScaleArray = [None, '']
builtInExamplevtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_1.OpacityArray = [None, '']
builtInExamplevtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
builtInExamplevtiDisplay_1.SelectionCellLabelFontFile = ''
builtInExamplevtiDisplay_1.SelectionPointLabelFontFile = ''
builtInExamplevtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
builtInExamplevtiDisplay_1.ScalarOpacityUnitDistance = 1.74099266343913
builtInExamplevtiDisplay_1.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
builtInExamplevtiDisplay_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
builtInExamplevtiDisplay_1.DataAxesGrid.XTitleFontFile = ''
builtInExamplevtiDisplay_1.DataAxesGrid.YTitleFontFile = ''
builtInExamplevtiDisplay_1.DataAxesGrid.ZTitleFontFile = ''
builtInExamplevtiDisplay_1.DataAxesGrid.XLabelFontFile = ''
builtInExamplevtiDisplay_1.DataAxesGrid.YLabelFontFile = ''
builtInExamplevtiDisplay_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
builtInExamplevtiDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
builtInExamplevtiDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
builtInExamplevtiDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
builtInExamplevtiDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display = Show(tTKGeometrySmoother2, renderView3)

# trace defaults for the display properties.
tTKGeometrySmoother2Display.Representation = 'Surface'
tTKGeometrySmoother2Display.ColorArrayName = [None, '']
tTKGeometrySmoother2Display.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
tTKGeometrySmoother2Display.Specular = 1.0
tTKGeometrySmoother2Display.OSPRayScaleArray = 'CriticalPointIndex'
tTKGeometrySmoother2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display.ScaleFactor = 13.0726513981819
tTKGeometrySmoother2Display.SelectScaleArray = 'None'
tTKGeometrySmoother2Display.GlyphType = 'Arrow'
tTKGeometrySmoother2Display.GaussianRadius = 6.53632569909096
tTKGeometrySmoother2Display.CustomShader = ''
tTKGeometrySmoother2Display.SetScaleArray = [None, '']
tTKGeometrySmoother2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.OpacityArray = [None, '']
tTKGeometrySmoother2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display.SelectionCellLabelFontFile = ''
tTKGeometrySmoother2Display.SelectionPointLabelFontFile = ''
tTKGeometrySmoother2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKGeometrySmoother2Display.DataAxesGrid.XTitleFontFile = ''
tTKGeometrySmoother2Display.DataAxesGrid.YTitleFontFile = ''
tTKGeometrySmoother2Display.DataAxesGrid.ZTitleFontFile = ''
tTKGeometrySmoother2Display.DataAxesGrid.XLabelFontFile = ''
tTKGeometrySmoother2Display.DataAxesGrid.YLabelFontFile = ''
tTKGeometrySmoother2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKGeometrySmoother2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKGeometrySmoother2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKGeometrySmoother2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKGeometrySmoother2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from contour1
contour1Display_2 = Show(contour1, renderView3)

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface With Edges'
contour1Display_2.ColorArrayName = ['POINTS', '']
contour1Display_2.Opacity = 0.15
contour1Display_2.Specular = 1.0
contour1Display_2.OSPRayScaleArray = 'log(Rho)'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = 11.046505355835
contour1Display_2.SelectScaleArray = 'log(Rho)'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GaussianRadius = 5.52325267791748
contour1Display_2.CustomShader = ''
contour1Display_2.SetScaleArray = ['POINTS', 'log(Rho)']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = ['POINTS', 'log(Rho)']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.SelectionCellLabelFontFile = ''
contour1Display_2.SelectionPointLabelFontFile = ''
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_2.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_2.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display_2.DataAxesGrid.XTitleFontFile = ''
contour1Display_2.DataAxesGrid.YTitleFontFile = ''
contour1Display_2.DataAxesGrid.ZTitleFontFile = ''
contour1Display_2.DataAxesGrid.XLabelFontFile = ''
contour1Display_2.DataAxesGrid.YLabelFontFile = ''
contour1Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold3
threshold3Display_2 = Show(threshold3, renderView3)

# trace defaults for the display properties.
threshold3Display_2.Representation = 'Surface'
threshold3Display_2.ColorArrayName = ['POINTS', 'CellDimension']
threshold3Display_2.LookupTable = cellDimensionLUT
threshold3Display_2.Specular = 1.0
threshold3Display_2.OSPRayScaleArray = 'CellDimension'
threshold3Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display_2.SelectOrientationVectors = 'CellDimension'
threshold3Display_2.ScaleFactor = 8.97187900543213
threshold3Display_2.SelectScaleArray = 'CellDimension'
threshold3Display_2.GlyphType = 'Arrow'
threshold3Display_2.GaussianRadius = 4.48593950271606
threshold3Display_2.CustomShader = ''
threshold3Display_2.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display_2.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display_2.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display_2.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display_2.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display_2.SelectionCellLabelFontFile = ''
threshold3Display_2.SelectionPointLabelFontFile = ''
threshold3Display_2.PolarAxes = 'PolarAxesRepresentation'
threshold3Display_2.ScalarOpacityFunction = cellDimensionPWF
threshold3Display_2.ScalarOpacityUnitDistance = 6.96479929698372

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display_2.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display_2.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold3Display_2.DataAxesGrid.XTitleFontFile = ''
threshold3Display_2.DataAxesGrid.YTitleFontFile = ''
threshold3Display_2.DataAxesGrid.ZTitleFontFile = ''
threshold3Display_2.DataAxesGrid.XLabelFontFile = ''
threshold3Display_2.DataAxesGrid.YLabelFontFile = ''
threshold3Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold3Display_2.PolarAxes.PolarAxisTitleFontFile = ''
threshold3Display_2.PolarAxes.PolarAxisLabelFontFile = ''
threshold3Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
threshold3Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display_2 = Show(tube1, renderView3)

# trace defaults for the display properties.
tube1Display_2.Representation = 'Surface'
tube1Display_2.ColorArrayName = [None, '']
tube1Display_2.Specular = 1.0
tube1Display_2.OSPRayScaleArray = 'CellDimension'
tube1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display_2.SelectOrientationVectors = 'CellDimension'
tube1Display_2.ScaleFactor = 8.65759143829346
tube1Display_2.SelectScaleArray = 'CellDimension'
tube1Display_2.GlyphType = 'Arrow'
tube1Display_2.GaussianRadius = 4.32879571914673
tube1Display_2.CustomShader = ''
tube1Display_2.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display_2.OpacityArray = ['POINTS', 'CellDimension']
tube1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display_2.DataAxesGrid = 'GridAxesRepresentation'
tube1Display_2.SelectionCellLabelFontFile = ''
tube1Display_2.SelectionPointLabelFontFile = ''
tube1Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display_2.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display_2.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display_2.DataAxesGrid.XTitleFontFile = ''
tube1Display_2.DataAxesGrid.YTitleFontFile = ''
tube1Display_2.DataAxesGrid.ZTitleFontFile = ''
tube1Display_2.DataAxesGrid.XLabelFontFile = ''
tube1Display_2.DataAxesGrid.YLabelFontFile = ''
tube1Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display_2 = Show(tube2, renderView3)

# trace defaults for the display properties.
tube2Display_2.Representation = 'Surface'
tube2Display_2.ColorArrayName = [None, '']
tube2Display_2.DiffuseColor = [0.36078431372549, 0.36078431372549, 0.36078431372549]
tube2Display_2.Specular = 1.0
tube2Display_2.OSPRayScaleArray = 'CellDimension'
tube2Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display_2.SelectOrientationVectors = 'CellDimension'
tube2Display_2.ScaleFactor = 11.5992790222168
tube2Display_2.SelectScaleArray = 'CellDimension'
tube2Display_2.GlyphType = 'Arrow'
tube2Display_2.GaussianRadius = 5.7996395111084
tube2Display_2.CustomShader = ''
tube2Display_2.SetScaleArray = ['POINTS', 'CellDimension']
tube2Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display_2.OpacityArray = ['POINTS', 'CellDimension']
tube2Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display_2.DataAxesGrid = 'GridAxesRepresentation'
tube2Display_2.SelectionCellLabelFontFile = ''
tube2Display_2.SelectionPointLabelFontFile = ''
tube2Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display_2.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display_2.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display_2.DataAxesGrid.XTitleFontFile = ''
tube2Display_2.DataAxesGrid.YTitleFontFile = ''
tube2Display_2.DataAxesGrid.ZTitleFontFile = ''
tube2Display_2.DataAxesGrid.XLabelFontFile = ''
tube2Display_2.DataAxesGrid.YLabelFontFile = ''
tube2Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display_2.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display_2.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display_2 = Show(tTKSphereFromPoint1, renderView3)

# trace defaults for the display properties.
tTKSphereFromPoint1Display_2.Representation = 'Surface'
tTKSphereFromPoint1Display_2.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_2.LookupTable = cellDimensionLUT
tTKSphereFromPoint1Display_2.Specular = 1.0
tTKSphereFromPoint1Display_2.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_2.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint1Display_2.ScaleFactor = 13.5
tTKSphereFromPoint1Display_2.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_2.GlyphType = 'Arrow'
tTKSphereFromPoint1Display_2.GaussianRadius = 6.75
tTKSphereFromPoint1Display_2.CustomShader = ''
tTKSphereFromPoint1Display_2.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_2.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_2.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display_2.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display_2.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint1Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display_2.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display_2.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint1Display_2.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint1Display_2.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint1Display_2.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint1Display_2.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint1Display_2.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint1Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKGeometrySmoother3
tTKGeometrySmoother3Display_1 = Show(tTKGeometrySmoother3, renderView3)

# trace defaults for the display properties.
tTKGeometrySmoother3Display_1.Representation = 'Surface'
tTKGeometrySmoother3Display_1.ColorArrayName = [None, '']
tTKGeometrySmoother3Display_1.DiffuseColor = [0.0, 0.431372549019608, 0.0]
tTKGeometrySmoother3Display_1.Opacity = 0.5
tTKGeometrySmoother3Display_1.Specular = 1.0
tTKGeometrySmoother3Display_1.OSPRayScaleArray = 'CriticalPointIndex'
tTKGeometrySmoother3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display_1.SelectOrientationVectors = 'None'
tTKGeometrySmoother3Display_1.ScaleFactor = 12.811474609375
tTKGeometrySmoother3Display_1.SelectScaleArray = 'None'
tTKGeometrySmoother3Display_1.GlyphType = 'Arrow'
tTKGeometrySmoother3Display_1.GaussianRadius = 6.4057373046875
tTKGeometrySmoother3Display_1.CustomShader = ''
tTKGeometrySmoother3Display_1.SetScaleArray = [None, '']
tTKGeometrySmoother3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display_1.OpacityArray = [None, '']
tTKGeometrySmoother3Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother3Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother3Display_1.SelectionCellLabelFontFile = ''
tTKGeometrySmoother3Display_1.SelectionPointLabelFontFile = ''
tTKGeometrySmoother3Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother3Display_1.ScalarOpacityUnitDistance = 5.6598863834941

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother3Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother3Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother3Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKGeometrySmoother3Display_1.DataAxesGrid.XTitleFontFile = ''
tTKGeometrySmoother3Display_1.DataAxesGrid.YTitleFontFile = ''
tTKGeometrySmoother3Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKGeometrySmoother3Display_1.DataAxesGrid.XLabelFontFile = ''
tTKGeometrySmoother3Display_1.DataAxesGrid.YLabelFontFile = ''
tTKGeometrySmoother3Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKGeometrySmoother3Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKGeometrySmoother3Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKGeometrySmoother3Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKGeometrySmoother3Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from computeDerivatives1
computeDerivatives1Display_2 = Show(computeDerivatives1, renderView3)

# trace defaults for the display properties.
computeDerivatives1Display_2.Representation = 'Volume'
computeDerivatives1Display_2.ColorArrayName = ['POINTS', 'log(s)']
computeDerivatives1Display_2.LookupTable = logsLUT
computeDerivatives1Display_2.OSPRayScaleArray = 'log(s)'
computeDerivatives1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display_2.SelectOrientationVectors = 'ScalarGradient'
computeDerivatives1Display_2.ScaleFactor = 13.3
computeDerivatives1Display_2.SelectScaleArray = 'log(s)'
computeDerivatives1Display_2.GlyphType = 'Arrow'
computeDerivatives1Display_2.SetScaleArray = [None, '']
computeDerivatives1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_2.OpacityArray = [None, '']
computeDerivatives1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_2.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display_2.SelectionCellLabelFontFile = ''
computeDerivatives1Display_2.SelectionPointLabelFontFile = ''
computeDerivatives1Display_2.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display_2.ScalarOpacityUnitDistance = 1.74099266343913
computeDerivatives1Display_2.ScalarOpacityFunction = logsPWF
computeDerivatives1Display_2.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
computeDerivatives1Display_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
computeDerivatives1Display_2.DataAxesGrid.XTitleFontFile = ''
computeDerivatives1Display_2.DataAxesGrid.YTitleFontFile = ''
computeDerivatives1Display_2.DataAxesGrid.ZTitleFontFile = ''
computeDerivatives1Display_2.DataAxesGrid.XLabelFontFile = ''
computeDerivatives1Display_2.DataAxesGrid.YLabelFontFile = ''
computeDerivatives1Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
computeDerivatives1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
computeDerivatives1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
computeDerivatives1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
computeDerivatives1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from builtInExamplevti
builtInExamplevtiDisplay_2 = Show(builtInExamplevti, renderView4)

# trace defaults for the display properties.
builtInExamplevtiDisplay_2.Representation = 'Outline'
builtInExamplevtiDisplay_2.ColorArrayName = ['POINTS', '']
builtInExamplevtiDisplay_2.OSPRayScaleArray = 'log(s)'
builtInExamplevtiDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_2.SelectOrientationVectors = 'None'
builtInExamplevtiDisplay_2.ScaleFactor = 13.3
builtInExamplevtiDisplay_2.SelectScaleArray = 'log(s)'
builtInExamplevtiDisplay_2.GlyphType = 'Arrow'
builtInExamplevtiDisplay_2.SetScaleArray = [None, '']
builtInExamplevtiDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_2.OpacityArray = [None, '']
builtInExamplevtiDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
builtInExamplevtiDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
builtInExamplevtiDisplay_2.SelectionCellLabelFontFile = ''
builtInExamplevtiDisplay_2.SelectionPointLabelFontFile = ''
builtInExamplevtiDisplay_2.PolarAxes = 'PolarAxesRepresentation'
builtInExamplevtiDisplay_2.ScalarOpacityUnitDistance = 1.74099266343913
builtInExamplevtiDisplay_2.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
builtInExamplevtiDisplay_2.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
builtInExamplevtiDisplay_2.DataAxesGrid.XTitleFontFile = ''
builtInExamplevtiDisplay_2.DataAxesGrid.YTitleFontFile = ''
builtInExamplevtiDisplay_2.DataAxesGrid.ZTitleFontFile = ''
builtInExamplevtiDisplay_2.DataAxesGrid.XLabelFontFile = ''
builtInExamplevtiDisplay_2.DataAxesGrid.YLabelFontFile = ''
builtInExamplevtiDisplay_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
builtInExamplevtiDisplay_2.PolarAxes.PolarAxisTitleFontFile = ''
builtInExamplevtiDisplay_2.PolarAxes.PolarAxisLabelFontFile = ''
builtInExamplevtiDisplay_2.PolarAxes.LastRadialAxisTextFontFile = ''
builtInExamplevtiDisplay_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display_1 = Show(tTKGeometrySmoother2, renderView4)

# trace defaults for the display properties.
tTKGeometrySmoother2Display_1.Representation = 'Surface'
tTKGeometrySmoother2Display_1.ColorArrayName = [None, '']
tTKGeometrySmoother2Display_1.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
tTKGeometrySmoother2Display_1.Specular = 1.0
tTKGeometrySmoother2Display_1.OSPRayScaleArray = 'CriticalPointIndex'
tTKGeometrySmoother2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display_1.ScaleFactor = 13.0726513981819
tTKGeometrySmoother2Display_1.SelectScaleArray = 'None'
tTKGeometrySmoother2Display_1.GlyphType = 'Arrow'
tTKGeometrySmoother2Display_1.GaussianRadius = 6.53632569909096
tTKGeometrySmoother2Display_1.CustomShader = ''
tTKGeometrySmoother2Display_1.SetScaleArray = [None, '']
tTKGeometrySmoother2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.OpacityArray = [None, '']
tTKGeometrySmoother2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display_1.SelectionCellLabelFontFile = ''
tTKGeometrySmoother2Display_1.SelectionPointLabelFontFile = ''
tTKGeometrySmoother2Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKGeometrySmoother2Display_1.DataAxesGrid.XTitleFontFile = ''
tTKGeometrySmoother2Display_1.DataAxesGrid.YTitleFontFile = ''
tTKGeometrySmoother2Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKGeometrySmoother2Display_1.DataAxesGrid.XLabelFontFile = ''
tTKGeometrySmoother2Display_1.DataAxesGrid.YLabelFontFile = ''
tTKGeometrySmoother2Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKGeometrySmoother2Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKGeometrySmoother2Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKGeometrySmoother2Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKGeometrySmoother2Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from contour1
contour1Display_3 = Show(contour1, renderView4)

# trace defaults for the display properties.
contour1Display_3.Representation = 'Surface With Edges'
contour1Display_3.ColorArrayName = ['POINTS', '']
contour1Display_3.Opacity = 0.15
contour1Display_3.Specular = 1.0
contour1Display_3.OSPRayScaleArray = 'log(Rho)'
contour1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_3.SelectOrientationVectors = 'None'
contour1Display_3.ScaleFactor = 11.046505355835
contour1Display_3.SelectScaleArray = 'log(Rho)'
contour1Display_3.GlyphType = 'Arrow'
contour1Display_3.GaussianRadius = 5.52325267791748
contour1Display_3.CustomShader = ''
contour1Display_3.SetScaleArray = ['POINTS', 'log(Rho)']
contour1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_3.OpacityArray = ['POINTS', 'log(Rho)']
contour1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_3.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_3.SelectionCellLabelFontFile = ''
contour1Display_3.SelectionPointLabelFontFile = ''
contour1Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_3.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_3.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display_3.DataAxesGrid.XTitleFontFile = ''
contour1Display_3.DataAxesGrid.YTitleFontFile = ''
contour1Display_3.DataAxesGrid.ZTitleFontFile = ''
contour1Display_3.DataAxesGrid.XLabelFontFile = ''
contour1Display_3.DataAxesGrid.YLabelFontFile = ''
contour1Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display_3.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display_3.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold3
threshold3Display_3 = Show(threshold3, renderView4)

# trace defaults for the display properties.
threshold3Display_3.Representation = 'Surface'
threshold3Display_3.ColorArrayName = ['POINTS', 'CellDimension']
threshold3Display_3.LookupTable = cellDimensionLUT
threshold3Display_3.Specular = 1.0
threshold3Display_3.OSPRayScaleArray = 'CellDimension'
threshold3Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display_3.SelectOrientationVectors = 'CellDimension'
threshold3Display_3.ScaleFactor = 8.97187900543213
threshold3Display_3.SelectScaleArray = 'CellDimension'
threshold3Display_3.GlyphType = 'Arrow'
threshold3Display_3.GaussianRadius = 4.48593950271606
threshold3Display_3.CustomShader = ''
threshold3Display_3.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display_3.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display_3.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display_3.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display_3.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display_3.SelectionCellLabelFontFile = ''
threshold3Display_3.SelectionPointLabelFontFile = ''
threshold3Display_3.PolarAxes = 'PolarAxesRepresentation'
threshold3Display_3.ScalarOpacityFunction = cellDimensionPWF
threshold3Display_3.ScalarOpacityUnitDistance = 6.96479929698372

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display_3.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display_3.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold3Display_3.DataAxesGrid.XTitleFontFile = ''
threshold3Display_3.DataAxesGrid.YTitleFontFile = ''
threshold3Display_3.DataAxesGrid.ZTitleFontFile = ''
threshold3Display_3.DataAxesGrid.XLabelFontFile = ''
threshold3Display_3.DataAxesGrid.YLabelFontFile = ''
threshold3Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold3Display_3.PolarAxes.PolarAxisTitleFontFile = ''
threshold3Display_3.PolarAxes.PolarAxisLabelFontFile = ''
threshold3Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
threshold3Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display_3 = Show(tTKSphereFromPoint1, renderView4)

# trace defaults for the display properties.
tTKSphereFromPoint1Display_3.Representation = 'Surface'
tTKSphereFromPoint1Display_3.ColorArrayName = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_3.LookupTable = cellDimensionLUT
tTKSphereFromPoint1Display_3.Specular = 1.0
tTKSphereFromPoint1Display_3.OSPRayScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_3.SelectOrientationVectors = 'CellDimension'
tTKSphereFromPoint1Display_3.ScaleFactor = 13.5
tTKSphereFromPoint1Display_3.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display_3.GlyphType = 'Arrow'
tTKSphereFromPoint1Display_3.GaussianRadius = 6.75
tTKSphereFromPoint1Display_3.CustomShader = ''
tTKSphereFromPoint1Display_3.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_3.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display_3.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display_3.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display_3.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint1Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display_3.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display_3.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint1Display_3.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint1Display_3.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint1Display_3.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint1Display_3.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint1Display_3.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint1Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint1Display_3.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint1Display_3.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint1Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint1Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube1
tube1Display_3 = Show(tube1, renderView4)

# trace defaults for the display properties.
tube1Display_3.Representation = 'Surface'
tube1Display_3.ColorArrayName = ['POINTS', '']
tube1Display_3.Specular = 1.0
tube1Display_3.OSPRayScaleArray = 'CellDimension'
tube1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display_3.SelectOrientationVectors = 'CellDimension'
tube1Display_3.ScaleFactor = 8.65759143829346
tube1Display_3.SelectScaleArray = 'CellDimension'
tube1Display_3.GlyphType = 'Arrow'
tube1Display_3.GaussianRadius = 4.32879571914673
tube1Display_3.CustomShader = ''
tube1Display_3.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display_3.OpacityArray = ['POINTS', 'CellDimension']
tube1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display_3.DataAxesGrid = 'GridAxesRepresentation'
tube1Display_3.SelectionCellLabelFontFile = ''
tube1Display_3.SelectionPointLabelFontFile = ''
tube1Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display_3.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display_3.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display_3.DataAxesGrid.XTitleFontFile = ''
tube1Display_3.DataAxesGrid.YTitleFontFile = ''
tube1Display_3.DataAxesGrid.ZTitleFontFile = ''
tube1Display_3.DataAxesGrid.XLabelFontFile = ''
tube1Display_3.DataAxesGrid.YLabelFontFile = ''
tube1Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display_3.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display_3.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display_3 = Show(tube2, renderView4)

# trace defaults for the display properties.
tube2Display_3.Representation = 'Surface'
tube2Display_3.ColorArrayName = [None, '']
tube2Display_3.DiffuseColor = [0.36078431372549, 0.36078431372549, 0.36078431372549]
tube2Display_3.Specular = 1.0
tube2Display_3.OSPRayScaleArray = 'CellDimension'
tube2Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display_3.SelectOrientationVectors = 'CellDimension'
tube2Display_3.ScaleFactor = 11.5992790222168
tube2Display_3.SelectScaleArray = 'CellDimension'
tube2Display_3.GlyphType = 'Arrow'
tube2Display_3.GaussianRadius = 5.7996395111084
tube2Display_3.CustomShader = ''
tube2Display_3.SetScaleArray = ['POINTS', 'CellDimension']
tube2Display_3.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display_3.OpacityArray = ['POINTS', 'CellDimension']
tube2Display_3.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display_3.DataAxesGrid = 'GridAxesRepresentation'
tube2Display_3.SelectionCellLabelFontFile = ''
tube2Display_3.SelectionPointLabelFontFile = ''
tube2Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display_3.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display_3.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube2Display_3.DataAxesGrid.XTitleFontFile = ''
tube2Display_3.DataAxesGrid.YTitleFontFile = ''
tube2Display_3.DataAxesGrid.ZTitleFontFile = ''
tube2Display_3.DataAxesGrid.XLabelFontFile = ''
tube2Display_3.DataAxesGrid.YLabelFontFile = ''
tube2Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube2Display_3.PolarAxes.PolarAxisTitleFontFile = ''
tube2Display_3.PolarAxes.PolarAxisLabelFontFile = ''
tube2Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
tube2Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from computeDerivatives1
computeDerivatives1Display_3 = Show(computeDerivatives1, renderView4)

# trace defaults for the display properties.
computeDerivatives1Display_3.Representation = 'Volume'
computeDerivatives1Display_3.ColorArrayName = ['POINTS', 'log(s)']
computeDerivatives1Display_3.LookupTable = logsLUT
computeDerivatives1Display_3.OSPRayScaleArray = 'log(s)'
computeDerivatives1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display_3.SelectOrientationVectors = 'ScalarGradient'
computeDerivatives1Display_3.ScaleFactor = 13.3
computeDerivatives1Display_3.SelectScaleArray = 'log(s)'
computeDerivatives1Display_3.GlyphType = 'Arrow'
computeDerivatives1Display_3.SetScaleArray = [None, '']
computeDerivatives1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_3.OpacityArray = [None, '']
computeDerivatives1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display_3.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display_3.SelectionCellLabelFontFile = ''
computeDerivatives1Display_3.SelectionPointLabelFontFile = ''
computeDerivatives1Display_3.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display_3.ScalarOpacityUnitDistance = 1.74099266343913
computeDerivatives1Display_3.ScalarOpacityFunction = logsPWF
computeDerivatives1Display_3.Slice = 66

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
computeDerivatives1Display_3.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
computeDerivatives1Display_3.DataAxesGrid.XTitleFontFile = ''
computeDerivatives1Display_3.DataAxesGrid.YTitleFontFile = ''
computeDerivatives1Display_3.DataAxesGrid.ZTitleFontFile = ''
computeDerivatives1Display_3.DataAxesGrid.XLabelFontFile = ''
computeDerivatives1Display_3.DataAxesGrid.YLabelFontFile = ''
computeDerivatives1Display_3.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
computeDerivatives1Display_3.PolarAxes.PolarAxisTitleFontFile = ''
computeDerivatives1Display_3.PolarAxes.PolarAxisLabelFontFile = ''
computeDerivatives1Display_3.PolarAxes.LastRadialAxisTextFontFile = ''
computeDerivatives1Display_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'IntegrationTime'
integrationTimePWF = GetOpacityTransferFunction('IntegrationTime')
integrationTimePWF.Points = [0.0, 0.0, 0.5, 0.0, 704.506695138077, 1.0, 0.5, 0.0]
integrationTimePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------