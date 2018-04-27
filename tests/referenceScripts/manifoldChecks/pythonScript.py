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
renderView1.ViewSize = [551, 1216]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.00000000931323, 1.99999989010394, 0.999999975785613]
renderView1.StereoType = 0
renderView1.CameraPosition = [4.49727009919691, 5.47637821012475, -9.69323910624827]
renderView1.CameraFocalPoint = [0.33549440585366, 1.41216074546321, 2.86502302546885]
renderView1.CameraViewUp = [-0.0919495101932537, 0.955911268079959, 0.278888750459722]
renderView1.CameraParallelScale = 6.5346311061565
renderView1.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitle = 'Birth'
renderView1.AxesGrid.YTitle = 'Death'
renderView1.AxesGrid.ZTitle = ''
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView1.AxesGrid.ShowGrid = 1
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [490, 1216]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [1.5, 2.0, 0.5]
renderView2.StereoType = 0
renderView2.CameraPosition = [-8.43510936159553, 5.15807069018414, 6.32388166291517]
renderView2.CameraFocalPoint = [1.4236935510801, 1.909980768761, 0.465519924103853]
renderView2.CameraViewUp = [0.235984061143141, 0.962147563782142, -0.136321635826747]
renderView2.CameraParallelScale = 2.54950975679639
renderView2.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitle = 'Birth'
renderView2.AxesGrid.YTitle = 'Death'
renderView2.AxesGrid.ZTitle = ''
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView2.AxesGrid.ShowGrid = 1
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [557, 1216]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [1.0, 2.0, 1.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [-7.69196220596045, 6.03389995997384, -3.94849204507528]
renderView3.CameraFocalPoint = [1.98802874219597, 1.55098768196511, 1.74322672505945]
renderView3.CameraViewUp = [0.33041095233363, 0.928514125519846, 0.169381584855317]
renderView3.CameraParallelScale = 4.7073011681576
renderView3.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.XTitle = 'Birth'
renderView3.AxesGrid.YTitle = 'Death'
renderView3.AxesGrid.ZTitle = ''
renderView3.AxesGrid.XTitleFontFile = ''
renderView3.AxesGrid.YTitleFontFile = ''
renderView3.AxesGrid.ZTitleFontFile = ''
renderView3.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView3.AxesGrid.ShowGrid = 1
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

# create a new 'XML Unstructured Grid Reader'
manifoldCheck2vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck2.vtu'])

# create a new 'XML Unstructured Grid Reader'
manifoldCheck1vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck1.vtu'])

# create a new 'XML Unstructured Grid Reader'
manifoldCheck0vtu = XMLUnstructuredGridReader(FileName=['manifoldCheck0.vtu'])

# create a new 'Tetrahedralize'
tetrahedralize3 = Tetrahedralize(Input=manifoldCheck2vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck3 = TTKManifoldCheck(Input=tetrahedralize3)

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKManifoldCheck3)
threshold3.Scalars = ['CELLS', 'TriangleLinkComponentNumber']
threshold3.ThresholdRange = [3.0, 3.0]

# create a new 'TTK Identifiers'
tTKIdentifiers1 = TTKIdentifiers(Input=threshold3)

# create a new 'Threshold'
threshold4 = Threshold(Input=tTKIdentifiers1)
threshold4.Scalars = ['CELLS', 'CellIdentifiers']
threshold4.ThresholdRange = [0.0, 1.0]

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=threshold4)

# create a new 'Threshold'
threshold5 = Threshold(Input=extractSurface2)
threshold5.Scalars = ['POINTS', 'TriangleLinkComponentNumber']
threshold5.ThresholdRange = [3.0, 3.0]

# create a new 'Extract Edges'
extractEdges3 = ExtractEdges(Input=threshold5)

# create a new 'Tube'
tube4 = Tube(Input=extractEdges3)
tube4.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube4.Vectors = [None, '']
tube4.Radius = 0.05

# create a new 'Extract Edges'
extractEdges4 = ExtractEdges(Input=tTKManifoldCheck3)

