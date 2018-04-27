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
renderView1.ViewSize = [651, 867]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [127.5, 127.5, 127.5]
renderView1.StereoType = 0
renderView1.CameraPosition = [-481.040396583351, 192.194532754214, 615.07361707245]
renderView1.CameraFocalPoint = [188.360424774964, 121.400750999691, 90.7449109002209]
renderView1.CameraViewUp = [-0.291930422572635, -0.923732472389515, -0.247981748985116]
renderView1.CameraParallelScale = 220.836477965032
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
renderView2.ViewSize = [368, 415]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [127.5, 127.5, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [97.6538449081972, 130.109594922231, 10000.0]
renderView2.CameraFocalPoint = [97.6538449081972, 130.109594922231, 0.0]
renderView2.CameraParallelScale = 187.492365734508
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1
renderView2.AxesGrid.XTitle = 'Birth'
renderView2.AxesGrid.YTitle = 'Death'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.GridColor = [0.301960784313725, 0.294117647058824, 0.294117647058824]
renderView2.AxesGrid.ShowGrid = 1
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [368, 414]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [127.5, 127.5, 127.5]
renderView3.StereoType = 0
renderView3.CameraPosition = [-368.019315468219, 242.775265331142, 345.109430362964]
renderView3.CameraFocalPoint = [71.1086303627937, 166.530320737749, 162.555083107376]
renderView3.CameraViewUp = [-0.254110800388195, -0.942362488045729, -0.217670949486456]
renderView3.CameraParallelScale = 220.836477965032
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.XLabelFontFile = ''
renderView3.AxesGrid.YLabelFontFile = ''
renderView3.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
ctBonesvti = XMLImageDataReader(FileName=['ctBones.vti'])
ctBonesvti.PointArrayStatus = ['Scalars_']

# create a new 'Clip'
clip1 = Clip(Input=ctBonesvti)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Scalars_']
clip1.Value = 127.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [131.012324886831, 123.987675113169, 127.5]
clip1.ClipType.Normal = [-0.707106781186548, 0.707106781186548, 0.0]

# create a new 'Contour'
contour1 = Contour(Input=ctBonesvti)
contour1.ContourBy = ['POINTS', 'Scalars_']
contour1.Isosurfaces = [12.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=ctBonesvti)
tTKPersistenceDiagram1.ScalarField = 'Scalars_'
tTKPersistenceDiagram1.InputOffsetField = ''

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKPersistenceDiagram1)
threshold4.Scalars = ['CELLS', 'PairIdentifier']
threshold4.ThresholdRange = [-1.0, -0.1]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold4)

# create a new 'Tube'
diagonal = Tube(Input=extractSurface2)
diagonal.Scalars = ['POINTS', 'NodeType']
diagonal.Vectors = ['POINTS', 'Coordinates']
diagonal.Radius = 1.5

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 345450.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [180.0, 255.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=ctBonesvti,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = 'Scalars_'
tTKTopologicalSimplification1.InputOffsetField = ''

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(Input=tTKTopologicalSimplification1)
tTKMergeandContourTreeFTM1.ScalarField = 'Scalars_'
tTKMergeandContourTreeFTM1.UseInputOffsetScalarField = 1
tTKMergeandContourTreeFTM1.InputOffset = 'OutputOffsetScalarField'
tTKMergeandContourTreeFTM1.TreeType = 'Split   Tree'

# find source
tTKMergeandContourTreeFTM1_1 = FindSource('TTKMergeandContourTreeFTM1')

# create a new 'Threshold'
threshold3 = Threshold(Input=OutputPort(tTKMergeandContourTreeFTM1_1,2))
threshold3.Scalars = ['POINTS', 'RegionType']
threshold3.ThresholdRange = [1.0, 1.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold3)

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=extractSurface1)
tTKGeometrySmoother1.IterationNumber = 3
tTKGeometrySmoother1.InputMaskField = 'RegionType'

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=tTKGeometrySmoother1)

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=persistenceThreshold)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface3)
tube2.Scalars = ['POINTS', 'NodeType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 1.5

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=persistenceThreshold)
tTKSphereFromPoint1.Radius = 5.0

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKMergeandContourTreeFTM1_1
tTKMergeandContourTreeFTM1Display = Show(OutputPort(tTKMergeandContourTreeFTM1, 2), renderView1)

