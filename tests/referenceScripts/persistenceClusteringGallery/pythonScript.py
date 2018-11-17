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
renderView1.ViewSize = [452, 589]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView1.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView1.CameraParallelScale = 2.74838600391004
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
renderView11 = CreateView('RenderView')
renderView11.ViewSize = [398, 589]
renderView11.InteractionMode = '2D'
renderView11.AxesGrid = 'GridAxes3DActor'
renderView11.OrientationAxesVisibility = 0
renderView11.CenterOfRotation = [-0.309726297855377, -0.0956822037696838, 0.0]
renderView11.StereoType = 0
renderView11.CameraPosition = [-0.26994147564784, -0.138501133808051, 8.86935894145291]
renderView11.CameraFocalPoint = [-0.26994147564784, -0.138501133808051, 0.0]
renderView11.CameraParallelScale = 2.41325202587316
renderView11.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView11.AxesGrid.Visibility = 1
renderView11.AxesGrid.XTitle = 'Birth'
renderView11.AxesGrid.YTitle = 'Death'
renderView11.AxesGrid.ZTitle = ''
renderView11.AxesGrid.XTitleFontFile = ''
renderView11.AxesGrid.YTitleFontFile = ''
renderView11.AxesGrid.ZTitleFontFile = ''
renderView11.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView11.AxesGrid.ShowEdges = 0
renderView11.AxesGrid.ShowTicks = 0
renderView11.AxesGrid.AxesToLabel = 0
renderView11.AxesGrid.XLabelFontFile = ''
renderView11.AxesGrid.YLabelFontFile = ''
renderView11.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [432, 589]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView2.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView2.CameraParallelScale = 2.74838600391004
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
renderView3.ViewSize = [451, 589]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView3.StereoType = 0
renderView3.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView3.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView3.CameraParallelScale = 2.74838600391004
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
renderView4.ViewSize = [462, 589]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView4.StereoType = 0
renderView4.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView4.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView4.CameraParallelScale = 2.74838600391004
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

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [398, 589]
renderView5.InteractionMode = '2D'
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [-0.309726297855377, -0.0956822037696838, 0.0]
renderView5.StereoType = 0
renderView5.CameraPosition = [-0.26994147564784, -0.138501133808051, 8.86935894145291]
renderView5.CameraFocalPoint = [-0.26994147564784, -0.138501133808051, 0.0]
renderView5.CameraParallelScale = 2.41325202587316
renderView5.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView5.AxesGrid.Visibility = 1
renderView5.AxesGrid.XTitle = 'Birth'
renderView5.AxesGrid.YTitle = 'Death'
renderView5.AxesGrid.ZTitle = ''
renderView5.AxesGrid.XTitleFontFile = ''
renderView5.AxesGrid.YTitleFontFile = ''
renderView5.AxesGrid.ZTitleFontFile = ''
renderView5.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView5.AxesGrid.ShowEdges = 0
renderView5.AxesGrid.ShowTicks = 0
renderView5.AxesGrid.AxesToLabel = 0
renderView5.AxesGrid.XLabelFontFile = ''
renderView5.AxesGrid.YLabelFontFile = ''
renderView5.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.ViewSize = [452, 589]
renderView6.InteractionMode = '2D'
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.OrientationAxesVisibility = 0
renderView6.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView6.StereoType = 0
renderView6.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView6.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView6.CameraParallelScale = 2.74838600391004
renderView6.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView6.AxesGrid.Visibility = 1
renderView6.AxesGrid.XTitleFontFile = ''
renderView6.AxesGrid.YTitleFontFile = ''
renderView6.AxesGrid.ZTitleFontFile = ''
renderView6.AxesGrid.FacesToRender = 0
renderView6.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView6.AxesGrid.ShowEdges = 0
renderView6.AxesGrid.ShowTicks = 0
renderView6.AxesGrid.XLabelFontFile = ''
renderView6.AxesGrid.YLabelFontFile = ''
renderView6.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView7 = CreateView('RenderView')
renderView7.ViewSize = [432, 589]
renderView7.InteractionMode = '2D'
renderView7.AxesGrid = 'GridAxes3DActor'
renderView7.OrientationAxesVisibility = 0
renderView7.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView7.StereoType = 0
renderView7.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView7.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView7.CameraParallelScale = 2.74838600391004
renderView7.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView7.AxesGrid.Visibility = 1
renderView7.AxesGrid.XTitleFontFile = ''
renderView7.AxesGrid.YTitleFontFile = ''
renderView7.AxesGrid.ZTitleFontFile = ''
renderView7.AxesGrid.FacesToRender = 0
renderView7.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView7.AxesGrid.ShowEdges = 0
renderView7.AxesGrid.ShowTicks = 0
renderView7.AxesGrid.XLabelFontFile = ''
renderView7.AxesGrid.YLabelFontFile = ''
renderView7.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView8 = CreateView('RenderView')
renderView8.ViewSize = [462, 589]
renderView8.InteractionMode = '2D'
renderView8.AxesGrid = 'GridAxes3DActor'
renderView8.OrientationAxesVisibility = 0
renderView8.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView8.StereoType = 0
renderView8.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView8.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView8.CameraParallelScale = 2.74838600391004
renderView8.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView8.AxesGrid.Visibility = 1
renderView8.AxesGrid.XTitleFontFile = ''
renderView8.AxesGrid.YTitleFontFile = ''
renderView8.AxesGrid.ZTitleFontFile = ''
renderView8.AxesGrid.FacesToRender = 0
renderView8.AxesGrid.GridColor = [0.392156862745098, 0.384313725490196, 0.384313725490196]
renderView8.AxesGrid.ShowEdges = 0
renderView8.AxesGrid.ShowTicks = 0
renderView8.AxesGrid.XLabelFontFile = ''
renderView8.AxesGrid.YLabelFontFile = ''
renderView8.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView9 = CreateView('RenderView')
renderView9.ViewSize = [451, 589]
renderView9.InteractionMode = '2D'
renderView9.AxesGrid = 'GridAxes3DActor'
renderView9.OrientationAxesVisibility = 0
renderView9.CenterOfRotation = [-0.0187499523162842, 0.0313221216201782, 0.0]
renderView9.StereoType = 0
renderView9.CameraPosition = [-0.0529632015041998, 0.0342357651659142, 12.8026525377278]
renderView9.CameraFocalPoint = [-0.0529632015041998, 0.0342357651659142, 0.0]
renderView9.CameraParallelScale = 2.74838600391004
renderView9.Background = [0.32, 0.34, 0.43]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView9.AxesGrid.Visibility = 1
renderView9.AxesGrid.XTitle = 'Birth'
renderView9.AxesGrid.YTitle = 'Death'
renderView9.AxesGrid.ZTitle = ''
renderView9.AxesGrid.XTitleFontFile = ''
renderView9.AxesGrid.YTitleFontFile = ''
renderView9.AxesGrid.ZTitleFontFile = ''
renderView9.AxesGrid.GridColor = [0.282352941176471, 0.27843137254902, 0.27843137254902]
renderView9.AxesGrid.ShowEdges = 0
renderView9.AxesGrid.ShowTicks = 0
renderView9.AxesGrid.AxesToLabel = 0
renderView9.AxesGrid.XLabelFontFile = ''
renderView9.AxesGrid.YLabelFontFile = ''
renderView9.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
clustering3csv = CSVReader(FileName=['clustering3.csv'])

