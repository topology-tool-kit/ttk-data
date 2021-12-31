#### import the simple module from the paraview
from paraview.simple import *

# paraview 5.9 VS 5.10 compatibility
def ThresholdAbove(threshold, value):
    try:
        # paraview 5.9
        threshold.ThresholdRange = [value, 9999999]
    except:
        # paraview 5.10
        threshold.ThresholdMethod = "Above Upper Threshold"
        threshold.UpperThreshold = value

# create a new 'TTK CinemaReader'
ttkCinemaReader1 = TTKCinemaReader(DatabasePath='ViscousFingers.cdb')

# create a new 'TTK CinemaQuery'
ttkCinemaQuery1 = TTKCinemaQuery(InputTable=ttkCinemaReader1)
ttkCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
WHERE Sim='run01'
ORDER BY Time
LIMIT 100 OFFSET 20"""

# create a new 'TTK ForEach'
ttkForEach1 = TTKForEach(Input=ttkCinemaQuery1)

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader1 = TTKCinemaProductReader(Input=ttkForEach1)

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(Input=ttkCinemaProductReader1)

# create a new 'Clip'
clip1 = Clip(Input=mergeBlocks1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Value = 38.38161849975586

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [31.5, 31.5, 50.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# create a new 'Threshold'
threshold1 = Threshold(Input=clip1)
threshold1.Scalars = ['POINTS', 'ImageFile']
ThresholdAbove(threshold1, 20)

# create a new 'Threshold'
threshold2 = Threshold(Input=clip1)
threshold2.Scalars = ['POINTS', 'ImageFile']
ThresholdAbove(threshold2, 28)

# create a new 'Threshold'
threshold3 = Threshold(Input=clip1)
threshold3.Scalars = ['POINTS', 'ImageFile']
ThresholdAbove(threshold3, 32)

# create a new 'Connectivity'
connectivity1 = Connectivity(Input=threshold1)

# create a new 'Connectivity'
connectivity2 = Connectivity(Input=threshold2)

# create a new 'Connectivity'
connectivity3 = Connectivity(Input=threshold3)

# create a new 'TTK BlockAggregator'
ttkBlockAggregator5 = TTKBlockAggregator(Input=connectivity1)
ttkBlockAggregator5.ForceReset = 1

# create a new 'TTK BlockAggregator'
ttkBlockAggregator6 = TTKBlockAggregator(Input=connectivity2)
ttkBlockAggregator6.ForceReset = 1

# create a new 'TTK BlockAggregator'
ttkBlockAggregator7 = TTKBlockAggregator(Input=connectivity3)
ttkBlockAggregator7.ForceReset = 1

# create a new 'TTK BlockAggregator'
ttkBlockAggregator1 = TTKBlockAggregator(Input=[ttkBlockAggregator5, ttkBlockAggregator6, ttkBlockAggregator7])
ttkBlockAggregator1.ForceReset = 1
ttkBlockAggregator1.FlattenInput = 0

# create a new 'TTK ArrayEditor'
ttkArrayEditor1 = TTKArrayEditor(Target=ttkBlockAggregator1,
    Source=ttkCinemaProductReader1)
ttkArrayEditor1.EditorMode = 'Add Arrays from Source'
ttkArrayEditor1.TargetAttributeType = 'Field Data'
ttkArrayEditor1.SourceFieldDataArrays = ['_ttk_IterationInfo']

# create a new 'TTK TrackingFromOverlap'
ttkTrackingFromOverlap1 = TTKTrackingFromOverlap(Input=ttkArrayEditor1)
ttkTrackingFromOverlap1.Labels = 'RegionId'

# create a new 'TTK EndFor'
ttkEndFor1 = TTKEndFor(Data=ttkTrackingFromOverlap1,
    For=ttkForEach1)

# create a new 'Calculator'
calculator1 = Calculator(Input=ttkEndFor1)
calculator1.ResultArrayName = 'Size'
calculator1.Function = 'Size/6000'
calculator1.ResultArrayType = 'Float'

# create a new 'TTK PlanarGraphLayout'
ttkPlanarGraphLayout1 = TTKPlanarGraphLayout(Input=calculator1)
ttkPlanarGraphLayout1.UseSequences = 1
ttkPlanarGraphLayout1.SequenceArray = ['POINTS', 'SequenceIndex']
ttkPlanarGraphLayout1.UseSizes = 1
ttkPlanarGraphLayout1.SizeArray = ['POINTS', 'Size']
ttkPlanarGraphLayout1.UseBranches = 1
ttkPlanarGraphLayout1.BranchArray = ['POINTS', 'BranchId']
ttkPlanarGraphLayout1.UseLevels = 1
ttkPlanarGraphLayout1.LevelArray = ['POINTS', 'LevelIndex']

# create a new 'Calculator'
calculator2 = Calculator(Input=ttkPlanarGraphLayout1)
calculator2.CoordinateResults = 1
calculator2.Function = 'iHat*SequenceIndex+jHat*Layout_Y+kHat*LevelIndex'

# create a new 'TTK MeshGraph'
ttkMeshGraph1 = TTKMeshGraph(Input=calculator2)
ttkMeshGraph1.SizeArray = ['POINTS', 'Size']

SaveData("NestedTrackingGraph.vtu", ttkMeshGraph1)