# create a new 'Tube'
tube5 = Tube(Input=extractEdges4)
tube5.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube5.Vectors = [None, '']
tube5.Radius = 0.0075

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(Input=manifoldCheck1vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck2 = TTKManifoldCheck(Input=tetrahedralize2)

# create a new 'Extract Edges'
extractEdges2 = ExtractEdges(Input=tTKManifoldCheck2)

# create a new 'Threshold'
threshold2 = Threshold(Input=extractEdges2)
threshold2.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
threshold2.ThresholdRange = [2.0, 2.0]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=threshold2)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface1)
tube3.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube3.Vectors = [None, '']
tube3.Radius = 0.05

# create a new 'Tube'
tube2 = Tube(Input=extractEdges2)
tube2.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube2.Vectors = [None, '']
tube2.Radius = 0.0075

# create a new 'Tetrahedralize'
tetrahedralize1 = Tetrahedralize(Input=manifoldCheck0vtu)

# create a new 'TTK ManifoldCheck'
tTKManifoldCheck1 = TTKManifoldCheck(Input=tetrahedralize1)

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=tTKManifoldCheck1)

# create a new 'Tube'
tube1 = Tube(Input=extractEdges1)
tube1.Scalars = ['POINTS', 'EdgeLinkComponentNumber']
tube1.Vectors = [None, '']
tube1.Radius = 0.0075

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKManifoldCheck1)
tTKSphereFromPoint1.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKManifoldCheck3)
tTKSphereFromPoint4.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tTKManifoldCheck2)
tTKSphereFromPoint3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tTKManifoldCheck1)
tTKSphereFromPoint2.Radius = 0.1

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKSphereFromPoint2)
threshold1.Scalars = ['POINTS', 'VertexLinkComponentNumber']
threshold1.ThresholdRange = [2.0, 2.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tTKManifoldCheck1
tTKManifoldCheck1Display = Show(tTKManifoldCheck1, renderView1)

# trace defaults for the display properties.
tTKManifoldCheck1Display.Representation = 'Surface'
tTKManifoldCheck1Display.ColorArrayName = ['POINTS', '']
tTKManifoldCheck1Display.Opacity = 0.1
tTKManifoldCheck1Display.Specular = 1.0
tTKManifoldCheck1Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKManifoldCheck1Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKManifoldCheck1Display.ScaleFactor = 0.4
tTKManifoldCheck1Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck1Display.GlyphType = 'Arrow'
tTKManifoldCheck1Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck1Display.GaussianRadius = 0.2
tTKManifoldCheck1Display.CustomShader = ''
tTKManifoldCheck1Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck1Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKManifoldCheck1Display.SelectionCellLabelFontFile = ''
tTKManifoldCheck1Display.SelectionPointLabelFontFile = ''
tTKManifoldCheck1Display.PolarAxes = 'PolarAxesRepresentation'
tTKManifoldCheck1Display.ScalarOpacityUnitDistance = 1.69838132956495

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKManifoldCheck1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKManifoldCheck1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKManifoldCheck1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKManifoldCheck1Display.DataAxesGrid.XTitleFontFile = ''
tTKManifoldCheck1Display.DataAxesGrid.YTitleFontFile = ''
tTKManifoldCheck1Display.DataAxesGrid.ZTitleFontFile = ''
tTKManifoldCheck1Display.DataAxesGrid.XLabelFontFile = ''
tTKManifoldCheck1Display.DataAxesGrid.YLabelFontFile = ''
tTKManifoldCheck1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKManifoldCheck1Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKManifoldCheck1Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKManifoldCheck1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKManifoldCheck1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint1
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView1)

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', '']
tTKSphereFromPoint1Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKSphereFromPoint1Display.ScaleFactor = 0.499658468365669
tTKSphereFromPoint1Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint1Display.GaussianRadius = 0.249829234182835
tTKSphereFromPoint1Display.CustomShader = ''
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tube1Display.ScaleFactor = 0.407999996095896
tube1Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tube1Display.GaussianRadius = 0.203999998047948
tube1Display.CustomShader = ''
tube1Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.DiffuseColor = [0.0, 0.333333333333333, 0.0]
threshold1Display.Specular = 1.0
threshold1Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
threshold1Display.ScaleFactor = 0.299658447504044
threshold1Display.SelectScaleArray = 'EdgeLinkComponentNumber'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
threshold1Display.GaussianRadius = 0.149829223752022
threshold1Display.CustomShader = ''
threshold1Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityUnitDistance = 0.256254884252341

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold1Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold1Display.DataAxesGrid.XTitleFontFile = ''
threshold1Display.DataAxesGrid.YTitleFontFile = ''
threshold1Display.DataAxesGrid.ZTitleFontFile = ''
threshold1Display.DataAxesGrid.XLabelFontFile = ''
threshold1Display.DataAxesGrid.YLabelFontFile = ''
threshold1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold1Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold1Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold1Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKManifoldCheck2
tTKManifoldCheck2Display = Show(tTKManifoldCheck2, renderView2)

