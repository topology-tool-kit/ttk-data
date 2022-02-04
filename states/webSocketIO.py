# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [678, 506]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.055230719568613376, 0.9258039835776175, 5.617192129740201]
renderView1.CameraFocalPoint = [0.028925400103161122, -0.07452783924491535, 0.013167622178124871]
renderView1.CameraViewUp = [0.4851148099218602, 0.8604466851591295, -0.1558689295310115]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.473370383194758
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [677, 506]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-2.1956880750963, 1.1012529795769979, 2.8984371371228597]
renderView2.CameraFocalPoint = [-0.10797200872540381, 0.36903090897439744, -0.16194931005432628]
renderView2.CameraViewUp = [-0.0374390542532092, 0.9657889167252136, -0.25661271509292716]
renderView2.CameraFocalDisk = 1.0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)
layout1.SetSize(1356, 506)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------
tTKIcosphere1 = TTKIcosphere(registrationName='TTKIcosphere1')
generateIds1 = GenerateIds(registrationName='GenerateIds1', Input=tTKIcosphere1)
tTKWebSocketIO1 = TTKWebSocketIO(registrationName='TTKWebSocketIO1', Input=generateIds1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from generateIds1
generateIds1Display = Show(generateIds1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'PointIds'
pointIdsLUT = GetColorTransferFunction('PointIds')
pointIdsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.5, 0.865003, 0.865003, 0.865003, 11.0, 0.705882, 0.0156863, 0.14902]
pointIdsLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
generateIds1Display.Representation = 'Surface'
generateIds1Display.ColorArrayName = ['POINTS', 'PointIds']
generateIds1Display.LookupTable = pointIdsLUT
generateIds1Display.SelectTCoordArray = 'None'
generateIds1Display.SelectNormalArray = 'None'
generateIds1Display.SelectTangentArray = 'None'
generateIds1Display.OSPRayScaleArray = 'ttkVertexScalarField'
generateIds1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateIds1Display.SelectOrientationVectors = 'None'
generateIds1Display.ScaleFactor = 0.17013015747070315
generateIds1Display.SelectScaleArray = 'None'
generateIds1Display.GlyphType = 'Arrow'
generateIds1Display.GlyphTableIndexArray = 'None'
generateIds1Display.GaussianRadius = 0.008506507873535156
generateIds1Display.SetScaleArray = ['POINTS', 'ttkVertexScalarField']
generateIds1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateIds1Display.OpacityArray = ['POINTS', 'ttkVertexScalarField']
generateIds1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateIds1Display.DataAxesGrid = 'GridAxesRepresentation'
generateIds1Display.PolarAxes = 'PolarAxesRepresentation'
generateIds1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 11.0, 1.0, 0.5, 0.0]
generateIds1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 11.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKWebSocketIO1
tTKWebSocketIO1Display = Show(tTKWebSocketIO1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ExamplePointDataArray'
examplePointDataArrayLUT = GetColorTransferFunction('ExamplePointDataArray')
examplePointDataArrayLUT.RGBPoints = [-5.0, 0.231373, 0.298039, 0.752941, -3.0, 0.865003, 0.865003, 0.865003, -1.0, 0.705882, 0.0156863, 0.14902]
examplePointDataArrayLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ExamplePointDataArray'
examplePointDataArrayPWF = GetOpacityTransferFunction('ExamplePointDataArray')
examplePointDataArrayPWF.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]
examplePointDataArrayPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKWebSocketIO1Display.Representation = 'Surface'
tTKWebSocketIO1Display.ColorArrayName = ['POINTS', 'ExamplePointDataArray']
tTKWebSocketIO1Display.LookupTable = examplePointDataArrayLUT
tTKWebSocketIO1Display.SelectTCoordArray = 'None'
tTKWebSocketIO1Display.SelectNormalArray = 'None'
tTKWebSocketIO1Display.SelectTangentArray = 'None'
tTKWebSocketIO1Display.OSPRayScaleArray = 'ExamplePointDataArray'
tTKWebSocketIO1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKWebSocketIO1Display.SelectOrientationVectors = 'None'
tTKWebSocketIO1Display.ScaleFactor = 0.2
tTKWebSocketIO1Display.SelectScaleArray = 'ExamplePointDataArray'
tTKWebSocketIO1Display.GlyphType = 'Arrow'
tTKWebSocketIO1Display.GlyphTableIndexArray = 'ExamplePointDataArray'
tTKWebSocketIO1Display.GaussianRadius = 0.01
tTKWebSocketIO1Display.SetScaleArray = ['POINTS', 'ExamplePointDataArray']
tTKWebSocketIO1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKWebSocketIO1Display.OpacityArray = ['POINTS', 'ExamplePointDataArray']
tTKWebSocketIO1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKWebSocketIO1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKWebSocketIO1Display.PolarAxes = 'PolarAxesRepresentation'
tTKWebSocketIO1Display.ScalarOpacityFunction = examplePointDataArrayPWF
tTKWebSocketIO1Display.ScalarOpacityUnitDistance = 1.774768329877785
tTKWebSocketIO1Display.OpacityArrayName = ['POINTS', 'ExamplePointDataArray']
tTKWebSocketIO1Display.ScaleTransferFunction.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]
tTKWebSocketIO1Display.OpacityTransferFunction.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]
