from paraview.simple import *
if len(sys.argv) >= 2:
	outputDirectory = sys.argv[1] + '/'
	if len(sys.argv) == 3:
		debugLevel = sys.argv[2]
	else:
		debugLevel = 0
else:
	print('Missing output directory')
	sys.exit()
if debugLevel != 0:
	print('  Debug level: ' + debugLevel)
# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [821, 1216]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.998917326331139, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [-4.30112073606076, -7.16397323687998, -1.36450297861183]
renderView1.CameraFocalPoint = [0.128558990097204, 0.917576086420296, 0.0616269852913064]
renderView1.CameraViewUp = [0.0529334977412574, 0.145329784500767, -0.987966243630741]
renderView1.CameraParallelScale = 3.56228671637776
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.FacesToRender = 0
renderView1.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView1.AxesGrid.ShowEdges = 0
renderView1.AxesGrid.ShowTicks = 0
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [822, 1216]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, 0.998917326331139, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [-4.30112073606076, -7.16397323687998, -1.36450297861183]
renderView2.CameraFocalPoint = [0.128558990097204, 0.917576086420296, 0.0616269852913064]
renderView2.CameraViewUp = [0.0529334977412574, 0.145329784500767, -0.987966243630741]
renderView2.CameraParallelScale = 3.56228671637776
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.FacesToRender = 0
renderView2.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView2.AxesGrid.ShowEdges = 0
renderView2.AxesGrid.ShowTicks = 0
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
pointCloudcsv = CSVReader(FileName=['pointCloud.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=pointCloudcsv)
tableToPoints1.XColumn = 'Points:0'
tableToPoints1.YColumn = 'Points:1'
tableToPoints1.ZColumn = 'Points:2'

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling1.ResamplingGrid = [64, 64, 128]

# create a new 'Outline'
outline1 = Outline(Input=gaussianResampling1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=gaussianResampling1)
tTKPersistenceDiagram1.ScalarField = 'SplatterValues'
tTKPersistenceDiagram1.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 9999.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.01, 0.999953171649318]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=gaussianResampling1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'SplatterValues'
tTKTopologicalSimplification1.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification1.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification1.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex1.InputOffsetField = 'SplatterValues'
tTKMorseSmaleComplex1.Ascending2Separatrices = 1
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.01

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint1.Radius = 0.025

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=OutputPort(tTKMorseSmaleComplex1_1,2))

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=tetrahedralize1)
tTKGeometrySmoother2.IterationNumber = 20
tTKGeometrySmoother2.InputMaskField = 'NumberOfCriticalPointsOnBoundary'

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface2)

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_2,1))
threshold2.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 20
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.01

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from outline1
outline1Display = Show(outline1, renderView1)

