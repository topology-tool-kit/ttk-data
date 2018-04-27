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
renderView1.ViewSize = [688, 433]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.499968, 0.166656, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.499883314775085, 0.162350039723861, 10000.0]
renderView1.CameraFocalPoint = [0.499883314775085, 0.162350039723861, 0.0]
renderView1.CameraParallelScale = 0.359956659881852
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
renderView2.ViewSize = [684, 432]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.499968, 0.166656, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [0.499883314775085, 0.162350039723861, 10000.0]
renderView2.CameraFocalPoint = [0.499883314775085, 0.162350039723861, 0.0]
renderView2.CameraParallelScale = 0.359956659881852
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
renderView3.ViewSize = [306, 433]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.85692298412323, 0.877376973628998, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [0.822069823502881, 0.756160989474757, 4.73852511539386]
renderView3.CameraFocalPoint = [0.822069823502881, 0.756160989474757, 0.0]
renderView3.CameraParallelScale = 1.48396886012827
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1
renderView3.AxesGrid.XTitle = 'Birth'
renderView3.AxesGrid.YTitle = 'Death'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [310, 432]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.85692298412323, 0.877376973628998, 0.0]
renderView4.StereoType = 0
renderView4.CameraPosition = [0.822069823502881, 0.756160989474757, 4.73852511539386]
renderView4.CameraFocalPoint = [0.822069823502881, 0.756160989474757, 0.0]
renderView4.CameraParallelScale = 1.48396886012827
renderView4.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView4.AxesGrid.Visibility = 1
renderView4.AxesGrid.XTitle = 'Birth'
renderView4.AxesGrid.YTitle = 'Death'
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
uncertainStartingVortexvti = XMLImageDataReader(FileName=['uncertainStartingVortex.vti'])
uncertainStartingVortexvti.PointArrayStatus = ['lowerBoundField', 'upperBoundField']

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(Input=uncertainStartingVortexvti)
randomAttributes1.DataType = 'Double'
randomAttributes1.ComponentRange = [0.0, 0.999]
randomAttributes1.GeneratePointScalars = 1
randomAttributes1.GenerateCellVectors = 0

# create a new 'Calculator'
calculator1 = Calculator(Input=randomAttributes1)
calculator1.ResultArrayName = 'realization0'
calculator1.Function = 'lowerBoundField+(upperBoundField-lowerBoundField)*RandomPointScalars'

# create a new 'Random Attributes'
randomAttributes2 = RandomAttributes(Input=calculator1)
randomAttributes2.DataType = 'Float'
randomAttributes2.ComponentRange = [0.0, 1.0]
randomAttributes2.GeneratePointScalars = 1
randomAttributes2.GenerateCellVectors = 0

# create a new 'Calculator'
calculator2 = Calculator(Input=randomAttributes2)
calculator2.ResultArrayName = 'realization1'
calculator2.Function = 'lowerBoundField+(upperBoundField-lowerBoundField)*RandomPointScalars'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=calculator2)
tTKPersistenceDiagram2.ScalarField = 'realization1'
tTKPersistenceDiagram2.InputOffsetField = ''

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram2)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=threshold3)

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram2)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [0.0, 185964.0]

# create a new 'Threshold'
persistenceThreshold2 = Threshold(Input=threshold4)
persistenceThreshold2.Scalars = ['CELLS', 'Persistence']
persistenceThreshold2.ThresholdRange = [0.05, 1.77902963800645]

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=persistenceThreshold2)
tTKSphereFromPoint3.Radius = 0.025
tTKSphereFromPoint3.ThetaResolution = 8
tTKSphereFromPoint3.PhiResolution = 8

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=persistenceThreshold2)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=calculator2,
    Constraints=persistenceThreshold2)
tTKTopologicalSimplification2.ScalarField = 'realization1'
tTKTopologicalSimplification2.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints2 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification2)
tTKScalarFieldCriticalPoints2.ScalarField = 'realization1'
tTKScalarFieldCriticalPoints2.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints2.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints2)
tTKSphereFromPoint4.Radius = 0.002
tTKSphereFromPoint4.ThetaResolution = 8
tTKSphereFromPoint4.PhiResolution = 8