# trace defaults for the display properties.
tTKMergeandContourTreeFTM1Display.Representation = 'Outline'
tTKMergeandContourTreeFTM1Display.ColorArrayName = ['POINTS', '']
tTKMergeandContourTreeFTM1Display.OSPRayScaleArray = 'Scalars_'
tTKMergeandContourTreeFTM1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMergeandContourTreeFTM1Display.SelectOrientationVectors = 'None'
tTKMergeandContourTreeFTM1Display.ScaleFactor = 25.5
tTKMergeandContourTreeFTM1Display.SelectScaleArray = 'Scalars_'
tTKMergeandContourTreeFTM1Display.GlyphType = 'Arrow'
tTKMergeandContourTreeFTM1Display.GlyphTableIndexArray = 'Scalars_'
tTKMergeandContourTreeFTM1Display.SetScaleArray = [None, '']
tTKMergeandContourTreeFTM1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMergeandContourTreeFTM1Display.OpacityArray = [None, '']
tTKMergeandContourTreeFTM1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMergeandContourTreeFTM1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMergeandContourTreeFTM1Display.SelectionCellLabelFontFile = ''
tTKMergeandContourTreeFTM1Display.SelectionPointLabelFontFile = ''
tTKMergeandContourTreeFTM1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMergeandContourTreeFTM1Display.ScalarOpacityUnitDistance = 1.73205080756888
tTKMergeandContourTreeFTM1Display.Slice = 127

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMergeandContourTreeFTM1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMergeandContourTreeFTM1Display.DataAxesGrid.XTitleFontFile = ''
tTKMergeandContourTreeFTM1Display.DataAxesGrid.YTitleFontFile = ''
tTKMergeandContourTreeFTM1Display.DataAxesGrid.ZTitleFontFile = ''
tTKMergeandContourTreeFTM1Display.DataAxesGrid.XLabelFontFile = ''
tTKMergeandContourTreeFTM1Display.DataAxesGrid.YLabelFontFile = ''
tTKMergeandContourTreeFTM1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMergeandContourTreeFTM1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMergeandContourTreeFTM1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMergeandContourTreeFTM1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMergeandContourTreeFTM1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)

# get color transfer function/color map for 'SegmentationId'
segmentationIdLUT = GetColorTransferFunction('SegmentationId')
segmentationIdLUT.RGBPoints = [0.0, 0.278431372549, 0.278431372549, 0.858823529412, 0.572, 0.0, 0.0, 0.360784313725, 1.14, 0.0, 1.0, 1.0, 1.716, 0.0, 0.501960784314, 0.0, 2.284, 1.0, 1.0, 0.0, 2.856, 1.0, 0.380392156863, 0.0, 3.428, 0.419607843137, 0.0, 0.0, 4.0, 0.878431372549, 0.301960784314, 0.301960784314]
segmentationIdLUT.ColorSpace = 'RGB'
segmentationIdLUT.AboveRangeColor = [1.0, 1.0, 1.0]
segmentationIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = ['POINTS', 'SegmentationId']
generateSurfaceNormals1Display.LookupTable = segmentationIdLUT
generateSurfaceNormals1Display.Specular = 1.0
generateSurfaceNormals1Display.OSPRayScaleArray = 'Scalars_'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'None'
generateSurfaceNormals1Display.ScaleFactor = 23.5840287391096
generateSurfaceNormals1Display.SelectScaleArray = 'Scalars_'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'Scalars_'
generateSurfaceNormals1Display.GaussianRadius = 11.7920143695548
generateSurfaceNormals1Display.CustomShader = ''
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'Scalars_']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'Scalars_']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

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

# show data from contour1
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.Opacity = 0.04
contour1Display.Specular = 1.0
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 23.5355270385742
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = 11.7677635192871
contour1Display.CustomShader = ''
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKPersistenceDiagram1
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView2)

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'
tTKPersistenceDiagram1Display.ColorArrayName = [None, '']
tTKPersistenceDiagram1Display.Opacity = 0.2
tTKPersistenceDiagram1Display.Specular = 1.0
tTKPersistenceDiagram1Display.OSPRayScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.SelectOrientationVectors = 'Coordinates'
tTKPersistenceDiagram1Display.ScaleFactor = 25.5
tTKPersistenceDiagram1Display.SelectScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.GlyphType = 'Arrow'
tTKPersistenceDiagram1Display.GlyphTableIndexArray = 'Coordinates'
tTKPersistenceDiagram1Display.GaussianRadius = 12.75
tTKPersistenceDiagram1Display.CustomShader = ''
tTKPersistenceDiagram1Display.SetScaleArray = ['POINTS', 'NodeType']
tTKPersistenceDiagram1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.OpacityArray = ['POINTS', 'NodeType']
tTKPersistenceDiagram1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistenceDiagram1Display.SelectionCellLabelFontFile = ''
tTKPersistenceDiagram1Display.SelectionPointLabelFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistenceDiagram1Display.ScalarOpacityUnitDistance = 5.13956000821459

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistenceDiagram1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistenceDiagram1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistenceDiagram1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKPersistenceDiagram1Display.DataAxesGrid.XTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.YTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.ZTitleFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.XLabelFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.YLabelFontFile = ''
tTKPersistenceDiagram1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKPersistenceDiagram1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKPersistenceDiagram1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView2)

