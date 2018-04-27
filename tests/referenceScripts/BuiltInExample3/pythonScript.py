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
lowerBound = CreateView('RenderView')
lowerBound.ViewSize = [1119, 286]
lowerBound.InteractionMode = '2D'
lowerBound.AxesGrid = 'GridAxes3DActor'
lowerBound.OrientationAxesVisibility = 0
lowerBound.CenterOfRotation = [256.0, 32.0, 0.0]
lowerBound.StereoType = 0
lowerBound.CameraPosition = [257.900347475601, 25.8238707042957, 10000.0]
lowerBound.CameraFocalPoint = [257.900347475601, 25.8238707042957, 0.0]
lowerBound.CameraParallelScale = 67.9374222527477
lowerBound.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
lowerBound.AxesGrid.XTitleFontFile = ''
lowerBound.AxesGrid.YTitleFontFile = ''
lowerBound.AxesGrid.ZTitleFontFile = ''
lowerBound.AxesGrid.XLabelFontFile = ''
lowerBound.AxesGrid.YLabelFontFile = ''
lowerBound.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
mandatoryJoinTree = CreateView('RenderView')
mandatoryJoinTree.ViewSize = [560, 286]
mandatoryJoinTree.InteractionMode = '2D'
mandatoryJoinTree.AxesGrid = 'GridAxes3DActor'
mandatoryJoinTree.OrientationAxesVisibility = 0
mandatoryJoinTree.CenterOfRotation = [0.5, 0.5, 0.0]
mandatoryJoinTree.StereoType = 0
mandatoryJoinTree.CameraPosition = [0.5, 0.5, 2.25789322939577]
mandatoryJoinTree.CameraFocalPoint = [0.5, 0.5, 0.0]
mandatoryJoinTree.CameraParallelScale = 0.707106781186548
mandatoryJoinTree.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
mandatoryJoinTree.AxesGrid.XTitleFontFile = ''
mandatoryJoinTree.AxesGrid.YTitleFontFile = ''
mandatoryJoinTree.AxesGrid.ZTitleFontFile = ''
mandatoryJoinTree.AxesGrid.XLabelFontFile = ''
mandatoryJoinTree.AxesGrid.YLabelFontFile = ''
mandatoryJoinTree.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
mandatoryMaxima = CreateView('RenderView')
mandatoryMaxima.ViewSize = [1122, 286]
mandatoryMaxima.InteractionMode = '2D'
mandatoryMaxima.AxesGrid = 'GridAxes3DActor'
mandatoryMaxima.OrientationAxesVisibility = 0
mandatoryMaxima.CenterOfRotation = [256.0, 32.0, 0.0]
mandatoryMaxima.StereoType = 0
mandatoryMaxima.CameraPosition = [257.900347475601, 25.8238707042957, 10000.0]
mandatoryMaxima.CameraFocalPoint = [257.900347475601, 25.8238707042957, 0.0]
mandatoryMaxima.CameraParallelScale = 67.9374222527477
mandatoryMaxima.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
mandatoryMaxima.AxesGrid.XTitleFontFile = ''
mandatoryMaxima.AxesGrid.YTitleFontFile = ''
mandatoryMaxima.AxesGrid.ZTitleFontFile = ''
mandatoryMaxima.AxesGrid.XLabelFontFile = ''
mandatoryMaxima.AxesGrid.YLabelFontFile = ''
mandatoryMaxima.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
mandatoryMinima = CreateView('RenderView')
mandatoryMinima.ViewSize = [1122, 286]
mandatoryMinima.InteractionMode = '2D'
mandatoryMinima.AxesGrid = 'GridAxes3DActor'
mandatoryMinima.OrientationAxesVisibility = 0
mandatoryMinima.CenterOfRotation = [256.0, 32.0, 0.0]
mandatoryMinima.StereoType = 0
mandatoryMinima.CameraPosition = [257.900347475601, 25.8238707042957, 10000.0]
mandatoryMinima.CameraFocalPoint = [257.900347475601, 25.8238707042957, 0.0]
mandatoryMinima.CameraParallelScale = 67.9374222527477
mandatoryMinima.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
mandatoryMinima.AxesGrid.XTitleFontFile = ''
mandatoryMinima.AxesGrid.YTitleFontFile = ''
mandatoryMinima.AxesGrid.ZTitleFontFile = ''
mandatoryMinima.AxesGrid.XLabelFontFile = ''
mandatoryMinima.AxesGrid.YLabelFontFile = ''
mandatoryMinima.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
mandatorySplitTree = CreateView('RenderView')
mandatorySplitTree.ViewSize = [560, 286]
mandatorySplitTree.InteractionMode = '2D'
mandatorySplitTree.AxesGrid = 'GridAxes3DActor'
mandatorySplitTree.OrientationAxesVisibility = 0
mandatorySplitTree.CenterOfRotation = [0.5, 0.5, 0.0]
mandatorySplitTree.StereoType = 0
mandatorySplitTree.CameraPosition = [0.5, 0.5, 2.25789322939577]
mandatorySplitTree.CameraFocalPoint = [0.5, 0.5, 0.0]
mandatorySplitTree.CameraParallelScale = 0.707106781186548
mandatorySplitTree.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
mandatorySplitTree.AxesGrid.XTitleFontFile = ''
mandatorySplitTree.AxesGrid.YTitleFontFile = ''
mandatorySplitTree.AxesGrid.ZTitleFontFile = ''
mandatorySplitTree.AxesGrid.XLabelFontFile = ''
mandatorySplitTree.AxesGrid.YLabelFontFile = ''
mandatorySplitTree.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
peristenceDiagramLower = CreateView('RenderView')
peristenceDiagramLower.ViewSize = [563, 286]
peristenceDiagramLower.InteractionMode = '2D'
peristenceDiagramLower.AxesGrid = 'GridAxes3DActor'
peristenceDiagramLower.OrientationAxesVisibility = 0
peristenceDiagramLower.CenterOfRotation = [0.61721670627594, 0.681049704551697, 0.0]
peristenceDiagramLower.StereoType = 0
peristenceDiagramLower.CameraPosition = [0.649088241337862, 0.696985472082657, 10000.0]
peristenceDiagramLower.CameraFocalPoint = [0.649088241337862, 0.696985472082657, 0.0]
peristenceDiagramLower.CameraParallelScale = 0.759604918975797
peristenceDiagramLower.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
peristenceDiagramLower.AxesGrid.XTitleFontFile = ''
peristenceDiagramLower.AxesGrid.YTitleFontFile = ''
peristenceDiagramLower.AxesGrid.ZTitleFontFile = ''
peristenceDiagramLower.AxesGrid.XLabelFontFile = ''
peristenceDiagramLower.AxesGrid.YLabelFontFile = ''
peristenceDiagramLower.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
persistenceDiagramUpper = CreateView('RenderView')
persistenceDiagramUpper.ViewSize = [563, 286]
persistenceDiagramUpper.InteractionMode = '2D'
persistenceDiagramUpper.AxesGrid = 'GridAxes3DActor'
persistenceDiagramUpper.OrientationAxesVisibility = 0
persistenceDiagramUpper.CenterOfRotation = [0.61721670627594, 0.681049704551697, 0.0]
persistenceDiagramUpper.StereoType = 0
persistenceDiagramUpper.CameraPosition = [0.649088241337862, 0.696985472082657, 10000.0]
persistenceDiagramUpper.CameraFocalPoint = [0.649088241337862, 0.696985472082657, 0.0]
persistenceDiagramUpper.CameraParallelScale = 0.759604918975797
persistenceDiagramUpper.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
persistenceDiagramUpper.AxesGrid.XTitleFontFile = ''
persistenceDiagramUpper.AxesGrid.YTitleFontFile = ''
persistenceDiagramUpper.AxesGrid.ZTitleFontFile = ''
persistenceDiagramUpper.AxesGrid.XLabelFontFile = ''
persistenceDiagramUpper.AxesGrid.YLabelFontFile = ''
persistenceDiagramUpper.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
upperBound = CreateView('RenderView')
upperBound.ViewSize = [1119, 286]
upperBound.InteractionMode = '2D'
upperBound.AxesGrid = 'GridAxes3DActor'
upperBound.OrientationAxesVisibility = 0
upperBound.CenterOfRotation = [256.0, 32.0, 0.0]
upperBound.StereoType = 0
upperBound.CameraPosition = [257.900347475601, 25.8238707042957, 10000.0]
upperBound.CameraFocalPoint = [257.900347475601, 25.8238707042957, 0.0]
upperBound.CameraParallelScale = 67.9374222527477
upperBound.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
upperBound.AxesGrid.XTitleFontFile = ''
upperBound.AxesGrid.YTitleFontFile = ''
upperBound.AxesGrid.ZTitleFontFile = ''
upperBound.AxesGrid.XLabelFontFile = ''
upperBound.AxesGrid.YLabelFontFile = ''
upperBound.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(lowerBound)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
example3vti = XMLImageDataReader(FileName=['BuiltInExample3.vti'])
example3vti.PointArrayStatus = ['lowerBoundField', 'upperBoundField']

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=example3vti)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram2.ScalarField = 'upperBoundField'
tTKPersistenceDiagram2.InputOffsetField = ''