# create a new 'CSV Reader'
clustering2csv = CSVReader(FileName=['clustering2.csv'])

# create a new 'CSV Reader'
clustering0csv = CSVReader(FileName=['clustering0.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=clustering0csv)
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.ZColumn = 'X'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'CSV Reader'
clustering1csv = CSVReader(FileName=['clustering1.csv'])

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(Input=clustering1csv)
tableToPoints2.XColumn = 'X'
tableToPoints2.YColumn = 'Y'
tableToPoints2.ZColumn = 'X'
tableToPoints2.a2DPoints = 1
tableToPoints2.KeepAllDataArrays = 1

# create a new 'Table To Points'
tableToPoints3 = TableToPoints(Input=clustering2csv)
tableToPoints3.XColumn = 'X'
tableToPoints3.YColumn = 'Y'
tableToPoints3.ZColumn = 'X'
tableToPoints3.a2DPoints = 1
tableToPoints3.KeepAllDataArrays = 1

# create a new 'CSV Reader'
clustering4csv = CSVReader(FileName=['clustering4.csv'])

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint5 = TTKSphereFromPoint(Input=tableToPoints3)
tTKSphereFromPoint5.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint3 = TTKSphereFromPoint(Input=tableToPoints2)
tTKSphereFromPoint3.Radius = 0.05

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint2 = TTKSphereFromPoint(Input=tableToPoints1)
tTKSphereFromPoint2.Radius = 0.05

# create a new 'Table To Points'
tableToPoints5 = TableToPoints(Input=clustering4csv)
tableToPoints5.XColumn = 'X'
tableToPoints5.YColumn = 'Y'
tableToPoints5.ZColumn = 'X'
tableToPoints5.a2DPoints = 1
tableToPoints5.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint8 = TTKSphereFromPoint(Input=tableToPoints5)
tTKSphereFromPoint8.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling5 = GaussianResampling(Input=tableToPoints5)
gaussianResampling5.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling5.ResamplingGrid = [256, 256, 3]
gaussianResampling5.SplatAccumulationMode = 'Sum'

# create a new 'Table To Points'
tableToPoints4 = TableToPoints(Input=clustering3csv)
tableToPoints4.XColumn = 'X'
tableToPoints4.YColumn = 'Y'
tableToPoints4.ZColumn = 'X'
tableToPoints4.a2DPoints = 1
tableToPoints4.KeepAllDataArrays = 1

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint7 = TTKSphereFromPoint(Input=tableToPoints4)
tTKSphereFromPoint7.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling4 = GaussianResampling(Input=tableToPoints4)
gaussianResampling4.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling4.ResamplingGrid = [256, 256, 3]
gaussianResampling4.GaussianSplatRadius = 0.025
gaussianResampling4.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice4 = Slice(Input=gaussianResampling4)
slice4.SliceType = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [0.432938475, -0.313307725, 0.0]
slice4.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(Input=slice4)
tTKPersistenceDiagram4.ScalarField = 'SplatterValues'
tTKPersistenceDiagram4.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold7 = Threshold(Input=tTKPersistenceDiagram4)
threshold7.Scalars = ['CELLS', 'PairIdentifier']
threshold7.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold3 = Threshold(Input=threshold7)
persistenceThreshold3.Scalars = ['CELLS', 'Persistence']
persistenceThreshold3.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification4 = TTKTopologicalSimplification(Domain=slice4,
    Constraints=persistenceThreshold3)
tTKTopologicalSimplification4.ScalarField = 'SplatterValues'
tTKTopologicalSimplification4.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification4.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification4.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex4 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification4)
tTKMorseSmaleComplex4.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex4.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold8 = Threshold(Input=OutputPort(tTKMorseSmaleComplex4,1))
threshold8.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother4 = TTKGeometrySmoother(Input=threshold8)
tTKGeometrySmoother4.IterationNumber = 10
tTKGeometrySmoother4.InputMaskField = 'CellDimension'

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator4 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex4,3),
    Target=tableToPoints4)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint9 = TTKSphereFromPoint(Input=tTKDataSetInterpolator4)
tTKSphereFromPoint9.Radius = 0.05

# create a new 'Gaussian Resampling'
gaussianResampling3 = GaussianResampling(Input=tableToPoints3)
gaussianResampling3.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling3.ResamplingGrid = [256, 256, 3]
gaussianResampling3.GaussianSplatRadius = 0.05
gaussianResampling3.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice3 = Slice(Input=gaussianResampling3)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [-0.189980645, 0.28712807, 0.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(Input=slice3)
tTKPersistenceDiagram3.ScalarField = 'SplatterValues'
tTKPersistenceDiagram3.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold5 = Threshold(Input=tTKPersistenceDiagram3)
threshold5.Scalars = ['CELLS', 'PairIdentifier']
threshold5.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold2 = Threshold(Input=threshold5)
persistenceThreshold2.Scalars = ['CELLS', 'Persistence']
persistenceThreshold2.ThresholdRange = [5.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification3 = TTKTopologicalSimplification(Domain=slice3,
    Constraints=persistenceThreshold2)
tTKTopologicalSimplification3.ScalarField = 'SplatterValues'
tTKTopologicalSimplification3.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification3.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification3.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex3 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification3)
tTKMorseSmaleComplex3.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex3.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex3_1 = FindSource('TTKMorseSmaleComplex3')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator3 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex3,3),
    Target=tableToPoints3)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint6 = TTKSphereFromPoint(Input=tTKDataSetInterpolator3)
tTKSphereFromPoint6.Radius = 0.05

# find source
tTKMorseSmaleComplex3_2 = FindSource('TTKMorseSmaleComplex3')

# create a new 'Threshold'
threshold6 = Threshold(Input=OutputPort(tTKMorseSmaleComplex3,1))
threshold6.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother3 = TTKGeometrySmoother(Input=threshold6)
tTKGeometrySmoother3.IterationNumber = 10
tTKGeometrySmoother3.InputMaskField = 'CellDimension'

# create a new 'Gaussian Resampling'
gaussianResampling2 = GaussianResampling(Input=tableToPoints2)
gaussianResampling2.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling2.ResamplingGrid = [256, 256, 3]
gaussianResampling2.SplatAccumulationMode = 'Sum'

# create a new 'Slice'
slice2 = Slice(Input=gaussianResampling2)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.0283216049999999, -0.0118457750000003, 0.0]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(Input=slice2)
tTKPersistenceDiagram2.ScalarField = 'SplatterValues'
tTKPersistenceDiagram2.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold3 = Threshold(Input=tTKPersistenceDiagram2)
threshold3.Scalars = ['CELLS', 'PairIdentifier']
threshold3.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold1 = Threshold(Input=threshold3)
persistenceThreshold1.Scalars = ['CELLS', 'Persistence']
persistenceThreshold1.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification2 = TTKTopologicalSimplification(Domain=slice2,
    Constraints=persistenceThreshold1)
tTKTopologicalSimplification2.ScalarField = 'SplatterValues'
tTKTopologicalSimplification2.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification2.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification2.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex2 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification2)
tTKMorseSmaleComplex2.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex2.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex2_1 = FindSource('TTKMorseSmaleComplex2')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator2 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex2_1,3),
    Target=tableToPoints2)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint4 = TTKSphereFromPoint(Input=tTKDataSetInterpolator2)