# get color transfer function/color map for 'NodeType'
nodeTypeLUT = GetColorTransferFunction('NodeType')
nodeTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 2.0, 0.917647, 0.941176, 0.788235, 4.0, 0.0, 0.431373, 0.0]
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
tTKSphereFromPoint1Display.SelectOrientationVectors = 'NodeType'
tTKSphereFromPoint1Display.ScaleFactor = 25.5996583253145
tTKSphereFromPoint1Display.SelectScaleArray = 'NodeType'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'NodeType'
tTKSphereFromPoint1Display.GaussianRadius = 12.7998291626573
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

# show data from diagonal
diagonalDisplay = Show(diagonal, renderView2)

# trace defaults for the display properties.
diagonalDisplay.Representation = 'Surface'
diagonalDisplay.ColorArrayName = [None, '']
diagonalDisplay.DiffuseColor = [0.250980392156863, 0.250980392156863, 0.250980392156863]
diagonalDisplay.Specular = 1.0
diagonalDisplay.OSPRayScaleArray = 'Coordinates'
diagonalDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
diagonalDisplay.SelectOrientationVectors = 'Coordinates'
diagonalDisplay.ScaleFactor = 25.8123103618622
diagonalDisplay.SelectScaleArray = 'Coordinates'
diagonalDisplay.GlyphType = 'Arrow'
diagonalDisplay.GlyphTableIndexArray = 'Coordinates'
diagonalDisplay.GaussianRadius = 12.9061551809311
diagonalDisplay.CustomShader = ''
diagonalDisplay.SetScaleArray = ['POINTS', 'NodeType']
diagonalDisplay.ScaleTransferFunction = 'PiecewiseFunction'
diagonalDisplay.OpacityArray = ['POINTS', 'NodeType']
diagonalDisplay.OpacityTransferFunction = 'PiecewiseFunction'
diagonalDisplay.DataAxesGrid = 'GridAxesRepresentation'
diagonalDisplay.SelectionCellLabelFontFile = ''
diagonalDisplay.SelectionPointLabelFontFile = ''
diagonalDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
diagonalDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
diagonalDisplay.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
diagonalDisplay.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
diagonalDisplay.DataAxesGrid.XTitleFontFile = ''
diagonalDisplay.DataAxesGrid.YTitleFontFile = ''
diagonalDisplay.DataAxesGrid.ZTitleFontFile = ''
diagonalDisplay.DataAxesGrid.XLabelFontFile = ''
diagonalDisplay.DataAxesGrid.YLabelFontFile = ''
diagonalDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
diagonalDisplay.PolarAxes.PolarAxisTitleFontFile = ''
diagonalDisplay.PolarAxes.PolarAxisLabelFontFile = ''
diagonalDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
diagonalDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube2
tube2Display = Show(tube2, renderView2)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'Coordinates'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Coordinates'
tube2Display.ScaleFactor = 25.5
tube2Display.SelectScaleArray = 'Coordinates'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'Coordinates'
tube2Display.GaussianRadius = 12.75
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
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from ctBonesvti
ctBonesvtiDisplay = Show(ctBonesvti, renderView3)