# create a new 'Threshold'
diagonal = Threshold(Input=tTKPersistenceDiagram2)
diagonal.Scalars = ['CELLS', 'PairIdentifier']
diagonal.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=diagonal)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=tetrahedralize1)
tTKPersistenceDiagram1.ScalarField = 'lowerBoundField'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
persistencePairs = Threshold(Input=tTKPersistenceDiagram1)
persistencePairs.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs.ThresholdRange = [-0.1, 98.0]

# create a new 'Threshold'
diagonal_1 = Threshold(Input=tTKPersistenceDiagram1)
diagonal_1.Scalars = ['CELLS', 'PairIdentifier']
diagonal_1.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=diagonal_1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.02

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(Input=example3vti)
tTKMandatoryCriticalPoints1.LowerBoundField = 'lowerBoundField'
tTKMandatoryCriticalPoints1.UpperBoundField = 'upperBoundField'

# find source
tTKMandatoryCriticalPoints1_1 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(Input=OutputPort(tTKMandatoryCriticalPoints1_1,5))

# create a new 'Tube'
tube6 = Tube(Input=extractSurface6)
tube6.Scalars = ['POINTS', 'ComponentId']
tube6.Vectors = [None, '']
tube6.Radius = 0.01

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold1.Scalars = ['POINTS', 'MinimumComponents']
threshold1.ThresholdRange = [-0.1, 21.0]