tTKSphereFromPoint4.Radius = 0.05

# find source
tTKMorseSmaleComplex2_2 = FindSource('TTKMorseSmaleComplex2')

# create a new 'Threshold'
threshold4 = Threshold(Input=OutputPort(tTKMorseSmaleComplex2_2,1))
threshold4.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(Input=threshold4)
tTKGeometrySmoother2.IterationNumber = 10
tTKGeometrySmoother2.InputMaskField = 'CellDimension'

# create a new 'Gaussian Resampling'
gaussianResampling1 = GaussianResampling(Input=tableToPoints1)
gaussianResampling1.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling1.ResamplingGrid = [256, 256, 3]
gaussianResampling1.SplatAccumulationMode = 'Sum'

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(Input=tTKGeometrySmoother4)

# create a new 'Tube'
tube4 = Tube(Input=extractSurface4)
tube4.Scalars = ['POINTS', 'CellDimension']
tube4.Vectors = [None, '']
tube4.Radius = 0.04

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(Input=tTKGeometrySmoother3)

# create a new 'Tube'
tube3 = Tube(Input=extractSurface3)
tube3.Scalars = ['POINTS', 'CellDimension']
tube3.Vectors = [None, '']
tube3.Radius = 0.04

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=tTKGeometrySmoother2)

# create a new 'Tube'
tube2 = Tube(Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CellDimension']
tube2.Vectors = [None, '']
tube2.Radius = 0.04

# create a new 'Slice'
slice1 = Slice(Input=gaussianResampling1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.0187499550000001, 0.0313220950000002, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(Input=slice1)
tTKPersistenceDiagram1.ScalarField = 'SplatterValues'
tTKPersistenceDiagram1.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold1 = Threshold(Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [-0.1, 999.0]

# create a new 'Threshold'
persistenceThreshold0 = Threshold(Input=threshold1)
persistenceThreshold0.Scalars = ['CELLS', 'Persistence']
persistenceThreshold0.ThresholdRange = [10.0, 9999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(Domain=slice1,
    Constraints=persistenceThreshold0)
tTKTopologicalSimplification1.ScalarField = 'SplatterValues'
tTKTopologicalSimplification1.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification1.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification1.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex1.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold2 = Threshold(Input=OutputPort(tTKMorseSmaleComplex1_1,1))
threshold2.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(Input=threshold2)
tTKGeometrySmoother1.IterationNumber = 10
tTKGeometrySmoother1.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = [None, '']
tube1.Radius = 0.04

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator1 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex1_2,3),
    Target=tableToPoints1)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint1 = TTKSphereFromPoint(Input=tTKDataSetInterpolator1)
tTKSphereFromPoint1.Radius = 0.05

# create a new 'Slice'
slice5 = Slice(Input=gaussianResampling5)
slice5.SliceType = 'Plane'
slice5.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice5.SliceType.Origin = [-0.309726305, -0.0956821999999999, 0.0]
slice5.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(Input=slice5)
tTKPersistenceDiagram5.ScalarField = 'SplatterValues'
tTKPersistenceDiagram5.InputOffsetField = 'SplatterValues'

# create a new 'Threshold'
threshold9 = Threshold(Input=tTKPersistenceDiagram5)
threshold9.Scalars = ['CELLS', 'PairIdentifier']
threshold9.ThresholdRange = [-0.1, 9999.0]

# create a new 'Threshold'
threshold10 = Threshold(Input=threshold9)
threshold10.Scalars = ['CELLS', 'Persistence']
threshold10.ThresholdRange = [10.0, 999.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification5 = TTKTopologicalSimplification(Domain=slice5,
    Constraints=threshold10)
tTKTopologicalSimplification5.ScalarField = 'SplatterValues'
tTKTopologicalSimplification5.InputOffsetField = 'SplatterValues'
tTKTopologicalSimplification5.Vertexidentifierfield = 'CriticalType'
tTKTopologicalSimplification5.OutputOffsetScalarField = ''

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex5 = TTKMorseSmaleComplex(Input=tTKTopologicalSimplification5)
tTKMorseSmaleComplex5.ScalarField = 'SplatterValues'
tTKMorseSmaleComplex5.InputOffsetField = 'SplatterValues'

# find source
tTKMorseSmaleComplex5_1 = FindSource('TTKMorseSmaleComplex5')

# create a new 'Threshold'
threshold11 = Threshold(Input=OutputPort(tTKMorseSmaleComplex5_1,1))
threshold11.Scalars = ['CELLS', 'SeparatrixType']

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother5 = TTKGeometrySmoother(Input=threshold11)
tTKGeometrySmoother5.IterationNumber = 10
tTKGeometrySmoother5.InputMaskField = 'CellDimension'

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(Input=tTKGeometrySmoother5)

# create a new 'Tube'
tube5 = Tube(Input=extractSurface5)
tube5.Scalars = ['POINTS', 'CellDimension']
tube5.Vectors = [None, '']
tube5.Radius = 0.04

# find source
tTKMorseSmaleComplex5_2 = FindSource('TTKMorseSmaleComplex5')

# create a new 'TTK DataSetInterpolator'
tTKDataSetInterpolator5 = TTKDataSetInterpolator(Source=OutputPort(tTKMorseSmaleComplex5_2,3),
    Target=tableToPoints5)

# create a new 'TTK SphereFromPoint'
tTKSphereFromPoint10 = TTKSphereFromPoint(Input=tTKDataSetInterpolator5)
tTKSphereFromPoint10.Radius = 0.05

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1)

# get color transfer function/color map for 'SplatterValues'
splatterValuesLUT = GetColorTransferFunction('SplatterValues')
splatterValuesLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 9.85870357834292, 0.917647, 0.941176, 0.788235, 19.717407156686, 0.0, 0.431373, 0.0]
splatterValuesLUT.ColorSpace = 'RGB'
splatterValuesLUT.NanColor = [0.0, 0.0, 0.0]
splatterValuesLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice1Display.LookupTable = splatterValuesLUT
slice1Display.Opacity = 0.5
slice1Display.Specular = 1.0
slice1Display.OSPRayScaleArray = 'SplatterValues'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.47112181186676
slice1Display.SelectScaleArray = 'SplatterValues'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'SplatterValues'
slice1Display.GaussianRadius = 0.023556090593338
slice1Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'SplatterValues']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 38.8330942882042, 1.0, 0.5, 0.0]

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
tTKSphereFromPoint2Display = Show(tTKSphereFromPoint2, renderView1)

# trace defaults for the display properties.
tTKSphereFromPoint2Display.Representation = 'Surface'
tTKSphereFromPoint2Display.ColorArrayName = [None, '']
tTKSphereFromPoint2Display.Opacity = 0.75
tTKSphereFromPoint2Display.Specular = 1.0
tTKSphereFromPoint2Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint2Display.ScaleFactor = 0.407550263404846
tTKSphereFromPoint2Display.SelectScaleArray = 'None'
tTKSphereFromPoint2Display.GlyphType = 'Arrow'
tTKSphereFromPoint2Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint2Display.GaussianRadius = 0.0203775131702423
tTKSphereFromPoint2Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint2Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint2Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint2Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint2Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

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
# setup the visualization in view 'renderView11'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint8
tTKSphereFromPoint8Display = Show(tTKSphereFromPoint8, renderView11)