# create a new 'TTK MandatoryCriticalPoints'
tTKMandatoryCriticalPoints1 = TTKMandatoryCriticalPoints(Input=uncertainStartingVortexvti)
tTKMandatoryCriticalPoints1.LowerBoundField = 'lowerBoundField'
tTKMandatoryCriticalPoints1.UpperBoundField = 'upperBoundField'
tTKMandatoryCriticalPoints1.NormalizedThreshold = 0.02

# create a new 'Threshold'
threshold6 = Threshold(Input=tTKMandatoryCriticalPoints1)
threshold6.Scalars = ['POINTS', 'MinimumComponents']
threshold6.ThresholdRange = [0.0, 2.0]

# find source
tTKMandatoryCriticalPoints1_1 = FindSource('TTKMandatoryCriticalPoints1')

# create a new 'Threshold'
threshold5 = Threshold(Input=OutputPort(tTKMandatoryCriticalPoints1_1,3))
threshold5.Scalars = ['POINTS', 'MaximumComponents']
threshold5.ThresholdRange = [0.0, 8.0]

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'NodeType']
tube4.Vectors = [None, '']
tube4.Radius = 0.01

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'NodeType']
tube3.Vectors = [None, '']
tube3.Radius = 0.015

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=calculator1)
tTKPersistenceDiagram1.ScalarField = 'realization0'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold2 = Threshold(Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [0.0, 185374.0]

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold2)
persistenceThreshold1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold1.ThresholdRange = [0.05, 1.75475390406744]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=persistenceThreshold1)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = [None, '']
tube2.Radius = 0.01

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold1)
tTKSphereFromPoint1.Radius = 0.025
tTKSphereFromPoint1.ThetaResolution = 8
tTKSphereFromPoint1.PhiResolution = 8

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=calculator1,
    Constraints=persistenceThreshold1)
tTKTopologicalSimplification1.ScalarField = 'realization0'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(Input=tTKTopologicalSimplification1)
tTKScalarFieldCriticalPoints1.ScalarField = 'realization0'
tTKScalarFieldCriticalPoints1.UseInputOffsetField = 1
tTKScalarFieldCriticalPoints1.Withvertexscalars = 0

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKScalarFieldCriticalPoints1)
tTKSphereFromPoint2.Radius = 0.002
tTKSphereFromPoint2.ThetaResolution = 8
tTKSphereFromPoint2.PhiResolution = 8

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'NodeType']
tube1.Vectors = [None, '']
tube1.Radius = 0.015

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator2
calculator2Display = Show(calculator2, renderView1)

# get color transfer function/color map for 'realization1'
realization1LUT = GetColorTransferFunction('realization1')
realization1LUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 1.77902963800645, 1.0, 1.0, 1.0]
realization1LUT.ColorSpace = 'RGB'
realization1LUT.AboveRangeColor = [1.0, 1.0, 1.0]
realization1LUT.NanColor = [1.0, 0.0, 0.0]
realization1LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'realization1'
realization1PWF = GetOpacityTransferFunction('realization1')
realization1PWF.Points = [0.0, 0.0, 0.5, 0.0, 1.77902963800645, 1.0, 0.5, 0.0]
realization1PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Slice'
calculator2Display.ColorArrayName = ['POINTS', 'realization1']
calculator2Display.LookupTable = realization1LUT
calculator2Display.OSPRayScaleArray = 'realization1'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'None'
calculator2Display.ScaleFactor = 0.0999936
calculator2Display.SelectScaleArray = 'realization1'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.SetScaleArray = [None, '']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = [None, '']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.SelectionCellLabelFontFile = ''
calculator2Display.SelectionPointLabelFontFile = ''
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 0.0114190653221319
calculator2Display.ScalarOpacityFunction = realization1PWF

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator2Display.DataAxesGrid.XTitleFontFile = ''
calculator2Display.DataAxesGrid.YTitleFontFile = ''
calculator2Display.DataAxesGrid.ZTitleFontFile = ''
calculator2Display.DataAxesGrid.XLabelFontFile = ''
calculator2Display.DataAxesGrid.YLabelFontFile = ''
calculator2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator2Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator2Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator2Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKTopologicalSimplification1
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView1)