# find source
tTKMandatoryCriticalPoints1_2 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=OutputPort(tTKMandatoryCriticalPoints1_2,4))

# create a new 'Tube'
tube5 = Tube(Input=extractSurface5)
tube5.Scalars = ['POINTS', 'ComponentId']
tube5.Vectors = [None, '']
tube5.Radius = 0.01

# find source
tTKMandatoryCriticalPoints1_3 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1_3,3))
threshold2.Scalars = ['POINTS', 'MaximumComponents']
threshold2.ThresholdRange = [-0.1, 27.0]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint6 = TTKSphereFromPoint(Input=OutputPort(tTKMandatoryCriticalPoints1_1,5))
tTKSphereFromPoint6.Radius = 0.025

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=OutputPort(tTKMandatoryCriticalPoints1_2,4))
tTKSphereFromPoint5.Radius = 0.025

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=persistencePairs)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.0, 1.37]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.0136209940910339

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 0.025

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint1)
tTKTopologicalSimplification1.ScalarField = 'lowerBoundField'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = 'lowerBoundField'
tTKScalarFieldCriticalPoints1.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints1.Withvertexidentifiers = 0
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 3.5

# create a new 'Threshold'
maxima = Threshold(Input=tTKSphereFromPoint2)
maxima.Scalars = ['POINTS', 'CriticalIndex']
maxima.ThresholdRange = [1.9, 2.0]

# create a new 'Threshold'
minima = Threshold(Input=tTKSphereFromPoint2)
minima.Scalars = ['POINTS', 'CriticalIndex']
minima.ThresholdRange = [0.0, 0.1]

# create a new 'Threshold'
persistencePairs_1 = Threshold(Input=tTKPersistenceDiagram2)
persistencePairs_1.Scalars = ['CELLS', 'PairIdentifier']
persistencePairs_1.ThresholdRange = [-0.1, 108.0]

# create a new 'Threshold'
persistenceThreshold_1 = Threshold(Input=persistencePairs_1)
persistenceThreshold_1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold_1.ThresholdRange = [0.0, 1.38]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=persistenceThreshold_1)
tTKSphereFromPoint3.Radius = 0.025

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=tetrahedralize1,
    Constraints=tTKSphereFromPoint3)
tTKTopologicalSimplification2.ScalarField = 'upperBoundField'
tTKTopologicalSimplification2.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints2 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification2)
tTKScalarFieldCriticalPoints2.ScalarField = 'upperBoundField'
tTKScalarFieldCriticalPoints2.UseInputOffsetField = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints2)
tTKSphereFromPoint4.Radius = 3.5

# create a new 'Threshold'
minima_1 = Threshold(Input=tTKSphereFromPoint4)
minima_1.Scalars = ['POINTS', 'CriticalIndex']
minima_1.ThresholdRange = [0.0, 0.1]

# create a new 'Threshold'
maxima_1 = Threshold(Input=tTKSphereFromPoint4)
maxima_1.Scalars = ['POINTS', 'CriticalIndex']
maxima_1.ThresholdRange = [1.9, 2.0]

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=persistenceThreshold_1)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'NodeType']
tube4.Vectors = [None, '']
tube4.Radius = 0.0136209940910339

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = [None, '']
tube3.Radius = 0.02

# create a new 'Transform'
transform1 = Transform(Input=threshold1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.0, 0.0, 0.0001]

# ----------------------------------------------------------------
# setup the visualization in view 'lowerBound'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification1
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, lowerBound)

# get color transfer function/color map for 'lowerBoundField'
lowerBoundFieldLUT = GetColorTransferFunction('lowerBoundField')
lowerBoundFieldLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 0.681049704551697, 0.917647, 0.941176, 0.788235, 1.36209940910339, 0.0, 0.431373, 0.0]
lowerBoundFieldLUT.ColorSpace = 'RGB'
lowerBoundFieldLUT.AboveRangeColor = [1.0, 1.0, 1.0]
lowerBoundFieldLUT.NanColor = [0.0, 0.0, 0.0]
lowerBoundFieldLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'lowerBoundField'
lowerBoundFieldPWF = GetOpacityTransferFunction('lowerBoundField')
lowerBoundFieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.36209940910339, 1.0, 0.5, 0.0]
lowerBoundFieldPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Surface'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', 'lowerBoundField']
tTKTopologicalSimplification1Display.LookupTable = lowerBoundFieldLUT
tTKTopologicalSimplification1Display.Specular = 1.0
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'OutputOffsetScalarField'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.ScaleFactor = 51.2
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.CustomShader = ''
tTKTopologicalSimplification1Display.SetScaleArray = ['POINTS', 'OutputOffsetScalarField']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = ['POINTS', 'OutputOffsetScalarField']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification1Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification1Display.ScalarOpacityFunction = lowerBoundFieldPWF
tTKTopologicalSimplification1Display.ScalarOpacityUnitDistance = 12.7980364308879

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTopologicalSimplification1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification1Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from minima
minimaDisplay = Show(minima, lowerBound)