# trace defaults for the display properties.
tTKSphereFromPoint8Display.Representation = 'Surface'
tTKSphereFromPoint8Display.ColorArrayName = [None, '']
tTKSphereFromPoint8Display.Opacity = 0.75
tTKSphereFromPoint8Display.Specular = 1.0
tTKSphereFromPoint8Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint8Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint8Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint8Display.ScaleFactor = 0.336189258098602
tTKSphereFromPoint8Display.SelectScaleArray = 'None'
tTKSphereFromPoint8Display.GlyphType = 'Arrow'
tTKSphereFromPoint8Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint8Display.GaussianRadius = 0.0168094629049301
tTKSphereFromPoint8Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint8Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint8Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint8Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint8Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint8Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint8Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint8Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint8Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint8Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint8Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint8Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint8Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint8Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint8Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint8Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint8Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint8Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint8Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint8Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from slice5
slice5Display = Show(slice5, renderView11)

# trace defaults for the display properties.
slice5Display.Representation = 'Surface'
slice5Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice5Display.LookupTable = splatterValuesLUT
slice5Display.Opacity = 0.5
slice5Display.Specular = 1.0
slice5Display.OSPRayScaleArray = 'SplatterValues'
slice5Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice5Display.SelectOrientationVectors = 'None'
slice5Display.ScaleFactor = 0.391468095779419
slice5Display.SelectScaleArray = 'SplatterValues'
slice5Display.GlyphType = 'Arrow'
slice5Display.GlyphTableIndexArray = 'SplatterValues'
slice5Display.GaussianRadius = 0.0195734047889709
slice5Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice5Display.ScaleTransferFunction = 'PiecewiseFunction'
slice5Display.OpacityArray = ['POINTS', 'SplatterValues']
slice5Display.OpacityTransferFunction = 'PiecewiseFunction'
slice5Display.DataAxesGrid = 'GridAxesRepresentation'
slice5Display.SelectionCellLabelFontFile = ''
slice5Display.SelectionPointLabelFontFile = ''
slice5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 173.730141581087, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 173.730141581087, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice5Display.DataAxesGrid.XTitleFontFile = ''
slice5Display.DataAxesGrid.YTitleFontFile = ''
slice5Display.DataAxesGrid.ZTitleFontFile = ''
slice5Display.DataAxesGrid.XLabelFontFile = ''
slice5Display.DataAxesGrid.YLabelFontFile = ''
slice5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice5Display.PolarAxes.PolarAxisTitleFontFile = ''
slice5Display.PolarAxes.PolarAxisLabelFontFile = ''
slice5Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint3
tTKSphereFromPoint3Display = Show(tTKSphereFromPoint3, renderView2)

# trace defaults for the display properties.
tTKSphereFromPoint3Display.Representation = 'Surface'
tTKSphereFromPoint3Display.ColorArrayName = [None, '']
tTKSphereFromPoint3Display.Opacity = 0.75
tTKSphereFromPoint3Display.Specular = 1.0
tTKSphereFromPoint3Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint3Display.ScaleFactor = 0.384070563316345
tTKSphereFromPoint3Display.SelectScaleArray = 'None'
tTKSphereFromPoint3Display.GlyphType = 'Arrow'
tTKSphereFromPoint3Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint3Display.GaussianRadius = 0.0192035281658173
tTKSphereFromPoint3Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint3Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint3Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint3Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint3Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

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

# show data from slice2
slice2Display = Show(slice2, renderView2)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice2Display.LookupTable = splatterValuesLUT
slice2Display.Opacity = 0.5
slice2Display.Specular = 1.0
slice2Display.OSPRayScaleArray = 'SplatterValues'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.442946171760559
slice2Display.SelectScaleArray = 'SplatterValues'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'SplatterValues'
slice2Display.GaussianRadius = 0.022147308588028
slice2Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'SplatterValues']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.SelectionCellLabelFontFile = ''
slice2Display.SelectionPointLabelFontFile = ''
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.5595639552215, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.5595639552215, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitleFontFile = ''
slice2Display.DataAxesGrid.YTitleFontFile = ''
slice2Display.DataAxesGrid.ZTitleFontFile = ''
slice2Display.DataAxesGrid.XLabelFontFile = ''
slice2Display.DataAxesGrid.YLabelFontFile = ''
slice2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice2Display.PolarAxes.PolarAxisTitleFontFile = ''
slice2Display.PolarAxes.PolarAxisLabelFontFile = ''
slice2Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint7
tTKSphereFromPoint7Display = Show(tTKSphereFromPoint7, renderView3)

# trace defaults for the display properties.
tTKSphereFromPoint7Display.Representation = 'Surface'
tTKSphereFromPoint7Display.ColorArrayName = [None, '']
tTKSphereFromPoint7Display.Opacity = 0.75
tTKSphereFromPoint7Display.Specular = 1.0
tTKSphereFromPoint7Display.SpecularPower = 50.0
tTKSphereFromPoint7Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint7Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint7Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint7Display.ScaleFactor = 0.61384768486023
tTKSphereFromPoint7Display.SelectScaleArray = 'None'
tTKSphereFromPoint7Display.GlyphType = 'Arrow'
tTKSphereFromPoint7Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint7Display.GaussianRadius = 0.0306923842430115
tTKSphereFromPoint7Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint7Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint7Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint7Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint7Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint7Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint7Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint7Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint7Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint7Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint7Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint7Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint7Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint7Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint7Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint7Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint7Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint7Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint7Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint7Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from slice4
slice4Display = Show(slice4, renderView3)

# trace defaults for the display properties.
slice4Display.Representation = 'Surface'
slice4Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice4Display.LookupTable = splatterValuesLUT
slice4Display.Opacity = 0.5
slice4Display.Specular = 1.0
slice4Display.SpecularPower = 50.0
slice4Display.OSPRayScaleArray = 'SplatterValues'
slice4Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice4Display.SelectOrientationVectors = 'None'
slice4Display.ScaleFactor = 0.724658203125
slice4Display.SelectScaleArray = 'SplatterValues'
slice4Display.GlyphType = 'Arrow'
slice4Display.GlyphTableIndexArray = 'SplatterValues'
slice4Display.GaussianRadius = 0.03623291015625
slice4Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice4Display.ScaleTransferFunction = 'PiecewiseFunction'
slice4Display.OpacityArray = ['POINTS', 'SplatterValues']
slice4Display.OpacityTransferFunction = 'PiecewiseFunction'
slice4Display.DataAxesGrid = 'GridAxesRepresentation'
slice4Display.SelectionCellLabelFontFile = ''
slice4Display.SelectionPointLabelFontFile = ''
slice4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.717407156686, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 19.717407156686, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice4Display.DataAxesGrid.XTitleFontFile = ''
slice4Display.DataAxesGrid.YTitleFontFile = ''
slice4Display.DataAxesGrid.ZTitleFontFile = ''
slice4Display.DataAxesGrid.XLabelFontFile = ''
slice4Display.DataAxesGrid.YLabelFontFile = ''
slice4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice4Display.PolarAxes.PolarAxisTitleFontFile = ''
slice4Display.PolarAxes.PolarAxisLabelFontFile = ''
slice4Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from tTKSphereFromPoint5
tTKSphereFromPoint5Display = Show(tTKSphereFromPoint5, renderView4)