# trace defaults for the display properties.
tTKManifoldCheck2Display.Representation = 'Surface'
tTKManifoldCheck2Display.ColorArrayName = ['POINTS', '']
tTKManifoldCheck2Display.Opacity = 0.1
tTKManifoldCheck2Display.Specular = 1.0
tTKManifoldCheck2Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKManifoldCheck2Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKManifoldCheck2Display.ScaleFactor = 0.4
tTKManifoldCheck2Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck2Display.GlyphType = 'Arrow'
tTKManifoldCheck2Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck2Display.GaussianRadius = 0.2
tTKManifoldCheck2Display.CustomShader = ''
tTKManifoldCheck2Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck2Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKManifoldCheck2Display.SelectionCellLabelFontFile = ''
tTKManifoldCheck2Display.SelectionPointLabelFontFile = ''
tTKManifoldCheck2Display.PolarAxes = 'PolarAxesRepresentation'
tTKManifoldCheck2Display.ScalarOpacityUnitDistance = 1.76773133394172

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKManifoldCheck2Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKManifoldCheck2Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKManifoldCheck2Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKManifoldCheck2Display.DataAxesGrid.XTitleFontFile = ''
tTKManifoldCheck2Display.DataAxesGrid.YTitleFontFile = ''
tTKManifoldCheck2Display.DataAxesGrid.ZTitleFontFile = ''
tTKManifoldCheck2Display.DataAxesGrid.XLabelFontFile = ''
tTKManifoldCheck2Display.DataAxesGrid.YLabelFontFile = ''
tTKManifoldCheck2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKManifoldCheck2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKManifoldCheck2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKManifoldCheck2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKManifoldCheck2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView2)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = [None, '']
tTKSphereFromPoint3Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKSphereFromPoint3Display.ScaleFactor = 0.499658468365669
tTKSphereFromPoint3Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint3Display.GaussianRadius = 0.249829234182835
tTKSphereFromPoint3Display.CustomShader = ''
tTKSphereFromPoint3Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from tube2
tube2Display = Show(tube2, renderView2)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tube2Display.ScaleFactor = 0.402000022865832
tube2Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tube2Display.GaussianRadius = 0.201000011432916
tube2Display.CustomShader = ''
tube2Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from tube3
tube3Display = Show(tube3, renderView2)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.DiffuseColor = [1.0, 0.952941176470588, 0.831372549019608]
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tube3Display.ScaleFactor = 0.203999996185303
tube3Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tube3Display.GaussianRadius = 0.101999998092651
tube3Display.CustomShader = ''
tube3Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tTKManifoldCheck3
tTKManifoldCheck3Display = Show(tTKManifoldCheck3, renderView3)