# trace defaults for the display properties.
ctBonesvtiDisplay.Representation = 'Outline'
ctBonesvtiDisplay.ColorArrayName = ['POINTS', '']
ctBonesvtiDisplay.OSPRayScaleArray = 'Scalars_'
ctBonesvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.SelectOrientationVectors = 'None'
ctBonesvtiDisplay.ScaleFactor = 25.5
ctBonesvtiDisplay.SelectScaleArray = 'Scalars_'
ctBonesvtiDisplay.GlyphType = 'Arrow'
ctBonesvtiDisplay.GlyphTableIndexArray = 'Scalars_'
ctBonesvtiDisplay.SetScaleArray = [None, '']
ctBonesvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.OpacityArray = [None, '']
ctBonesvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ctBonesvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
ctBonesvtiDisplay.SelectionCellLabelFontFile = ''
ctBonesvtiDisplay.SelectionPointLabelFontFile = ''
ctBonesvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
ctBonesvtiDisplay.ScalarOpacityUnitDistance = 1.73205080756888
ctBonesvtiDisplay.Slice = 127

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ctBonesvtiDisplay.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ctBonesvtiDisplay.DataAxesGrid.XTitleFontFile = ''
ctBonesvtiDisplay.DataAxesGrid.YTitleFontFile = ''
ctBonesvtiDisplay.DataAxesGrid.ZTitleFontFile = ''
ctBonesvtiDisplay.DataAxesGrid.XLabelFontFile = ''
ctBonesvtiDisplay.DataAxesGrid.YLabelFontFile = ''
ctBonesvtiDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ctBonesvtiDisplay.PolarAxes.PolarAxisTitleFontFile = ''
ctBonesvtiDisplay.PolarAxes.PolarAxisLabelFontFile = ''
ctBonesvtiDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
ctBonesvtiDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from clip1
clip1Display = Show(clip1, renderView3)

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')
scalars_LUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 54.5283012390137, 0.462745098039216, 0.541176470588235, 0.686274509803922, 64.1509399414062, 0.917647, 0.941176, 0.788235, 81.7924499511719, 0.415686274509804, 0.662745098039216, 0.356862745098039, 107.452827453613, 0.101960784313725, 0.486274509803922, 0.0862745098039216, 255.0, 0.0, 0.431373, 0.0]
scalars_LUT.ColorSpace = 'RGB'
scalars_LUT.AboveRangeColor = [1.0, 1.0, 1.0]
scalars_LUT.NanColor = [0.0, 0.0, 0.0]
scalars_LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')
scalars_PWF.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]
scalars_PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'Scalars_']
clip1Display.LookupTable = scalars_LUT
clip1Display.Specular = 1.0
clip1Display.OSPRayScaleArray = 'Scalars_'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 25.5
clip1Display.SelectScaleArray = 'Scalars_'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Scalars_'
clip1Display.GaussianRadius = 12.75
clip1Display.CustomShader = ''
clip1Display.SetScaleArray = ['POINTS', 'Scalars_']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Scalars_']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = scalars_PWF
clip1Display.ScalarOpacityUnitDistance = 1.88741758042521

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from generateSurfaceNormals1
generateSurfaceNormals1Display_1 = Show(generateSurfaceNormals1, renderView3)

# trace defaults for the display properties.
generateSurfaceNormals1Display_1.Representation = 'Surface'
generateSurfaceNormals1Display_1.ColorArrayName = ['POINTS', '']
generateSurfaceNormals1Display_1.Opacity = 0.2
generateSurfaceNormals1Display_1.Specular = 1.0
generateSurfaceNormals1Display_1.OSPRayScaleArray = 'Scalars_'
generateSurfaceNormals1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display_1.SelectOrientationVectors = 'None'
generateSurfaceNormals1Display_1.ScaleFactor = 23.662092590332
generateSurfaceNormals1Display_1.SelectScaleArray = 'Scalars_'
generateSurfaceNormals1Display_1.GlyphType = 'Arrow'
generateSurfaceNormals1Display_1.GlyphTableIndexArray = 'Scalars_'
generateSurfaceNormals1Display_1.GaussianRadius = 11.831046295166
generateSurfaceNormals1Display_1.CustomShader = ''
generateSurfaceNormals1Display_1.SetScaleArray = ['POINTS', 'Scalars_']
generateSurfaceNormals1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display_1.OpacityArray = ['POINTS', 'Scalars_']
generateSurfaceNormals1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display_1.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display_1.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display_1.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals1Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals1Display_1.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals1Display_1.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals1Display_1.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals1Display_1.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals1Display_1.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals1Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'NodeType'
nodeTypePWF = GetOpacityTransferFunction('NodeType')
nodeTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
nodeTypePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'SegmentationId'
segmentationIdPWF = GetOpacityTransferFunction('SegmentationId')
segmentationIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
segmentationIdPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------