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
renderView1.ViewSize = [678, 402]
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
renderView2.ViewSize = [677, 402]
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
layout1.SetSize(1356, 402)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

ttkIcosphere1 = TTKIcosphere(registrationName='TTKIcosphere1')
ttkIdentifiers1 = TTKIdentifiers(registrationName='TTKIdentifiers1', Input=ttkIcosphere1)
ttkWebSocketIO1 = TTKWebSocketIO(registrationName='TTKWebSocketIO1', Input=ttkIdentifiers1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from ttkIdentifiers1
ttkIdentifiers1Display = Show(ttkIdentifiers1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'ttkVertexScalarField'
ttkVertexScalarFieldLUT = GetColorTransferFunction('ttkVertexScalarField')
ttkVertexScalarFieldLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.5, 0.865003, 0.865003, 0.865003, 11.0, 0.705882, 0.0156863, 0.14902]
ttkVertexScalarFieldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
ttkIdentifiers1Display.Representation = 'Surface'
ttkIdentifiers1Display.ColorArrayName = ['POINTS', 'ttkVertexScalarField']
ttkIdentifiers1Display.LookupTable = ttkVertexScalarFieldLUT
ttkIdentifiers1Display.SelectTCoordArray = 'None'
ttkIdentifiers1Display.SelectNormalArray = 'None'
ttkIdentifiers1Display.SelectTangentArray = 'None'
ttkIdentifiers1Display.OSPRayScaleArray = 'ttkVertexScalarField'
ttkIdentifiers1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkIdentifiers1Display.SelectOrientationVectors = 'None'
ttkIdentifiers1Display.ScaleFactor = 0.17013015747070315
ttkIdentifiers1Display.SelectScaleArray = 'None'
ttkIdentifiers1Display.GlyphType = 'Arrow'
ttkIdentifiers1Display.GlyphTableIndexArray = 'None'
ttkIdentifiers1Display.GaussianRadius = 0.008506507873535156
ttkIdentifiers1Display.SetScaleArray = ['POINTS', 'ttkVertexScalarField']
ttkIdentifiers1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkIdentifiers1Display.OpacityArray = ['POINTS', 'ttkVertexScalarField']
ttkIdentifiers1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkIdentifiers1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkIdentifiers1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkIdentifiers1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 11.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkIdentifiers1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 11.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from ttkWebSocketIO1
ttkWebSocketIO1Display = Show(ttkWebSocketIO1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ExamplePointDataArray'
examplePointDataArrayLUT = GetColorTransferFunction('ExamplePointDataArray')
examplePointDataArrayLUT.RGBPoints = [-5.0, 0.231373, 0.298039, 0.752941, -3.0, 0.865003, 0.865003, 0.865003, -1.0, 0.705882, 0.0156863, 0.14902]
examplePointDataArrayLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ExamplePointDataArray'
examplePointDataArrayPWF = GetOpacityTransferFunction('ExamplePointDataArray')
examplePointDataArrayPWF.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]
examplePointDataArrayPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
ttkWebSocketIO1Display.Representation = 'Surface'
ttkWebSocketIO1Display.ColorArrayName = ['POINTS', 'ExamplePointDataArray']
ttkWebSocketIO1Display.LookupTable = examplePointDataArrayLUT
ttkWebSocketIO1Display.SelectTCoordArray = 'None'
ttkWebSocketIO1Display.SelectNormalArray = 'None'
ttkWebSocketIO1Display.SelectTangentArray = 'None'
ttkWebSocketIO1Display.OSPRayScaleArray = 'ExamplePointDataArray'
ttkWebSocketIO1Display.OSPRayScaleFunction = 'PiecewiseFunction'
ttkWebSocketIO1Display.SelectOrientationVectors = 'None'
ttkWebSocketIO1Display.ScaleFactor = 0.2
ttkWebSocketIO1Display.SelectScaleArray = 'ExamplePointDataArray'
ttkWebSocketIO1Display.GlyphType = 'Arrow'
ttkWebSocketIO1Display.GlyphTableIndexArray = 'ExamplePointDataArray'
ttkWebSocketIO1Display.GaussianRadius = 0.01
ttkWebSocketIO1Display.SetScaleArray = ['POINTS', 'ExamplePointDataArray']
ttkWebSocketIO1Display.ScaleTransferFunction = 'PiecewiseFunction'
ttkWebSocketIO1Display.OpacityArray = ['POINTS', 'ExamplePointDataArray']
ttkWebSocketIO1Display.OpacityTransferFunction = 'PiecewiseFunction'
ttkWebSocketIO1Display.DataAxesGrid = 'GridAxesRepresentation'
ttkWebSocketIO1Display.PolarAxes = 'PolarAxesRepresentation'
ttkWebSocketIO1Display.ScalarOpacityFunction = examplePointDataArrayPWF
ttkWebSocketIO1Display.ScalarOpacityUnitDistance = 1.774768329877785
ttkWebSocketIO1Display.OpacityArrayName = ['POINTS', 'ExamplePointDataArray']
ttkWebSocketIO1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ttkWebSocketIO1Display.ScaleTransferFunction.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ttkWebSocketIO1Display.OpacityTransferFunction.Points = [-5.0, 0.0, 0.5, 0.0, -1.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'ttkVertexScalarField'
ttkVertexScalarFieldPWF = GetOpacityTransferFunction('ttkVertexScalarField')
ttkVertexScalarFieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 11.0, 1.0, 0.5, 0.0]
ttkVertexScalarFieldPWF.ScalarRangeInitialized = 1