# trace defaults for the display properties.
minimaDisplay.Representation = 'Surface'
minimaDisplay.ColorArrayName = [None, '']
minimaDisplay.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
minimaDisplay.Specular = 1.0
minimaDisplay.OSPRayScaleArray = 'CriticalIndex'
minimaDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
minimaDisplay.ScaleFactor = 51.0972666025162
minimaDisplay.GlyphType = 'Arrow'
minimaDisplay.CustomShader = ''
minimaDisplay.SetScaleArray = ['POINTS', 'CriticalIndex']
minimaDisplay.ScaleTransferFunction = 'PiecewiseFunction'
minimaDisplay.OpacityArray = ['POINTS', 'CriticalIndex']
minimaDisplay.OpacityTransferFunction = 'PiecewiseFunction'
minimaDisplay.DataAxesGrid = 'GridAxesRepresentation'
minimaDisplay.SelectionCellLabelFontFile = ''
minimaDisplay.SelectionPointLabelFontFile = ''
minimaDisplay.PolarAxes = 'PolarAxesRepresentation'
minimaDisplay.ScalarOpacityUnitDistance = 15.6296178138793

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
minimaDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
minimaDisplay.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
minimaDisplay.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
minimaDisplay.DataAxesGrid.XTitleFontFile = ''
minimaDisplay.DataAxesGrid.YTitleFontFile = ''
minimaDisplay.DataAxesGrid.ZTitleFontFile = ''
minimaDisplay.DataAxesGrid.XLabelFontFile = ''
minimaDisplay.DataAxesGrid.YLabelFontFile = ''
minimaDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
minimaDisplay.PolarAxes.PolarAxisTitleFontFile = ''
minimaDisplay.PolarAxes.PolarAxisLabelFontFile = ''
minimaDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
minimaDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from maxima
maximaDisplay = Show(maxima, lowerBound)

# trace defaults for the display properties.
maximaDisplay.Representation = 'Surface'
maximaDisplay.ColorArrayName = [None, '']
maximaDisplay.DiffuseColor = [0.0, 0.431372549019608, 0.0]
maximaDisplay.Specular = 1.0
maximaDisplay.OSPRayScaleArray = 'CriticalIndex'
maximaDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
maximaDisplay.ScaleFactor = 48.7972665786743
maximaDisplay.GlyphType = 'Arrow'
maximaDisplay.CustomShader = ''
maximaDisplay.SetScaleArray = ['POINTS', 'CriticalIndex']
maximaDisplay.ScaleTransferFunction = 'PiecewiseFunction'
maximaDisplay.OpacityArray = ['POINTS', 'CriticalIndex']
maximaDisplay.OpacityTransferFunction = 'PiecewiseFunction'
maximaDisplay.DataAxesGrid = 'GridAxesRepresentation'
maximaDisplay.SelectionCellLabelFontFile = ''
maximaDisplay.SelectionPointLabelFontFile = ''
maximaDisplay.PolarAxes = 'PolarAxesRepresentation'
maximaDisplay.ScalarOpacityUnitDistance = 14.940266242078

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maximaDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maximaDisplay.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maximaDisplay.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
maximaDisplay.DataAxesGrid.XTitleFontFile = ''
maximaDisplay.DataAxesGrid.YTitleFontFile = ''
maximaDisplay.DataAxesGrid.ZTitleFontFile = ''
maximaDisplay.DataAxesGrid.XLabelFontFile = ''
maximaDisplay.DataAxesGrid.YLabelFontFile = ''
maximaDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
maximaDisplay.PolarAxes.PolarAxisTitleFontFile = ''
maximaDisplay.PolarAxes.PolarAxisLabelFontFile = ''
maximaDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
maximaDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'mandatoryJoinTree'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint5
tTKSphereFromPoint5Display = Show(tTKSphereFromPoint5, mandatoryJoinTree)

# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')
typeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
typeLUT.ColorSpace = 'RGB'
typeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
typeLUT.NanColor = [0.0, 0.0, 0.0]
typeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint5Display.Representation = 'Surface'
tTKSphereFromPoint5Display.ColorArrayName = ['POINTS', 'Type']
tTKSphereFromPoint5Display.LookupTable = typeLUT
tTKSphereFromPoint5Display.Specular = 1.0
tTKSphereFromPoint5Display.OSPRayScaleArray = 'ComponentId'
tTKSphereFromPoint5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.ScaleFactor = 0.199658444523811
tTKSphereFromPoint5Display.GlyphType = 'Arrow'
tTKSphereFromPoint5Display.CustomShader = ''
tTKSphereFromPoint5Display.SetScaleArray = ['POINTS', 'ComponentId']
tTKSphereFromPoint5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.OpacityArray = ['POINTS', 'ComponentId']
tTKSphereFromPoint5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint5Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint5Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint5Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint5Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube5
tube5Display = Show(tube5, mandatoryJoinTree)