# trace defaults for the display properties.
outline1Display.Representation = 'Surface'
outline1Display.ColorArrayName = [None, '']
outline1Display.Specular = 1.0
outline1Display.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display.SelectOrientationVectors = 'None'
outline1Display.ScaleFactor = 0.480000019073486
outline1Display.SelectScaleArray = 'None'
outline1Display.GlyphType = 'Arrow'
outline1Display.GlyphTableIndexArray = 'None'
outline1Display.GaussianRadius = 0.0240000009536743
outline1Display.SetScaleArray = [None, '']
outline1Display.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display.OpacityArray = [None, '']
outline1Display.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display.DataAxesGrid = 'GridAxesRepresentation'
outline1Display.SelectionCellLabelFontFile = ''
outline1Display.SelectionPointLabelFontFile = ''
outline1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
outline1Display.DataAxesGrid.XTitleFontFile = ''
outline1Display.DataAxesGrid.YTitleFontFile = ''
outline1Display.DataAxesGrid.ZTitleFontFile = ''
outline1Display.DataAxesGrid.XLabelFontFile = ''
outline1Display.DataAxesGrid.YLabelFontFile = ''
outline1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
outline1Display.PolarAxes.PolarAxisTitleFontFile = ''
outline1Display.PolarAxes.PolarAxisLabelFontFile = ''
outline1Display.PolarAxes.LastRadialAxisTextFontFile = ''
outline1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1Display = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView1)

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Outline'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex1Display.ScaleFactor = 0.48
tTKMorseSmaleComplex1Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.024
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display.ScalarOpacityUnitDistance = 0.0987445237175993
tTKMorseSmaleComplex1Display.IsosurfaceValues = [0.499966283934866]
tTKMorseSmaleComplex1Display.Slice = 31

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
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
tTKSphereFromPoint1Display.ScaleFactor = 0.446326375007629
tTKSphereFromPoint1Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint1Display.GaussianRadius = 0.0223163187503815
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

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

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 0.410560917854309
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 0.0205280458927155
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

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

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = [None, '']
generateSurfaceNormals1Display.DiffuseColor = [0.0, 0.0, 0.498039215686275]
generateSurfaceNormals1Display.Opacity = 0.5
generateSurfaceNormals1Display.Specular = 1.0
generateSurfaceNormals1Display.OSPRayScaleArray = 'Normals'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'None'
generateSurfaceNormals1Display.ScaleFactor = 0.400539422035217
generateSurfaceNormals1Display.SelectScaleArray = 'None'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'None'
generateSurfaceNormals1Display.GaussianRadius = 0.0200269711017609
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'Normals']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'Normals']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [-0.999997437000275, 0.0, 0.5, 0.0, 0.999999761581421, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [-0.999997437000275, 0.0, 0.5, 0.0, 0.999999761581421, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals1Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals1Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals1Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from gaussianResampling1
gaussianResampling1Display = Show(gaussianResampling1, renderView2)

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 0.153352356380398, 0.0941176470588235, 0.211764705882353, 0.603921568627451, 0.64855273377577, 0.917647, 0.941176, 0.788235, 0.99998518154625, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.546317791268681, 0.264423072338104, 0.5, 0.0, 0.99998518154625, 0.0769230797886848, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
gaussianResampling1Display.Representation = 'Volume'
gaussianResampling1Display.ColorArrayName = ['POINTS', 'SplatterValues']
gaussianResampling1Display.LookupTable = splatterValuesLUT
gaussianResampling1Display.OSPRayScaleArray = 'SplatterValues'
gaussianResampling1Display.OSPRayScaleFunction = 'PiecewiseFunction'
gaussianResampling1Display.SelectOrientationVectors = 'None'
gaussianResampling1Display.ScaleFactor = 0.48
gaussianResampling1Display.SelectScaleArray = 'SplatterValues'
gaussianResampling1Display.GlyphType = 'Arrow'
gaussianResampling1Display.GlyphTableIndexArray = 'SplatterValues'
gaussianResampling1Display.GaussianRadius = 0.024
gaussianResampling1Display.SetScaleArray = ['POINTS', 'SplatterValues']
gaussianResampling1Display.ScaleTransferFunction = 'PiecewiseFunction'
gaussianResampling1Display.OpacityArray = ['POINTS', 'SplatterValues']
gaussianResampling1Display.OpacityTransferFunction = 'PiecewiseFunction'
gaussianResampling1Display.DataAxesGrid = 'GridAxesRepresentation'
gaussianResampling1Display.SelectionCellLabelFontFile = ''
gaussianResampling1Display.SelectionPointLabelFontFile = ''
gaussianResampling1Display.PolarAxes = 'PolarAxesRepresentation'
gaussianResampling1Display.ScalarOpacityUnitDistance = 0.0987445237175993
gaussianResampling1Display.ScalarOpacityFunction = splatterValuesPWF
gaussianResampling1Display.Shade = 1
gaussianResampling1Display.IsosurfaceValues = [0.499976585824659]
gaussianResampling1Display.Slice = 31

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gaussianResampling1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.999913546083997, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gaussianResampling1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.999913546083997, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
gaussianResampling1Display.DataAxesGrid.XTitleFontFile = ''
gaussianResampling1Display.DataAxesGrid.YTitleFontFile = ''
gaussianResampling1Display.DataAxesGrid.ZTitleFontFile = ''
gaussianResampling1Display.DataAxesGrid.XLabelFontFile = ''
gaussianResampling1Display.DataAxesGrid.YLabelFontFile = ''
gaussianResampling1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
gaussianResampling1Display.PolarAxes.PolarAxisTitleFontFile = ''
gaussianResampling1Display.PolarAxes.PolarAxisLabelFontFile = ''
gaussianResampling1Display.PolarAxes.LastRadialAxisTextFontFile = ''
gaussianResampling1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tableToPoints1
tableToPoints1Display = Show(tableToPoints1, renderView2)

# trace defaults for the display properties.
tableToPoints1Display.Representation = 'Point Gaussian'
tableToPoints1Display.ColorArrayName = [None, '']
tableToPoints1Display.Specular = 1.0
tableToPoints1Display.OSPRayScaleArray = 'Elevation'
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.SelectOrientationVectors = 'Elevation'
tableToPoints1Display.ScaleFactor = 0.4
tableToPoints1Display.SelectScaleArray = 'Elevation'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.GlyphTableIndexArray = 'Elevation'
tableToPoints1Display.GaussianRadius = 0.05
tableToPoints1Display.SetScaleArray = ['POINTS', 'Elevation']
tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.OpacityArray = ['POINTS', 'Elevation']
tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.SelectionCellLabelFontFile = ''
tableToPoints1Display.SelectionPointLabelFontFile = ''
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tableToPoints1Display.ScaleTransferFunction.Points = [0.068044, 0.0, 0.5, 0.0, 0.9329, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tableToPoints1Display.OpacityTransferFunction.Points = [0.068044, 0.0, 0.5, 0.0, 0.9329, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tableToPoints1Display.DataAxesGrid.XTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.YTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.ZTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.XLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.YLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFile = ''
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from outline1
outline1Display_1 = Show(outline1, renderView2)

# trace defaults for the display properties.
outline1Display_1.Representation = 'Surface'
outline1Display_1.ColorArrayName = [None, '']
outline1Display_1.Specular = 1.0
outline1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
outline1Display_1.SelectOrientationVectors = 'None'
outline1Display_1.ScaleFactor = 0.480000019073486
outline1Display_1.SelectScaleArray = 'None'
outline1Display_1.GlyphType = 'Arrow'
outline1Display_1.GlyphTableIndexArray = 'None'
outline1Display_1.GaussianRadius = 0.0240000009536743
outline1Display_1.SetScaleArray = [None, '']
outline1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
outline1Display_1.OpacityArray = [None, '']
outline1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
outline1Display_1.DataAxesGrid = 'GridAxesRepresentation'
outline1Display_1.SelectionCellLabelFontFile = ''
outline1Display_1.SelectionPointLabelFontFile = ''
outline1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
outline1Display_1.DataAxesGrid.XTitleFontFile = ''
outline1Display_1.DataAxesGrid.YTitleFontFile = ''
outline1Display_1.DataAxesGrid.ZTitleFontFile = ''
outline1Display_1.DataAxesGrid.XLabelFontFile = ''
outline1Display_1.DataAxesGrid.YLabelFontFile = ''
outline1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
outline1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
outline1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
outline1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
outline1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))


tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification1, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification1.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification1)))


tTKMorseSmaleComplex1.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex1, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex1.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex1)))


tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))


tTKGeometrySmoother2.DebugLevel = int(debugLevel)
if tTKGeometrySmoother2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother2, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother2.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother2)))


tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
