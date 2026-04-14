# Tracking From Critical Points

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/8R04uSiCafE?si=0VMzLa_Uyt_2YYar" frameborder="0"
allowfullscreen></iframe>

## Pipeline description

This example loads a 2D time-varying scalar field and automatically tracks its extrema over
time using the module [TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html), in order to capture the trajectory of the main features of the data (i.e, the vortices). Specifically, the input data describes the orthogonal component of the curl (a measure of vorticity) for a time-varying vector field modeling a mixing von Karman vortex street.

Each extremum captures the center of a vortex. Extrema are tracked over time by solving an optimal assignment problem (supporting mass variation) between consecutive time steps. For each extremum, its position is visualized over time with a distinct color. The top left view shows the position of the extrema at a given time step. The bottom left view shows the same information along with each extremum path through the whole time-space dataset. The right view shows the time-space dataset as well as its tracked topological features with a 3D view, where the third component encodes time.

The animation can be played by hitting the 'Play' control button (green triangle icon, top).

The tracking can be tuned by two main parameters. The persistence threshold selects the topological features to track based on their persistence (decrease this value to track more features). The relative destruction cost defines the destruction cost for a critical point (increase this value to allow for larger displacement from one time step to the next, decrease this value to prevent the tracking from jumping from critical points which are too far from each other).

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/trackingFromCriticalPoints.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/trackingFromCriticalPoints.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/trackingFromCriticalPoints.py
```


## Inputs

- [mixingVonKarman.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/mixingVonKarman.vti): time-varying vorticity (ortoghonal component of the curl) for a mixing 2D von Karman vortex street, with time steps represented by data arrays 'sf_0000', 'sf_0001', ..., 'sf_0149'.

## Outputs

- `mixingVonKarman.vtu`: space-time trajectory of the vortices.

## C++/Python API

[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html)