# trace defaults for the display properties.
tube5Display.Representation = 'Surface'
tube5Display.ColorArrayName = [None, '']
tube5Display.Specular = 1.0
tube5Display.OSPRayScaleArray = 'ComponentId'
tube5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube5Display.ScaleFactor = 0.101655348390341
tube5Display.GlyphType = 'Arrow'
tube5Display.CustomShader = ''
tube5Display.SetScaleArray = ['POINTS', 'ComponentId']
tube5Display.ScaleTransferFunction = 'PiecewiseFunction'
tube5Display.OpacityArray = ['POINTS', 'ComponentId']
tube5Display.OpacityTransferFunction = 'PiecewiseFunction'
tube5Display.DataAxesGrid = 'GridAxesRepresentation'
tube5Display.SelectionCellLabelFontFile = ''
tube5Display.SelectionPointLabelFontFile = ''
tube5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube5Display.DataAxesGrid.XTitleFontFile = ''
tube5Display.DataAxesGrid.YTitleFontFile = ''
tube5Display.DataAxesGrid.ZTitleFontFile = ''
tube5Display.DataAxesGrid.XLabelFontFile = ''
tube5Display.DataAxesGrid.YLabelFontFile = ''
tube5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube5Display.PolarAxes.PolarAxisTitleFontFile = ''
tube5Display.PolarAxes.PolarAxisLabelFontFile = ''
tube5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'mandatoryMaxima'
# ----------------------------------------------------------------

# show data from threshold2
threshold2Display = Show(threshold2, mandatoryMaxima)

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', '']
threshold2Display.DiffuseColor = [0.0, 0.431372549019608, 0.0]
threshold2Display.Specular = 1.0
threshold2Display.OSPRayScaleArray = 'MaximumComponents'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.ScaleFactor = 45.4
threshold2Display.GlyphType = 'Arrow'
threshold2Display.CustomShader = ''
threshold2Display.SetScaleArray = ['POINTS', 'MaximumComponents']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'MaximumComponents']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.SelectionCellLabelFontFile = ''
threshold2Display.SelectionPointLabelFontFile = ''
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityUnitDistance = 48.0155243565443

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold2Display.DataAxesGrid.XTitleFontFile = ''
threshold2Display.DataAxesGrid.YTitleFontFile = ''
threshold2Display.DataAxesGrid.ZTitleFontFile = ''
threshold2Display.DataAxesGrid.XLabelFontFile = ''
threshold2Display.DataAxesGrid.YLabelFontFile = ''
threshold2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold2Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold2Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold2Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tetrahedralize1
tetrahedralize1Display = Show(tetrahedralize1, mandatoryMaxima)

# trace defaults for the display properties.
tetrahedralize1Display.Representation = 'Surface'
tetrahedralize1Display.ColorArrayName = ['POINTS', 'lowerBoundField']
tetrahedralize1Display.LookupTable = lowerBoundFieldLUT
tetrahedralize1Display.Opacity = 0.3
tetrahedralize1Display.Specular = 1.0
tetrahedralize1Display.OSPRayScaleArray = 'lowerBoundField'
tetrahedralize1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tetrahedralize1Display.ScaleFactor = 51.2
tetrahedralize1Display.GlyphType = 'Arrow'
tetrahedralize1Display.CustomShader = ''
tetrahedralize1Display.SetScaleArray = ['POINTS', 'lowerBoundField']
tetrahedralize1Display.ScaleTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display.OpacityArray = ['POINTS', 'lowerBoundField']
tetrahedralize1Display.OpacityTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display.DataAxesGrid = 'GridAxesRepresentation'
tetrahedralize1Display.SelectionCellLabelFontFile = ''
tetrahedralize1Display.SelectionPointLabelFontFile = ''
tetrahedralize1Display.PolarAxes = 'PolarAxesRepresentation'
tetrahedralize1Display.ScalarOpacityFunction = lowerBoundFieldPWF
tetrahedralize1Display.ScalarOpacityUnitDistance = 12.7980364308879

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tetrahedralize1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tetrahedralize1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tetrahedralize1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tetrahedralize1Display.DataAxesGrid.XTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.YTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.ZTitleFontFile = ''
tetrahedralize1Display.DataAxesGrid.XLabelFontFile = ''
tetrahedralize1Display.DataAxesGrid.YLabelFontFile = ''
tetrahedralize1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tetrahedralize1Display.PolarAxes.PolarAxisTitleFontFile = ''
tetrahedralize1Display.PolarAxes.PolarAxisLabelFontFile = ''
tetrahedralize1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tetrahedralize1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'mandatoryMinima'
# ----------------------------------------------------------------

# show data from tetrahedralize1
tetrahedralize1Display_1 = Show(tetrahedralize1, mandatoryMinima)

