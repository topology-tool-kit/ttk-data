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
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [822, 589]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, 0.998917326331139, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [-4.30578629311887, -7.1502419192231, -1.42782357329266]
renderView2.CameraFocalPoint = [0.123893433039095, 0.931307404077181, -0.00169360938952134]
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

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [822, 589]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [-0.00547350355230147, 0.0452015383244153, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [-0.0583994234081377, 0.0366171880106964, -10.6472725369372]
renderView3.CameraFocalPoint = [-0.0583994234081377, 0.0366171880106964, 0.0]
renderView3.CameraParallelScale = 2.47612510100868
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.FacesToRender = 0
renderView3.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView3.AxesGrid.ShowEdges = 0
renderView3.AxesGrid.ShowTicks = 0
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [821, 1216]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [-0.00547343492507935, 0.0452015399932861, 0.0]
renderView4.StereoType = 0
renderView4.CameraPosition = [0.0635132012721223, 0.186636507394001, -9.81525986253902]
renderView4.CameraFocalPoint = [0.0635132012721223, 0.186636507394001, 0.0]
renderView4.CameraParallelScale = 2.55571997037375
renderView4.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.Visibility = 1
renderView4.AxesGrid.XTitleFontFile = ''
renderView4.AxesGrid.YTitleFontFile = ''
renderView4.AxesGrid.ZTitleFontFile = ''
renderView4.AxesGrid.FacesToRender = 0
renderView4.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView4.AxesGrid.ShowEdges = 0
renderView4.AxesGrid.ShowTicks = 0
renderView4.AxesGrid.XLabelFontFile = ''
renderView4.AxesGrid.YLabelFontFile = ''
renderView4.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
pointCloudcsv = CSVReader(FileName=['pointCloud.csv'])

# create a new 'TTK DimensionReduction'
tTKDimensionReduction1 = TTKDimensionReduction(Input=pointCloudcsv,
    ModulePath='default')
tTKDimensionReduction1.InputColumns = ['Points:0', 'Points:1', 'Points:2']
tTKDimensionReduction1.Method = 'Multi-Dimensional Scaling'
tTKDimensionReduction1.Method = 'Multi-Dimensional Scaling'
tTKDimensionReduction1.Method = 'Multi-Dimensional Scaling'

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=tTKDimensionReduction1)
tableToPoints2.XColumn = 'Component_0'
tableToPoints2.YColumn = 'Component_1'
tableToPoints2.ZColumn = 'Component_0'
tableToPoints2.a2DPoints = 1

# create a new 'Gaussian Resampling'
gaussianResampling2 = GaussianResampling(Input=tableToPoints2)
gaussianResampling2.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling2.ResamplingGrid = [128, 64, 3]
gaussianResampling2.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling2)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.00547350355230147, 0.0452015383244153, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

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

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tableToPoints2)
tTKSphereFromPoint2.Radius = 0.035

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = 'SplatterValues'
tTKPersistenceDiagram1.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [3.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=slice1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'SplatterValues'
tTKTopologicalSimplification1.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification1.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification1.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex1.InputOffsetField = 'SplatterValues'

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKMorseSmaleComplex1)
tTKSphereFromPoint1.Radius = 0.075

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,1))
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.ThresholdRange = [1.0, 1.0]

# create a new 'Threshold'
threshold3 = Threshold(Input=threshold2)
threshold3.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold3)
tTKGeometrySmoother1.IterationNumber = 100
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.0414543533325195

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from gaussianResampling1
gaussianResampling1Display = Show(gaussianResampling1, renderView2)