# get color transfer function/color map for 'realization0'
realization0LUT = GetColorTransferFunction('realization0')
realization0LUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 1.75475390406744, 1.0, 1.0, 1.0]
realization0LUT.ColorSpace = 'RGB'
realization0LUT.AboveRangeColor = [1.0, 1.0, 1.0]
realization0LUT.NanColor = [1.0, 0.0, 0.0]
realization0LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'realization0'
realization0PWF = GetOpacityTransferFunction('realization0')
realization0PWF.Points = [0.0, 0.0, 0.5, 0.0, 1.75475390406744, 1.0, 0.5, 0.0]
realization0PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Slice'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', 'realization0']
tTKTopologicalSimplification1Display.LookupTable = realization0LUT
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'realization0'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification1Display.ScaleFactor = 0.0999936
tTKTopologicalSimplification1Display.SelectScaleArray = 'realization0'
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.SetScaleArray = [None, '']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = [None, '']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification1Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification1Display.ScalarOpacityUnitDistance = 0.0114190653221319
tTKTopologicalSimplification1Display.ScalarOpacityFunction = realization0PWF

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTopologicalSimplification1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from tTKSphereFromPoint2
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView1)

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.129412, 0.584314, 1.0, 0.917647, 0.941176, 0.788235, 2.0, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint2Display.LookupTable = criticalTypeLUT
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.SpecularPower = 50.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'CriticalIndex'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'CriticalIndex'
tTKSphereFromPoint2Display.ScaleFactor = 0.180755689740181
tTKSphereFromPoint2Display.SelectScaleArray = 'CriticalIndex'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GaussianRadius = 0.0903778448700905
tTKSphereFromPoint2Display.CustomShader = ''
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint2Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint2Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from threshold5
threshold5Display = Show(threshold5, renderView1)

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = ['POINTS', '']
threshold5Display.DiffuseColor = [0.0, 0.431372549019608, 0.0]
threshold5Display.Specular = 1.0
threshold5Display.OSPRayScaleArray = 'MaximumComponents'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'MaximumComponents'
threshold5Display.ScaleFactor = 0.0791615977883339
threshold5Display.SelectScaleArray = 'MaximumComponents'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GaussianRadius = 0.0395807988941669
threshold5Display.CustomShader = ''
threshold5Display.SetScaleArray = ['POINTS', 'MaximumComponents']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'MaximumComponents']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.SelectionCellLabelFontFile = ''
threshold5Display.SelectionPointLabelColor = [0.5, 0.5, 0.5]
threshold5Display.SelectionPointLabelFontFile = ''
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityUnitDistance = 0.0340987741502776

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold5Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold5Display.DataAxesGrid.XTitleFontFile = ''
threshold5Display.DataAxesGrid.YTitleFontFile = ''
threshold5Display.DataAxesGrid.ZTitleFontFile = ''
threshold5Display.DataAxesGrid.XLabelFontFile = ''
threshold5Display.DataAxesGrid.YLabelFontFile = ''
threshold5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold5Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold5Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold5Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold6
threshold6Display = Show(threshold6, renderView1)

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['POINTS', '']
threshold6Display.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
threshold6Display.Specular = 1.0
threshold6Display.OSPRayScaleArray = 'MinimumComponents'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'MinimumComponents'
threshold6Display.ScaleFactor = 0.0831977978348732
threshold6Display.SelectScaleArray = 'MinimumComponents'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GaussianRadius = 0.0415988989174366
threshold6Display.CustomShader = ''
threshold6Display.SetScaleArray = ['POINTS', 'MinimumComponents']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'MinimumComponents']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.SelectionCellLabelFontFile = ''
threshold6Display.SelectionPointLabelColor = [0.5, 0.5, 0.5]
threshold6Display.SelectionPointLabelFontFile = ''
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityUnitDistance = 0.0287776491219126

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold6Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold6Display.DataAxesGrid.XTitleFontFile = ''
threshold6Display.DataAxesGrid.YTitleFontFile = ''
threshold6Display.DataAxesGrid.ZTitleFontFile = ''
threshold6Display.DataAxesGrid.XLabelFontFile = ''
threshold6Display.DataAxesGrid.YLabelFontFile = ''
threshold6Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold6Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold6Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold6Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold6Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification2
tTKTopologicalSimplification2Display = Show(tTKTopologicalSimplification2, renderView2)