# trace defaults for the display properties.
tetrahedralize1Display_1.Representation = 'Surface'
tetrahedralize1Display_1.ColorArrayName = ['POINTS', 'lowerBoundField']
tetrahedralize1Display_1.LookupTable = lowerBoundFieldLUT
tetrahedralize1Display_1.Opacity = 0.3
tetrahedralize1Display_1.Specular = 1.0
tetrahedralize1Display_1.OSPRayScaleArray = 'lowerBoundField'
tetrahedralize1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tetrahedralize1Display_1.ScaleFactor = 51.2
tetrahedralize1Display_1.GlyphType = 'Arrow'
tetrahedralize1Display_1.CustomShader = ''
tetrahedralize1Display_1.SetScaleArray = ['POINTS', 'lowerBoundField']
tetrahedralize1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display_1.OpacityArray = ['POINTS', 'lowerBoundField']
tetrahedralize1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tetrahedralize1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tetrahedralize1Display_1.SelectionCellLabelFontFile = ''
tetrahedralize1Display_1.SelectionPointLabelFontFile = ''
tetrahedralize1Display_1.PolarAxes = 'PolarAxesRepresentation'
tetrahedralize1Display_1.ScalarOpacityFunction = lowerBoundFieldPWF
tetrahedralize1Display_1.ScalarOpacityUnitDistance = 12.7980364308879

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tetrahedralize1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tetrahedralize1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tetrahedralize1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tetrahedralize1Display_1.DataAxesGrid.XTitleFontFile = ''
tetrahedralize1Display_1.DataAxesGrid.YTitleFontFile = ''
tetrahedralize1Display_1.DataAxesGrid.ZTitleFontFile = ''
tetrahedralize1Display_1.DataAxesGrid.XLabelFontFile = ''
tetrahedralize1Display_1.DataAxesGrid.YLabelFontFile = ''
tetrahedralize1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tetrahedralize1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tetrahedralize1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tetrahedralize1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tetrahedralize1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from transform1
transform1Display = Show(transform1, mandatoryMinima)

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = [None, '']
transform1Display.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
transform1Display.Specular = 1.0
transform1Display.OSPRayScaleArray = 'MinimumComponents'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.ScaleFactor = 47.8
transform1Display.GlyphType = 'Arrow'
transform1Display.CustomShader = ''
transform1Display.SetScaleArray = ['POINTS', 'MinimumComponents']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'MinimumComponents']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.SelectionCellLabelFontFile = ''
transform1Display.SelectionPointLabelFontFile = ''
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityUnitDistance = 49.9770767155363

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
transform1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transform1Display.DataAxesGrid.XTitleFontFile = ''
transform1Display.DataAxesGrid.YTitleFontFile = ''
transform1Display.DataAxesGrid.ZTitleFontFile = ''
transform1Display.DataAxesGrid.XLabelFontFile = ''
transform1Display.DataAxesGrid.YLabelFontFile = ''
transform1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transform1Display.PolarAxes.PolarAxisTitleFontFile = ''
transform1Display.PolarAxes.PolarAxisLabelFontFile = ''
transform1Display.PolarAxes.LastRadialAxisTextFontFile = ''
transform1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'mandatorySplitTree'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint6
tTKSphereFromPoint6Display = Show(tTKSphereFromPoint6, mandatorySplitTree)

# trace defaults for the display properties.
tTKSphereFromPoint6Display.Representation = 'Surface'
tTKSphereFromPoint6Display.ColorArrayName = ['POINTS', 'Type']
tTKSphereFromPoint6Display.LookupTable = typeLUT
tTKSphereFromPoint6Display.Specular = 1.0
tTKSphereFromPoint6Display.OSPRayScaleArray = 'ComponentId'
tTKSphereFromPoint6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.ScaleFactor = 0.199658444523811
tTKSphereFromPoint6Display.GlyphType = 'Arrow'
tTKSphereFromPoint6Display.CustomShader = ''
tTKSphereFromPoint6Display.SetScaleArray = ['POINTS', 'ComponentId']
tTKSphereFromPoint6Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.OpacityArray = ['POINTS', 'ComponentId']
tTKSphereFromPoint6Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint6Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint6Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint6Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint6Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint6Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint6Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint6Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint6Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint6Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint6Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint6Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint6Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint6Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint6Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube6
tube6Display = Show(tube6, mandatorySplitTree)

# trace defaults for the display properties.
tube6Display.Representation = 'Surface'
tube6Display.ColorArrayName = [None, '']
tube6Display.Specular = 1.0
tube6Display.OSPRayScaleArray = 'ComponentId'
tube6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube6Display.ScaleFactor = 0.101695218496025
tube6Display.GlyphType = 'Arrow'
tube6Display.CustomShader = ''
tube6Display.SetScaleArray = ['POINTS', 'ComponentId']
tube6Display.ScaleTransferFunction = 'PiecewiseFunction'
tube6Display.OpacityArray = ['POINTS', 'ComponentId']
tube6Display.OpacityTransferFunction = 'PiecewiseFunction'
tube6Display.DataAxesGrid = 'GridAxesRepresentation'
tube6Display.SelectionCellLabelFontFile = ''
tube6Display.SelectionPointLabelFontFile = ''
tube6Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube6Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube6Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube6Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube6Display.DataAxesGrid.XTitleFontFile = ''
tube6Display.DataAxesGrid.YTitleFontFile = ''
tube6Display.DataAxesGrid.ZTitleFontFile = ''
tube6Display.DataAxesGrid.XLabelFontFile = ''
tube6Display.DataAxesGrid.YLabelFontFile = ''
tube6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube6Display.PolarAxes.PolarAxisTitleFontFile = ''
tube6Display.PolarAxes.PolarAxisLabelFontFile = ''
tube6Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'peristenceDiagramLower'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, peristenceDiagramLower)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.501960784313725, 0.501960784313725, 0.501960784313725]
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'NodeType'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.ScaleFactor = 0.124955204175785
tube1Display.GlyphType = 'Arrow'
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'NodeType']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'NodeType']
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

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, peristenceDiagramLower)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')
nodeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
nodeTypeLUT.ColorSpace = 'RGB'
nodeTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
nodeTypeLUT.NanColor = [0.0, 0.0, 0.0]
nodeTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint1Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.ScaleFactor = 0.235868385434151
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.CustomShader = ''
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'NodeType']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'NodeType']
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