# get separate color transfer function/color map for 'SplatterValues'
separate_gaussianResampling1Display_SplatterValuesLUT = GetColorTransferFunction('SplatterValues', gaussianResampling1Display, separate=True)
separate_gaussianResampling1Display_SplatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 0.153341370750671, 0.0941176470588235, 0.211764705882353, 0.603921568627451, 0.648506273712424, 0.917647, 0.941176, 0.788235, 0.999913546083997, 0.0, 0.431373, 0.0]
separate_gaussianResampling1Display_SplatterValuesLUT.ColorSpace = 'RGB'
separate_gaussianResampling1Display_SplatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
separate_gaussianResampling1Display_SplatterValuesLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'SplatterValues'
separate_gaussianResampling1Display_SplatterValuesPWF = GetOpacityTransferFunction('SplatterValues', gaussianResampling1Display, separate=True)
separate_gaussianResampling1Display_SplatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.546278654961227, 0.264423072338104, 0.5, 0.0, 0.999913546083997, 0.0769230797886848, 0.5, 0.0]
separate_gaussianResampling1Display_SplatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
gaussianResampling1Display.Representation = 'Volume'
gaussianResampling1Display.ColorArrayName = ['POINTS', 'SplatterValues']
gaussianResampling1Display.LookupTable = separate_gaussianResampling1Display_SplatterValuesLUT
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
gaussianResampling1Display.ScalarOpacityFunction = separate_gaussianResampling1Display_SplatterValuesPWF
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

# set separate color map
gaussianResampling1Display.UseSeparateColorMap = True

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
outline1Display = Show(outline1, renderView2)

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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView3)

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 6.29735971356196, 0.0941176470588235, 0.211764705882353, 0.603921568627451, 26.6325862490761, 0.917647, 0.941176, 0.788235, 41.0640341307024, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice1Display.LookupTable = splatterValuesLUT
slice1Display.Specular = 1.0
slice1Display.OSPRayScaleArray = 'SplatterValues'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.546927547454834
slice1Display.SelectScaleArray = 'SplatterValues'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'SplatterValues'
slice1Display.GaussianRadius = 0.0273463773727417
slice1Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'SplatterValues']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 33.6326228177258, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 33.6326228177258, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint2
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView3)

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = [None, '']
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'Elevation'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'Elevation'
tTKSphereFromPoint2Display.ScaleFactor = 0.555431413650513
tTKSphereFromPoint2Display.SelectScaleArray = 'Elevation'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GlyphTableIndexArray = 'Elevation'
tTKSphereFromPoint2Display.GaussianRadius = 0.0277715706825256
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'Elevation']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'Elevation']
tTKSphereFromPoint2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint2Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint2Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint2Display.ScaleTransferFunction.Points = [0.068044, 0.0, 0.5, 0.0, 0.9329, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint2Display.OpacityTransferFunction.Points = [0.068044, 0.0, 0.5, 0.0, 0.9329, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint2Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_2
tTKMorseSmaleComplex1Display = Show(OutputPort(tTKMorseSmaleComplex1, 2), renderView4)

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = [None, '']
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = -2e+298
tTKMorseSmaleComplex1Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1Display.GaussianRadius = -1e+297
tTKMorseSmaleComplex1Display.SetScaleArray = [None, '']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = [None, '']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'

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

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView4)

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display_1.Representation = 'Surface'
tTKMorseSmaleComplex1Display_1.ColorArrayName = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display_1.LookupTable = splatterValuesLUT
tTKMorseSmaleComplex1Display_1.Specular = 1.0
tTKMorseSmaleComplex1Display_1.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex1Display_1.ScaleFactor = 0.546927547454834
tTKMorseSmaleComplex1Display_1.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display_1.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display_1.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex1Display_1.GaussianRadius = 0.0273463773727417
tTKMorseSmaleComplex1Display_1.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display_1.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display_1.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex1Display_1.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex1Display_1.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex1Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex1Display_1.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex1Display_1.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView4)

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
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
tTKSphereFromPoint1Display.ScaleFactor = 0.646585988998413
tTKSphereFromPoint1Display.SelectScaleArray = 'CellDimension'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'CellDimension'
tTKSphereFromPoint1Display.GaussianRadius = 0.0323292994499207
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

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
tube1Display = Show(tube1, renderView4)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.0, 0.431372549019608, 0.0]
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 0.421723198890686
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 0.0210861599445343
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

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

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 22.4343448691689, 0.264423072338104, 0.5, 0.0, 41.0640341307024, 0.0769230797886848, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))


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


tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))