# trace defaults for the display properties.
tTKSphereFromPoint5Display.Representation = 'Surface'
tTKSphereFromPoint5Display.ColorArrayName = [None, '']
tTKSphereFromPoint5Display.Opacity = 0.75
tTKSphereFromPoint5Display.Specular = 1.0
tTKSphereFromPoint5Display.OSPRayScaleArray = 'Normals'
tTKSphereFromPoint5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.SelectOrientationVectors = 'None'
tTKSphereFromPoint5Display.ScaleFactor = 0.536806011199951
tTKSphereFromPoint5Display.SelectScaleArray = 'None'
tTKSphereFromPoint5Display.GlyphType = 'Arrow'
tTKSphereFromPoint5Display.GlyphTableIndexArray = 'None'
tTKSphereFromPoint5Display.GaussianRadius = 0.0268403005599976
tTKSphereFromPoint5Display.SetScaleArray = ['POINTS', 'Normals']
tTKSphereFromPoint5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.OpacityArray = ['POINTS', 'Normals']
tTKSphereFromPoint5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint5Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint5Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint5Display.ScaleTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint5Display.OpacityTransferFunction.Points = [-0.996584475040436, 0.0, 0.5, 0.0, 0.996584475040436, 1.0, 0.5, 0.0]

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

# show data from slice3
slice3Display = Show(slice3, renderView4)

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'SplatterValues']
slice3Display.LookupTable = splatterValuesLUT
slice3Display.Opacity = 0.5
slice3Display.Specular = 1.0
slice3Display.OSPRayScaleArray = 'SplatterValues'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.ScaleFactor = 0.6262286901474
slice3Display.SelectScaleArray = 'SplatterValues'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'SplatterValues'
slice3Display.GaussianRadius = 0.03131143450737
slice3Display.SetScaleArray = ['POINTS', 'SplatterValues']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'SplatterValues']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.SelectionCellLabelFontFile = ''
slice3Display.SelectionPointLabelFontFile = ''
slice3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 149.324656219048, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 149.324656219048, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice3Display.DataAxesGrid.XTitleFontFile = ''
slice3Display.DataAxesGrid.YTitleFontFile = ''
slice3Display.DataAxesGrid.ZTitleFontFile = ''
slice3Display.DataAxesGrid.XLabelFontFile = ''
slice3Display.DataAxesGrid.YLabelFontFile = ''
slice3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice3Display.PolarAxes.PolarAxisTitleFontFile = ''
slice3Display.PolarAxes.PolarAxisLabelFontFile = ''
slice3Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from tube5
tube5Display = Show(tube5, renderView5)

# trace defaults for the display properties.
tube5Display.Representation = 'Surface'
tube5Display.ColorArrayName = [None, '']
tube5Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube5Display.Specular = 1.0
tube5Display.OSPRayScaleArray = 'CellDimension'
tube5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube5Display.SelectOrientationVectors = 'CellDimension'
tube5Display.ScaleFactor = 0.404458475112915
tube5Display.SelectScaleArray = 'CellDimension'
tube5Display.GlyphType = 'Arrow'
tube5Display.GlyphTableIndexArray = 'CellDimension'
tube5Display.GaussianRadius = 0.0202229237556458
tube5Display.SetScaleArray = ['POINTS', 'CellDimension']
tube5Display.ScaleTransferFunction = 'PiecewiseFunction'
tube5Display.OpacityArray = ['POINTS', 'CellDimension']
tube5Display.OpacityTransferFunction = 'PiecewiseFunction'
tube5Display.DataAxesGrid = 'GridAxesRepresentation'
tube5Display.SelectionCellLabelFontFile = ''
tube5Display.SelectionPointLabelFontFile = ''
tube5Display.PolarAxes = 'PolarAxesRepresentation'

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

# show data from tTKTopologicalSimplification5
tTKTopologicalSimplification5Display = Show(tTKTopologicalSimplification5, renderView5)

# trace defaults for the display properties.
tTKTopologicalSimplification5Display.Representation = 'Surface'
tTKTopologicalSimplification5Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification5Display.Specular = 1.0
tTKTopologicalSimplification5Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification5Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification5Display.ScaleFactor = 0.391468095779419
tTKTopologicalSimplification5Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification5Display.GlyphType = 'Arrow'
tTKTopologicalSimplification5Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification5Display.GaussianRadius = 0.0195734047889709
tTKTopologicalSimplification5Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification5Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification5Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification5Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 216.082581438871, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 216.082581438871, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification5Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification5Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification5Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification5Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification5Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification5Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification5Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKMorseSmaleComplex5_2
tTKMorseSmaleComplex5Display = Show(OutputPort(tTKMorseSmaleComplex5, 3), renderView5)

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.RGBPoints = [-1.0, 0.278431372549, 0.278431372549, 0.858823529412, -0.571, 0.0, 0.0, 0.360784313725, -0.145, 0.0, 1.0, 1.0, 0.287, 0.0, 0.501960784314, 0.0, 0.713, 1.0, 1.0, 0.0, 1.142, 1.0, 0.380392156863, 0.0, 1.571, 0.419607843137, 0.0, 0.0, 2.0, 0.878431372549, 0.301960784314, 0.301960784314]
ascendingManifoldLUT.ColorSpace = 'RGB'
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKMorseSmaleComplex5Display.Representation = 'Surface'
tTKMorseSmaleComplex5Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex5Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex5Display.Opacity = 0.5
tTKMorseSmaleComplex5Display.Specular = 1.0
tTKMorseSmaleComplex5Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex5Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex5Display.ScaleFactor = 0.391468095779419
tTKMorseSmaleComplex5Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex5Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex5Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex5Display.GaussianRadius = 0.0195734047889709
tTKMorseSmaleComplex5Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex5Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex5Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex5Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex5Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex5Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex5Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 216.082581438871, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 216.082581438871, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex5Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex5Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex5Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex5Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex5Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex5Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex5Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex5Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex5Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex5Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint10
tTKSphereFromPoint10Display = Show(tTKSphereFromPoint10, renderView5)

# trace defaults for the display properties.
tTKSphereFromPoint10Display.Representation = 'Surface'
tTKSphereFromPoint10Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint10Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint10Display.Specular = 1.0
tTKSphereFromPoint10Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint10Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint10Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint10Display.ScaleFactor = 0.336189258098602
tTKSphereFromPoint10Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint10Display.GlyphType = 'Arrow'
tTKSphereFromPoint10Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint10Display.GaussianRadius = 0.0168094629049301
tTKSphereFromPoint10Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint10Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint10Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint10Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint10Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint10Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint10Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint10Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint10Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint10Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint10Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint10Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint10Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint10Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint10Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint10Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint10Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint10Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint10Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint10Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView6'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification1
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView6)

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Surface'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification1Display.Specular = 1.0
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification1Display.ScaleFactor = 0.47112181186676
tTKTopologicalSimplification1Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification1Display.GaussianRadius = 0.023556090593338
tTKTopologicalSimplification1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification1Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 37.7877598418108, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 37.7877598418108, 1.0, 0.5, 0.0]

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

# show data from tTKMorseSmaleComplex1_2
tTKMorseSmaleComplex1Display = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView6)

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex1Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex1Display.Opacity = 0.5
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex1Display.ScaleFactor = 0.47112181186676
tTKMorseSmaleComplex1Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.023556090593338
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex1Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 37.7877598418108, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 37.7877598418108, 1.0, 0.5, 0.0]

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
tTKSphereFromPoint1Display = Show(tTKSphereFromPoint1, renderView6)