# show data from tube2
tube2Display = Show(tube2, peristenceDiagramLower)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'NodeType'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.ScaleFactor = 0.136209940910339
tube2Display.GlyphType = 'Arrow'
tube2Display.CustomShader = ''
tube2Display.SetScaleArray = ['POINTS', 'NodeType']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'NodeType']
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

# ----------------------------------------------------------------
# setup the visualization in view 'persistenceDiagramUpper'
# ----------------------------------------------------------------

# show data from tube3
tube3Display = Show(tube3, persistenceDiagramUpper)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.DiffuseColor = [0.501960784313725, 0.501960784313725, 0.501960784313725]
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'NodeType'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.ScaleFactor = 0.128009296022356
tube3Display.GlyphType = 'Arrow'
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', 'NodeType']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'NodeType']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.SelectionCellLabelFontFile = ''
tube3Display.SelectionPointLabelFontFile = ''
tube3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube3Display.DataAxesGrid.XTitleFontFile = ''
tube3Display.DataAxesGrid.YTitleFontFile = ''
tube3Display.DataAxesGrid.ZTitleFontFile = ''
tube3Display.DataAxesGrid.XLabelFontFile = ''
tube3Display.DataAxesGrid.YLabelFontFile = ''
tube3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube3Display.PolarAxes.PolarAxisTitleFontFile = ''
tube3Display.PolarAxes.PolarAxisLabelFontFile = ''
tube3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, persistenceDiagramUpper)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint3Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.ScaleFactor = 0.237601307034493
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.CustomShader = ''
tTKSphereFromPoint3Display.SetScaleArray = ['POINTS', 'NodeType']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = ['POINTS', 'NodeType']
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

# show data from tube4
tube4Display = Show(tube4, persistenceDiagramUpper)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = [None, '']
tube4Display.Specular = 1.0
tube4Display.OSPRayScaleArray = 'NodeType'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.ScaleFactor = 0.137942862510681
tube4Display.GlyphType = 'Arrow'
tube4Display.CustomShader = ''
tube4Display.SetScaleArray = ['POINTS', 'NodeType']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'NodeType']
tube4Display.OpacityTransferFunction = 'PiecewiseFunction'
tube4Display.DataAxesGrid = 'GridAxesRepresentation'
tube4Display.SelectionCellLabelFontFile = ''
tube4Display.SelectionPointLabelFontFile = ''
tube4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube4Display.DataAxesGrid.XTitleFontFile = ''
tube4Display.DataAxesGrid.YTitleFontFile = ''
tube4Display.DataAxesGrid.ZTitleFontFile = ''
tube4Display.DataAxesGrid.XLabelFontFile = ''
tube4Display.DataAxesGrid.YLabelFontFile = ''
tube4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube4Display.PolarAxes.PolarAxisTitleFontFile = ''
tube4Display.PolarAxes.PolarAxisLabelFontFile = ''
tube4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'upperBound'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification2
tTKTopologicalSimplification2Display = Show(tTKTopologicalSimplification2, upperBound)