# trace defaults for the display properties.
tTKTopologicalSimplification2Display.Representation = 'Slice'
tTKTopologicalSimplification2Display.ColorArrayName = ['POINTS', 'realization1']
tTKTopologicalSimplification2Display.LookupTable = realization1LUT
tTKTopologicalSimplification2Display.OSPRayScaleArray = 'realization1'
tTKTopologicalSimplification2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification2Display.ScaleFactor = 0.0999936
tTKTopologicalSimplification2Display.SelectScaleArray = 'realization1'
tTKTopologicalSimplification2Display.GlyphType = 'Arrow'
tTKTopologicalSimplification2Display.SetScaleArray = [None, '']
tTKTopologicalSimplification2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.OpacityArray = [None, '']
tTKTopologicalSimplification2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification2Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification2Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification2Display.ScalarOpacityUnitDistance = 0.0114190653221319
tTKTopologicalSimplification2Display.ScalarOpacityFunction = realization1PWF

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKTopologicalSimplification2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from tTKSphereFromPoint4
tTKSphereFromPoint4Display = Show(tTKSphereFromPoint4, renderView2)

# trace defaults for the display properties.
tTKSphereFromPoint4Display.Representation = 'Surface'
tTKSphereFromPoint4Display.ColorArrayName = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint4Display.LookupTable = criticalTypeLUT
tTKSphereFromPoint4Display.Specular = 1.0
tTKSphereFromPoint4Display.SpecularPower = 50.0
tTKSphereFromPoint4Display.OSPRayScaleArray = 'CriticalIndex'
tTKSphereFromPoint4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.SelectOrientationVectors = 'CriticalIndex'
tTKSphereFromPoint4Display.ScaleFactor = 0.0933376729488373
tTKSphereFromPoint4Display.SelectScaleArray = 'CriticalIndex'
tTKSphereFromPoint4Display.GlyphType = 'Arrow'
tTKSphereFromPoint4Display.GaussianRadius = 0.0466688364744186
tTKSphereFromPoint4Display.CustomShader = ''
tTKSphereFromPoint4Display.SetScaleArray = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.OpacityArray = ['POINTS', 'CriticalIndex']
tTKSphereFromPoint4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint4Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint4Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKSphereFromPoint4Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint4Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint4Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint4Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint4Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold6
threshold6Display_1 = Show(threshold6, renderView2)

# trace defaults for the display properties.
threshold6Display_1.Representation = 'Surface'
threshold6Display_1.ColorArrayName = [None, '']
threshold6Display_1.DiffuseColor = [0.0, 0.129411764705882, 0.584313725490196]
threshold6Display_1.Specular = 1.0
threshold6Display_1.OSPRayScaleArray = 'MinimumComponents'
threshold6Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display_1.SelectOrientationVectors = 'MinimumComponents'
threshold6Display_1.ScaleFactor = 0.0831977978348732
threshold6Display_1.SelectScaleArray = 'MinimumComponents'
threshold6Display_1.GlyphType = 'Arrow'
threshold6Display_1.GaussianRadius = 0.0415988989174366
threshold6Display_1.CustomShader = ''
threshold6Display_1.SetScaleArray = ['POINTS', 'MinimumComponents']
threshold6Display_1.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display_1.OpacityArray = ['POINTS', 'MinimumComponents']
threshold6Display_1.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display_1.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display_1.SelectionCellLabelFontFile = ''
threshold6Display_1.SelectionPointLabelColor = [0.5, 0.5, 0.5]
threshold6Display_1.SelectionPointLabelFontFile = ''
threshold6Display_1.PolarAxes = 'PolarAxesRepresentation'
threshold6Display_1.ScalarOpacityUnitDistance = 0.0287776491219126

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold6Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold6Display_1.DataAxesGrid.XTitleFontFile = ''
threshold6Display_1.DataAxesGrid.YTitleFontFile = ''
threshold6Display_1.DataAxesGrid.ZTitleFontFile = ''
threshold6Display_1.DataAxesGrid.XLabelFontFile = ''
threshold6Display_1.DataAxesGrid.YLabelFontFile = ''
threshold6Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold6Display_1.PolarAxes.PolarAxisTitleFontFile = ''
threshold6Display_1.PolarAxes.PolarAxisLabelFontFile = ''
threshold6Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
threshold6Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold5
threshold5Display_1 = Show(threshold5, renderView2)