# trace defaults for the display properties.
tTKSphereFromPoint1Display.Representation = 'Surface'
tTKSphereFromPoint1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint1Display.Specular = 1.0
tTKSphereFromPoint1Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint1Display.ScaleFactor = 0.492259955406189
tTKSphereFromPoint1Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint1Display.GlyphType = 'Arrow'
tTKSphereFromPoint1Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint1Display.GaussianRadius = 0.0246129977703094
tTKSphereFromPoint1Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint1Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint1Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint1Display.PolarAxes = 'PolarAxesRepresentation'

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
tube1Display = Show(tube1, renderView6)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube1Display.Specular = 1.0
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'CellDimension'
tube1Display.ScaleFactor = 0.479194259643555
tube1Display.SelectScaleArray = 'CellDimension'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'CellDimension'
tube1Display.GaussianRadius = 0.0239597129821777
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

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
# setup the visualization in view 'renderView7'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification2
tTKTopologicalSimplification2Display = Show(tTKTopologicalSimplification2, renderView7)

# trace defaults for the display properties.
tTKTopologicalSimplification2Display.Representation = 'Surface'
tTKTopologicalSimplification2Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification2Display.Specular = 1.0
tTKTopologicalSimplification2Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification2Display.ScaleFactor = 0.442946171760559
tTKTopologicalSimplification2Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification2Display.GlyphType = 'Arrow'
tTKTopologicalSimplification2Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification2Display.GaussianRadius = 0.022147308588028
tTKTopologicalSimplification2Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification2Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification2Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.2741169239563, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.2741169239563, 1.0, 0.5, 0.0]

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

# show data from tTKMorseSmaleComplex2_1
tTKMorseSmaleComplex2Display = Show(OutputPort(tTKMorseSmaleComplex2, 3), renderView7)

# trace defaults for the display properties.
tTKMorseSmaleComplex2Display.Representation = 'Surface'
tTKMorseSmaleComplex2Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex2Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex2Display.Opacity = 0.5
tTKMorseSmaleComplex2Display.Specular = 1.0
tTKMorseSmaleComplex2Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex2Display.ScaleFactor = 0.442946171760559
tTKMorseSmaleComplex2Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex2Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex2Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex2Display.GaussianRadius = 0.022147308588028
tTKMorseSmaleComplex2Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex2Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex2Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.2741169239563, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 49.2741169239563, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex2Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex2Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKSphereFromPoint4
tTKSphereFromPoint4Display = Show(tTKSphereFromPoint4, renderView7)

# trace defaults for the display properties.
tTKSphereFromPoint4Display.Representation = 'Surface'
tTKSphereFromPoint4Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint4Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint4Display.Specular = 1.0
tTKSphereFromPoint4Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint4Display.ScaleFactor = 0.384070563316345
tTKSphereFromPoint4Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint4Display.GlyphType = 'Arrow'
tTKSphereFromPoint4Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint4Display.GaussianRadius = 0.0192035281658173
tTKSphereFromPoint4Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint4Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint4Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint4Display.PolarAxes = 'PolarAxesRepresentation'

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

# show data from tube2
tube2Display = Show(tube2, renderView7)

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = [None, '']
tube2Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube2Display.Specular = 1.0
tube2Display.OSPRayScaleArray = 'CellDimension'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'CellDimension'
tube2Display.ScaleFactor = 0.457946181297302
tube2Display.SelectScaleArray = 'CellDimension'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'CellDimension'
tube2Display.GaussianRadius = 0.0228973090648651
tube2Display.SetScaleArray = ['POINTS', 'CellDimension']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'CellDimension']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.SelectionCellLabelFontFile = ''
tube2Display.SelectionPointLabelFontFile = ''
tube2Display.PolarAxes = 'PolarAxesRepresentation'

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
# setup the visualization in view 'renderView8'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification3
tTKTopologicalSimplification3Display = Show(tTKTopologicalSimplification3, renderView8)

# trace defaults for the display properties.
tTKTopologicalSimplification3Display.Representation = 'Surface'
tTKTopologicalSimplification3Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification3Display.Specular = 1.0
tTKTopologicalSimplification3Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification3Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification3Display.ScaleFactor = 0.6262286901474
tTKTopologicalSimplification3Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification3Display.GlyphType = 'Arrow'
tTKTopologicalSimplification3Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification3Display.GaussianRadius = 0.03131143450737
tTKTopologicalSimplification3Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification3Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification3Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification3Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 299.281584169491, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 299.281584169491, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification3Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification3Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification3Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification3Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification3Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKMorseSmaleComplex3_1
tTKMorseSmaleComplex3Display = Show(OutputPort(tTKMorseSmaleComplex3, 3), renderView8)

# trace defaults for the display properties.
tTKMorseSmaleComplex3Display.Representation = 'Surface'
tTKMorseSmaleComplex3Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex3Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex3Display.Opacity = 0.5
tTKMorseSmaleComplex3Display.Specular = 1.0
tTKMorseSmaleComplex3Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex3Display.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex3Display.ScaleFactor = 0.6262286901474
tTKMorseSmaleComplex3Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex3Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex3Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex3Display.GaussianRadius = 0.03131143450737
tTKMorseSmaleComplex3Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex3Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex3Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex3Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 345.557953185823, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 345.557953185823, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex3Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex3Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex3Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex3Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex3Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex3Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex3Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex3Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube3
tube3Display = Show(tube3, renderView8)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube3Display.Specular = 1.0
tube3Display.OSPRayScaleArray = 'CellDimension'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'CellDimension'
tube3Display.ScaleFactor = 0.634888958930969
tube3Display.SelectScaleArray = 'CellDimension'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'CellDimension'
tube3Display.GaussianRadius = 0.0317444479465485
tube3Display.SetScaleArray = ['POINTS', 'CellDimension']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'CellDimension']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.SelectionCellLabelFontFile = ''
tube3Display.SelectionPointLabelFontFile = ''
tube3Display.PolarAxes = 'PolarAxesRepresentation'

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

# show data from tTKSphereFromPoint6
tTKSphereFromPoint6Display = Show(tTKSphereFromPoint6, renderView8)

# trace defaults for the display properties.
tTKSphereFromPoint6Display.Representation = 'Surface'
tTKSphereFromPoint6Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint6Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint6Display.Specular = 1.0
tTKSphereFromPoint6Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint6Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint6Display.ScaleFactor = 0.536806011199951
tTKSphereFromPoint6Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint6Display.GlyphType = 'Arrow'
tTKSphereFromPoint6Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint6Display.GaussianRadius = 0.0268403005599976
tTKSphereFromPoint6Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint6Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint6Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint6Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint6Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint6Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint6Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint6Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint6Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView9'
# ----------------------------------------------------------------

# show data from tTKTopologicalSimplification4
tTKTopologicalSimplification4Display = Show(tTKTopologicalSimplification4, renderView9)