# trace defaults for the display properties.
tTKManifoldCheck3Display.Representation = 'Surface'
tTKManifoldCheck3Display.ColorArrayName = [None, '']
tTKManifoldCheck3Display.Opacity = 0.1
tTKManifoldCheck3Display.Specular = 1.0
tTKManifoldCheck3Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKManifoldCheck3Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKManifoldCheck3Display.ScaleFactor = 0.3
tTKManifoldCheck3Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck3Display.GlyphType = 'Arrow'
tTKManifoldCheck3Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKManifoldCheck3Display.GaussianRadius = 0.15
tTKManifoldCheck3Display.CustomShader = ''
tTKManifoldCheck3Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck3Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKManifoldCheck3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKManifoldCheck3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKManifoldCheck3Display.SelectionCellLabelFontFile = ''
tTKManifoldCheck3Display.SelectionPointLabelFontFile = ''
tTKManifoldCheck3Display.PolarAxes = 'PolarAxesRepresentation'
tTKManifoldCheck3Display.ScalarOpacityUnitDistance = 1.5111458631295

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKManifoldCheck3Display.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKManifoldCheck3Display.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKManifoldCheck3Display.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKManifoldCheck3Display.DataAxesGrid.XTitleFontFile = ''
tTKManifoldCheck3Display.DataAxesGrid.YTitleFontFile = ''
tTKManifoldCheck3Display.DataAxesGrid.ZTitleFontFile = ''
tTKManifoldCheck3Display.DataAxesGrid.XLabelFontFile = ''
tTKManifoldCheck3Display.DataAxesGrid.YLabelFontFile = ''
tTKManifoldCheck3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKManifoldCheck3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKManifoldCheck3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKManifoldCheck3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKManifoldCheck3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from threshold5
threshold5Display = Show(threshold5, renderView3)

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = [None, '']
threshold5Display.DiffuseColor = [0.0, 0.0, 0.498039215686275]
threshold5Display.Opacity = 0.5
threshold5Display.Specular = 1.0
threshold5Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
threshold5Display.ScaleFactor = 0.1
threshold5Display.SelectScaleArray = 'EdgeLinkComponentNumber'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
threshold5Display.GaussianRadius = 0.05
threshold5Display.CustomShader = ''
threshold5Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.SelectionCellLabelFontFile = ''
threshold5Display.SelectionPointLabelFontFile = ''
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityUnitDistance = 0.866025403784439

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

# show data from tube4
tube4Display = Show(tube4, renderView3)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = [None, '']
tube4Display.DiffuseColor = [0.0, 0.0, 0.498039215686275]
tube4Display.Specular = 1.0
tube4Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tube4Display.ScaleFactor = 0.101999998092651
tube4Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tube4Display.GlyphType = 'Arrow'
tube4Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tube4Display.GaussianRadius = 0.0509999990463257
tube4Display.CustomShader = ''
tube4Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from tTKSphereFromPoint4
tTKSphereFromPoint4Display = Show(tTKSphereFromPoint4, renderView3)

# trace defaults for the display properties.
tTKSphereFromPoint4Display.Representation = 'Surface'
tTKSphereFromPoint4Display.ColorArrayName = [None, '']
tTKSphereFromPoint4Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tTKSphereFromPoint4Display.Specular = 1.0
tTKSphereFromPoint4Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tTKSphereFromPoint4Display.ScaleFactor = 0.309965848922729
tTKSphereFromPoint4Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint4Display.GlyphType = 'Arrow'
tTKSphereFromPoint4Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tTKSphereFromPoint4Display.GaussianRadius = 0.154982924461365
tTKSphereFromPoint4Display.CustomShader = ''
tTKSphereFromPoint4Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tTKSphereFromPoint4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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

# show data from tube5
tube5Display = Show(tube5, renderView3)

# trace defaults for the display properties.
tube5Display.Representation = 'Surface'
tube5Display.ColorArrayName = [None, '']
tube5Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube5Display.Specular = 1.0
tube5Display.OSPRayScaleArray = 'EdgeLinkComponentNumber'
tube5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube5Display.SelectOrientationVectors = 'EdgeLinkComponentNumber'
tube5Display.ScaleFactor = 0.301499992609024
tube5Display.SelectScaleArray = 'EdgeLinkComponentNumber'
tube5Display.GlyphType = 'Arrow'
tube5Display.GlyphTableIndexArray = 'EdgeLinkComponentNumber'
tube5Display.GaussianRadius = 0.150749996304512
tube5Display.CustomShader = ''
tube5Display.SetScaleArray = ['POINTS', 'EdgeLinkComponentNumber']
tube5Display.ScaleTransferFunction = 'PiecewiseFunction'
tube5Display.OpacityArray = ['POINTS', 'EdgeLinkComponentNumber']
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
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------