# get color transfer function/color map for 'upperBoundField'
upperBoundFieldLUT = GetColorTransferFunction('upperBoundField')
upperBoundFieldLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 0.689714312553406, 0.917647, 0.941176, 0.788235, 1.37942862510681, 0.0, 0.431373, 0.0]
upperBoundFieldLUT.ColorSpace = 'RGB'
upperBoundFieldLUT.AboveRangeColor = [1.0, 1.0, 1.0]
upperBoundFieldLUT.NanColor = [0.0, 0.0, 0.0]
upperBoundFieldLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'upperBoundField'
upperBoundFieldPWF = GetOpacityTransferFunction('upperBoundField')
upperBoundFieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.37942862510681, 1.0, 0.5, 0.0]
upperBoundFieldPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKTopologicalSimplification2Display.Representation = 'Surface'
tTKTopologicalSimplification2Display.ColorArrayName = ['POINTS', 'upperBoundField']
tTKTopologicalSimplification2Display.LookupTable = upperBoundFieldLUT
tTKTopologicalSimplification2Display.Specular = 1.0
tTKTopologicalSimplification2Display.OSPRayScaleArray = 'OutputOffsetScalarField'
tTKTopologicalSimplification2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.ScaleFactor = 51.2
tTKTopologicalSimplification2Display.GlyphType = 'Arrow'
tTKTopologicalSimplification2Display.CustomShader = ''
tTKTopologicalSimplification2Display.SetScaleArray = ['POINTS', 'OutputOffsetScalarField']
tTKTopologicalSimplification2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.OpacityArray = ['POINTS', 'OutputOffsetScalarField']
tTKTopologicalSimplification2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification2Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification2Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification2Display.ScalarOpacityFunction = upperBoundFieldPWF
tTKTopologicalSimplification2Display.ScalarOpacityUnitDistance = 12.7980364308879

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTopologicalSimplification2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification2Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification2Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification2Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification2Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification2Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from minima_1
minima_1Display = Show(minima_1, upperBound)

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0000100001, 0.917647, 0.941176, 0.788235, 2.0000200002, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0000200002, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
minima_1Display.Representation = 'Surface'
minima_1Display.ColorArrayName = ['POINTS', 'CriticalIndex']
minima_1Display.LookupTable = criticalTypeLUT
minima_1Display.Specular = 1.0
minima_1Display.OSPRayScaleArray = 'CriticalIndex'
minima_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
minima_1Display.ScaleFactor = 51.8976082801819
minima_1Display.GlyphType = 'Arrow'
minima_1Display.CustomShader = ''
minima_1Display.SetScaleArray = ['POINTS', 'CriticalIndex']
minima_1Display.ScaleTransferFunction = 'PiecewiseFunction'
minima_1Display.OpacityArray = ['POINTS', 'CriticalIndex']
minima_1Display.OpacityTransferFunction = 'PiecewiseFunction'
minima_1Display.DataAxesGrid = 'GridAxesRepresentation'
minima_1Display.SelectionCellLabelFontFile = ''
minima_1Display.SelectionPointLabelFontFile = ''
minima_1Display.PolarAxes = 'PolarAxesRepresentation'
minima_1Display.ScalarOpacityFunction = criticalTypePWF
minima_1Display.ScalarOpacityUnitDistance = 14.3195579062878

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
minima_1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
minima_1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
minima_1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
minima_1Display.DataAxesGrid.XTitleFontFile = ''
minima_1Display.DataAxesGrid.YTitleFontFile = ''
minima_1Display.DataAxesGrid.ZTitleFontFile = ''
minima_1Display.DataAxesGrid.XLabelFontFile = ''
minima_1Display.DataAxesGrid.YLabelFontFile = ''
minima_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
minima_1Display.PolarAxes.PolarAxisTitleFontFile = ''
minima_1Display.PolarAxes.PolarAxisLabelFontFile = ''
minima_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
minima_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from maxima_1
maxima_1Display = Show(maxima_1, upperBound)

# trace defaults for the display properties.
maxima_1Display.Representation = 'Surface'
maxima_1Display.ColorArrayName = ['POINTS', 'CriticalIndex']
maxima_1Display.LookupTable = criticalTypeLUT
maxima_1Display.Specular = 1.0
maxima_1Display.OSPRayScaleArray = 'CriticalIndex'
maxima_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
maxima_1Display.ScaleFactor = 48.6976083755493
maxima_1Display.GlyphType = 'Arrow'
maxima_1Display.CustomShader = ''
maxima_1Display.SetScaleArray = ['POINTS', 'CriticalIndex']
maxima_1Display.ScaleTransferFunction = 'PiecewiseFunction'
maxima_1Display.OpacityArray = ['POINTS', 'CriticalIndex']
maxima_1Display.OpacityTransferFunction = 'PiecewiseFunction'
maxima_1Display.DataAxesGrid = 'GridAxesRepresentation'
maxima_1Display.SelectionCellLabelFontFile = ''
maxima_1Display.SelectionPointLabelFontFile = ''
maxima_1Display.PolarAxes = 'PolarAxesRepresentation'
maxima_1Display.ScalarOpacityFunction = criticalTypePWF
maxima_1Display.ScalarOpacityUnitDistance = 15.7427563612737

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maxima_1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maxima_1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maxima_1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
maxima_1Display.DataAxesGrid.XTitleFontFile = ''
maxima_1Display.DataAxesGrid.YTitleFontFile = ''
maxima_1Display.DataAxesGrid.ZTitleFontFile = ''
maxima_1Display.DataAxesGrid.XLabelFontFile = ''
maxima_1Display.DataAxesGrid.YLabelFontFile = ''
maxima_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
maxima_1Display.PolarAxes.PolarAxisTitleFontFile = ''
maxima_1Display.PolarAxes.PolarAxisLabelFontFile = ''
maxima_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
maxima_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')
typePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
typePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))
tTKPersistenceDiagram1.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram1, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram1.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram1)))
tTKMandatoryCriticalPoints1.DebugLevel = int(debugLevel)
if tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMandatoryCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKMandatoryCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKMandatoryCriticalPoints1)))
tTKSphereFromPoint6.DebugLevel = int(debugLevel)
if tTKSphereFromPoint6.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint6.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint6_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint6, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint6.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint6)))
tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))
tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))
tTKTopologicalSimplification1.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification1, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification1.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification1)))
tTKScalarFieldCriticalPoints1.DebugLevel = int(debugLevel)
if tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldCriticalPoints1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints1.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints1)))
tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))
tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))
tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))
tTKScalarFieldCriticalPoints2.DebugLevel = int(debugLevel)
if tTKScalarFieldCriticalPoints2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKScalarFieldCriticalPoints2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints2, i)))
else:
	SaveData(outputDirectory + 'tTKScalarFieldCriticalPoints2.vtu',
		CleantoGrid(OutputPort(tTKScalarFieldCriticalPoints2)))
tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))