# trace defaults for the display properties.
tTKTopologicalSimplification4Display.Representation = 'Surface'
tTKTopologicalSimplification4Display.ColorArrayName = ['POINTS', '']
tTKTopologicalSimplification4Display.Specular = 1.0
tTKTopologicalSimplification4Display.OSPRayScaleArray = 'SplatterValues'
tTKTopologicalSimplification4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification4Display.SelectOrientationVectors = 'None'
tTKTopologicalSimplification4Display.ScaleFactor = 0.724658203125
tTKTopologicalSimplification4Display.SelectScaleArray = 'SplatterValues'
tTKTopologicalSimplification4Display.GlyphType = 'Arrow'
tTKTopologicalSimplification4Display.GlyphTableIndexArray = 'SplatterValues'
tTKTopologicalSimplification4Display.GaussianRadius = 0.03623291015625
tTKTopologicalSimplification4Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification4Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification4Display.SelectionCellLabelFontFile = ''
tTKTopologicalSimplification4Display.SelectionPointLabelFontFile = ''
tTKTopologicalSimplification4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 154.381460801815, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 154.381460801815, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKTopologicalSimplification4Display.DataAxesGrid.XTitleFontFile = ''
tTKTopologicalSimplification4Display.DataAxesGrid.YTitleFontFile = ''
tTKTopologicalSimplification4Display.DataAxesGrid.ZTitleFontFile = ''
tTKTopologicalSimplification4Display.DataAxesGrid.XLabelFontFile = ''
tTKTopologicalSimplification4Display.DataAxesGrid.YLabelFontFile = ''
tTKTopologicalSimplification4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKTopologicalSimplification4Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKTopologicalSimplification4Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKTopologicalSimplification4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKTopologicalSimplification4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKMorseSmaleComplex4
tTKMorseSmaleComplex4Display = Show(tTKMorseSmaleComplex4, renderView9)

# get opacity transfer function/opacity map for 'SplatterValues'
splatterValuesPWF = GetOpacityTransferFunction('SplatterValues')
splatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 19.717407156686, 1.0, 0.5, 0.0]
splatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKMorseSmaleComplex4Display.Representation = 'Surface'
tTKMorseSmaleComplex4Display.ColorArrayName = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex4Display.LookupTable = splatterValuesLUT
tTKMorseSmaleComplex4Display.Specular = 1.0
tTKMorseSmaleComplex4Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display.SelectOrientationVectors = 'CellDimension'
tTKMorseSmaleComplex4Display.ScaleFactor = 0.724658203125
tTKMorseSmaleComplex4Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex4Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex4Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex4Display.GaussianRadius = 0.03623291015625
tTKMorseSmaleComplex4Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex4Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display.OpacityArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex4Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex4Display.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex4Display.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex4Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex4Display.ScalarOpacityFunction = splatterValuesPWF
tTKMorseSmaleComplex4Display.ScalarOpacityUnitDistance = 9.11935634138722

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex4Display.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex4Display.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex4Display.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex4Display.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex4Display.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex4Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex4Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex4Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex4Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex4Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# find source
tTKMorseSmaleComplex4_3 = FindSource('TTKMorseSmaleComplex4')

# show data from tTKMorseSmaleComplex4_3
tTKMorseSmaleComplex4Display_1 = Show(OutputPort(tTKMorseSmaleComplex4, 2), renderView9)

# trace defaults for the display properties.
tTKMorseSmaleComplex4Display_1.Representation = 'Surface'
tTKMorseSmaleComplex4Display_1.ColorArrayName = [None, '']
tTKMorseSmaleComplex4Display_1.Specular = 1.0
tTKMorseSmaleComplex4Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_1.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex4Display_1.ScaleFactor = -2e+298
tTKMorseSmaleComplex4Display_1.SelectScaleArray = 'None'
tTKMorseSmaleComplex4Display_1.GlyphType = 'Arrow'
tTKMorseSmaleComplex4Display_1.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex4Display_1.GaussianRadius = -1e+297
tTKMorseSmaleComplex4Display_1.SetScaleArray = [None, '']
tTKMorseSmaleComplex4Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_1.OpacityArray = [None, '']
tTKMorseSmaleComplex4Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex4Display_1.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex4Display_1.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex4Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex4Display_1.OSPRayScaleFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex4Display_1.ScaleTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex4Display_1.OpacityTransferFunction.Points = [0.216992005705833, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex4Display_1.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex4Display_1.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex4Display_1.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex4Display_1.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex4Display_1.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex4Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex4Display_1.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex4Display_1.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex4Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex4Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tTKMorseSmaleComplex4_2
tTKMorseSmaleComplex4Display_2 = Show(OutputPort(tTKMorseSmaleComplex4, 3), renderView9)

# trace defaults for the display properties.
tTKMorseSmaleComplex4Display_2.Representation = 'Surface'
tTKMorseSmaleComplex4Display_2.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex4Display_2.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex4Display_2.Opacity = 0.5
tTKMorseSmaleComplex4Display_2.Specular = 1.0
tTKMorseSmaleComplex4Display_2.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex4Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_2.SelectOrientationVectors = 'AscendingManifold'
tTKMorseSmaleComplex4Display_2.ScaleFactor = 0.724658203125
tTKMorseSmaleComplex4Display_2.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex4Display_2.GlyphType = 'Arrow'
tTKMorseSmaleComplex4Display_2.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex4Display_2.GaussianRadius = 0.03623291015625
tTKMorseSmaleComplex4Display_2.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex4Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_2.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex4Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex4Display_2.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex4Display_2.SelectionCellLabelFontFile = ''
tTKMorseSmaleComplex4Display_2.SelectionPointLabelFontFile = ''
tTKMorseSmaleComplex4Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex4Display_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 25.7603042581899, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex4Display_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 25.7603042581899, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKMorseSmaleComplex4Display_2.DataAxesGrid.XTitleFontFile = ''
tTKMorseSmaleComplex4Display_2.DataAxesGrid.YTitleFontFile = ''
tTKMorseSmaleComplex4Display_2.DataAxesGrid.ZTitleFontFile = ''
tTKMorseSmaleComplex4Display_2.DataAxesGrid.XLabelFontFile = ''
tTKMorseSmaleComplex4Display_2.DataAxesGrid.YLabelFontFile = ''
tTKMorseSmaleComplex4Display_2.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKMorseSmaleComplex4Display_2.PolarAxes.PolarAxisTitleFontFile = ''
tTKMorseSmaleComplex4Display_2.PolarAxes.PolarAxisLabelFontFile = ''
tTKMorseSmaleComplex4Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
tTKMorseSmaleComplex4Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data from tube4
tube4Display = Show(tube4, renderView9)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = [None, '']
tube4Display.DiffuseColor = [0.180392156862745, 0.176470588235294, 0.176470588235294]
tube4Display.Specular = 1.0
tube4Display.OSPRayScaleArray = 'CellDimension'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'CellDimension'
tube4Display.ScaleFactor = 0.733318471908569
tube4Display.SelectScaleArray = 'CellDimension'
tube4Display.GlyphType = 'Arrow'
tube4Display.GlyphTableIndexArray = 'CellDimension'
tube4Display.GaussianRadius = 0.0366659235954285
tube4Display.SetScaleArray = ['POINTS', 'CellDimension']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'CellDimension']
tube4Display.OpacityTransferFunction = 'PiecewiseFunction'
tube4Display.DataAxesGrid = 'GridAxesRepresentation'
tube4Display.SelectionCellLabelFontFile = ''
tube4Display.SelectionPointLabelFontFile = ''
tube4Display.PolarAxes = 'PolarAxesRepresentation'

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

# show data from tTKSphereFromPoint9
tTKSphereFromPoint9Display = Show(tTKSphereFromPoint9, renderView9)