# trace defaults for the display properties.
threshold5Display_1.Representation = 'Surface'
threshold5Display_1.ColorArrayName = [None, '']
threshold5Display_1.DiffuseColor = [0.0, 0.431372549019608, 0.0]
threshold5Display_1.Specular = 1.0
threshold5Display_1.OSPRayScaleArray = 'MaximumComponents'
threshold5Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display_1.SelectOrientationVectors = 'MaximumComponents'
threshold5Display_1.ScaleFactor = 0.0791615977883339
threshold5Display_1.SelectScaleArray = 'MaximumComponents'
threshold5Display_1.GlyphType = 'Arrow'
threshold5Display_1.GaussianRadius = 0.0395807988941669
threshold5Display_1.CustomShader = ''
threshold5Display_1.SetScaleArray = ['POINTS', 'MaximumComponents']
threshold5Display_1.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display_1.OpacityArray = ['POINTS', 'MaximumComponents']
threshold5Display_1.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display_1.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display_1.SelectionCellLabelFontFile = ''
threshold5Display_1.SelectionPointLabelColor = [0.5, 0.5, 0.5]
threshold5Display_1.SelectionPointLabelFontFile = ''
threshold5Display_1.PolarAxes = 'PolarAxesRepresentation'
threshold5Display_1.ScalarOpacityUnitDistance = 0.0340987741502776

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold5Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold5Display_1.DataAxesGrid.XTitleFontFile = ''
threshold5Display_1.DataAxesGrid.YTitleFontFile = ''
threshold5Display_1.DataAxesGrid.ZTitleFontFile = ''
threshold5Display_1.DataAxesGrid.XLabelFontFile = ''
threshold5Display_1.DataAxesGrid.YLabelFontFile = ''
threshold5Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold5Display_1.PolarAxes.PolarAxisTitleFontFile = ''
threshold5Display_1.PolarAxes.PolarAxisLabelFontFile = ''
threshold5Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
threshold5Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, renderView3)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube1Display.Specular = 1.0
tube1Display.SpecularPower = 50.0
tube1Display.OSPRayScaleArray = 'NodeType'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'NodeType'
tube1Display.ScaleFactor = 0.173483615554869
tube1Display.SelectScaleArray = 'NodeType'
tube1Display.GlyphType = 'Arrow'
tube1Display.GaussianRadius = 0.0867418077774346
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
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView3)

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
tTKSphereFromPoint1Display.SpecularPower = 50.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint1Display.ScaleFactor = 0.262077924609184
tTKSphereFromPoint1Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GaussianRadius = 0.131038962304592
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
tube2Display = Show(tube2, renderView3)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Specular = 1.0
tube2Display.SpecularPower = 50.0
tube2Display.OSPRayScaleArray = 'NodeType'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'NodeType'
tube2Display.ScaleFactor = 0.1754753947258
tube2Display.SelectScaleArray = 'NodeType'
tube2Display.GlyphType = 'Arrow'
tube2Display.GaussianRadius = 0.0877376973628998
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
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from tube3
tube3Display = Show(tube3, renderView4)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
tube3Display.Specular = 1.0
tube3Display.SpecularPower = 50.0
tube3Display.OSPRayScaleArray = 'NodeType'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'NodeType'
tube3Display.ScaleFactor = 0.17273921109736
tube3Display.SelectScaleArray = 'NodeType'
tube3Display.GlyphType = 'Arrow'
tube3Display.GaussianRadius = 0.0863696055486798
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
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView4)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = ['POINTS', 'NodeType']
tTKSphereFromPoint3Display.LookupTable = nodeTypeLUT
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.SpecularPower = 50.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'NodeType'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint3Display.ScaleFactor = 0.187652235105634
tTKSphereFromPoint3Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GaussianRadius = 0.0938261175528169
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
tube4Display = Show(tube4, renderView4)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = [None, '']
tube4Display.Specular = 1.0
tube4Display.SpecularPower = 50.0
tube4Display.OSPRayScaleArray = 'NodeType'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'NodeType'
tube4Display.ScaleFactor = 0.177902960777283
tube4Display.SelectScaleArray = 'NodeType'
tube4Display.GlyphType = 'Arrow'
tube4Display.GaussianRadius = 0.0889514803886414
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
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------