# trace defaults for the display properties.
tTKSphereFromPoint9Display.Representation = 'Surface'
tTKSphereFromPoint9Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint9Display.LookupTable = ascendingManifoldLUT
tTKSphereFromPoint9Display.Specular = 1.0
tTKSphereFromPoint9Display.OSPRayScaleArray = 'AscendingManifold'
tTKSphereFromPoint9Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKSphereFromPoint9Display.SelectOrientationVectors = 'AscendingManifold'
tTKSphereFromPoint9Display.ScaleFactor = 0.61384768486023
tTKSphereFromPoint9Display.SelectScaleArray = 'AscendingManifold'
tTKSphereFromPoint9Display.GlyphType = 'Arrow'
tTKSphereFromPoint9Display.GlyphTableIndexArray = 'AscendingManifold'
tTKSphereFromPoint9Display.GaussianRadius = 0.0306923842430115
tTKSphereFromPoint9Display.SetScaleArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint9Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint9Display.OpacityArray = ['POINTS', 'AscendingManifold']
tTKSphereFromPoint9Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKSphereFromPoint9Display.DataAxesGrid = 'GridAxesRepresentation'
tTKSphereFromPoint9Display.SelectionCellLabelFontFile = ''
tTKSphereFromPoint9Display.SelectionPointLabelFontFile = ''
tTKSphereFromPoint9Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKSphereFromPoint9Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKSphereFromPoint9Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tTKSphereFromPoint9Display.DataAxesGrid.XTitleFontFile = ''
tTKSphereFromPoint9Display.DataAxesGrid.YTitleFontFile = ''
tTKSphereFromPoint9Display.DataAxesGrid.ZTitleFontFile = ''
tTKSphereFromPoint9Display.DataAxesGrid.XLabelFontFile = ''
tTKSphereFromPoint9Display.DataAxesGrid.YLabelFontFile = ''
tTKSphereFromPoint9Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tTKSphereFromPoint9Display.PolarAxes.PolarAxisTitleFontFile = ''
tTKSphereFromPoint9Display.PolarAxes.PolarAxisLabelFontFile = ''
tTKSphereFromPoint9Display.PolarAxes.LastRadialAxisTextFontFile = ''
tTKSphereFromPoint9Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

tTKSphereFromPoint5.DebugLevel = int(debugLevel)
if tTKSphereFromPoint5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint5, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint5.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint5)))


tTKSphereFromPoint3.DebugLevel = int(debugLevel)
if tTKSphereFromPoint3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint3, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint3.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint3)))


tTKSphereFromPoint2.DebugLevel = int(debugLevel)
if tTKSphereFromPoint2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint2, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint2.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint2)))


tTKSphereFromPoint8.DebugLevel = int(debugLevel)
if tTKSphereFromPoint8.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint8.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint8_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint8, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint8.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint8)))


tTKSphereFromPoint7.DebugLevel = int(debugLevel)
if tTKSphereFromPoint7.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint7.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint7_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint7, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint7.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint7)))


tTKPersistenceDiagram4.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram4, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram4.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram4)))


tTKTopologicalSimplification4.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification4, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification4.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification4)))


tTKMorseSmaleComplex4.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex4, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex4.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex4)))


tTKGeometrySmoother4.DebugLevel = int(debugLevel)
if tTKGeometrySmoother4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother4, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother4.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother4)))


tTKDataSetInterpolator4.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator4, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator4.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator4)))


tTKSphereFromPoint9.DebugLevel = int(debugLevel)
if tTKSphereFromPoint9.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint9.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint9_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint9, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint9.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint9)))


tTKPersistenceDiagram3.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram3, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram3.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram3)))


tTKTopologicalSimplification3.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification3, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification3.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification3)))


tTKMorseSmaleComplex3.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex3, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex3.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex3)))


tTKDataSetInterpolator3.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator3, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator3.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator3)))


tTKSphereFromPoint6.DebugLevel = int(debugLevel)
if tTKSphereFromPoint6.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint6.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint6_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint6, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint6.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint6)))


tTKGeometrySmoother3.DebugLevel = int(debugLevel)
if tTKGeometrySmoother3.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother3.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother3_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother3, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother3.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother3)))


tTKPersistenceDiagram2.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram2, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram2.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram2)))


tTKTopologicalSimplification2.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification2, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification2.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification2)))


tTKMorseSmaleComplex2.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex2, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex2.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex2)))


tTKDataSetInterpolator2.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator2, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator2.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator2)))


tTKSphereFromPoint4.DebugLevel = int(debugLevel)
if tTKSphereFromPoint4.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint4.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint4_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint4, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint4.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint4)))


tTKGeometrySmoother2.DebugLevel = int(debugLevel)
if tTKGeometrySmoother2.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother2.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother2_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother2, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother2.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother2)))


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


tTKGeometrySmoother1.DebugLevel = int(debugLevel)
if tTKGeometrySmoother1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother1, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother1.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother1)))


tTKDataSetInterpolator1.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator1, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator1.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator1)))


tTKSphereFromPoint1.DebugLevel = int(debugLevel)
if tTKSphereFromPoint1.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint1.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint1_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint1, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint1.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint1)))


tTKPersistenceDiagram5.DebugLevel = int(debugLevel)
if tTKPersistenceDiagram5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKPersistenceDiagram5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKPersistenceDiagram5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKPersistenceDiagram5, i)))
else:
	SaveData(outputDirectory + 'tTKPersistenceDiagram5.vtu',
		CleantoGrid(OutputPort(tTKPersistenceDiagram5)))


tTKTopologicalSimplification5.DebugLevel = int(debugLevel)
if tTKTopologicalSimplification5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKTopologicalSimplification5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKTopologicalSimplification5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKTopologicalSimplification5, i)))
else:
	SaveData(outputDirectory + 'tTKTopologicalSimplification5.vtu',
		CleantoGrid(OutputPort(tTKTopologicalSimplification5)))


tTKMorseSmaleComplex5.DebugLevel = int(debugLevel)
if tTKMorseSmaleComplex5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKMorseSmaleComplex5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKMorseSmaleComplex5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKMorseSmaleComplex5, i)))
else:
	SaveData(outputDirectory + 'tTKMorseSmaleComplex5.vtu',
		CleantoGrid(OutputPort(tTKMorseSmaleComplex5)))


tTKGeometrySmoother5.DebugLevel = int(debugLevel)
if tTKGeometrySmoother5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKGeometrySmoother5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKGeometrySmoother5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKGeometrySmoother5, i)))
else:
	SaveData(outputDirectory + 'tTKGeometrySmoother5.vtu',
		CleantoGrid(OutputPort(tTKGeometrySmoother5)))


tTKDataSetInterpolator5.DebugLevel = int(debugLevel)
if tTKDataSetInterpolator5.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKDataSetInterpolator5.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKDataSetInterpolator5_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKDataSetInterpolator5, i)))
else:
	SaveData(outputDirectory + 'tTKDataSetInterpolator5.vtu',
		CleantoGrid(OutputPort(tTKDataSetInterpolator5)))


tTKSphereFromPoint10.DebugLevel = int(debugLevel)
if tTKSphereFromPoint10.GetNumberOfOutputPorts() != 1:
	for i in range(0, tTKSphereFromPoint10.GetNumberOfOutputPorts()):
		SaveData(outputDirectory + 'tTKSphereFromPoint10_' + str(i) + '.vtu',
			CleantoGrid(OutputPort(tTKSphereFromPoint10, i)))
else:
	SaveData(outputDirectory + 'tTKSphereFromPoint10.vtu',
		CleantoGrid(OutputPort(tTKSphereFromPoint10)))
