#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

t = np.linspace(-8.0, 8.0, 100)
pitch = 5.0
helixdf = pd.DataFrame({"x" : pitch*np.cos(t), "y" : pitch*np.sin(t), "z" : t})

p = (helixdf.iloc[[60]]).values.tolist()[0]
V = [-pitch*np.sin(p[2]), pitch*np.cos(p[2]), 1]
u = np.linspace(-2.0, 2.0, 100)

tanglinedf = pd.DataFrame({"x": [p[0] + uval * V[0] for uval in u], "y": [p[1] + uval * V[1] for uval in u], "z": [p[2] + uval * V[2] for uval in u]})

n1 = np.linspace(-7.5, 7.5, 100)
n2 = np.linspace(-1.5, 1.5, 100)
N1, N2 = np.meshgrid(n1, n2)
E1 = [np.cos(p[2]), np.sin(p[2]), 0.0]
E2 = [-np.sin(p[2]), np.cos(p[2]), -pitch]
def normalplane_para(e1, e2):
    return (p[0] + e1*E1[0] + e2*E2[0], p[1] + e1*E1[1] + e2*E2[1], p[2] + e1*E1[2] + e2*E2[2])

normalplane_data = normalplane_para(N1, N2)

L1 = pd.DataFrame({"x" : [p[0] + n * E1[0] for n in n1], "y" : [p[1] + n * E1[1] for n in n1], "z" : [p[2] + n * E1[2] for n in n1]})
L2 = pd.DataFrame({"x" : [p[0] + n * E2[0] for n in n2], "y" : [p[1] + n * E2[1] for n in n2], "z" : [p[2] + n * E2[2] for n in n2]})

helix  = go.Scatter3d(x = helixdf["x"], y = helixdf["y"], z = helixdf["z"], mode="lines", showlegend = False)
point = go.Scatter3d(x=[p[0]], y=[p[1]], z=[p[2]], mode="markers", marker=dict(color="red", size=5), showlegend=False)
tangline = go.Scatter3d(x = tanglinedf["x"], y = tanglinedf["y"], z = tanglinedf["z"], mode="lines", showlegend = False)
normalplane = go.Surface(x = normalplane_data[0], y = normalplane_data[1], z = normalplane_data[2], opacity=0.1, showscale=False,  colorscale=["gray","gray"], showlegend=False)
norline1 = go.Scatter3d(x = L1["x"], y = L1["y"], z = L1["z"], mode="lines", line=dict(color="black"), showlegend = False)
norline2 = go.Scatter3d(x = L2["x"], y = L2["y"], z = L2["z"], mode="lines", line=dict(color="black"), showlegend = False)

fig = go.Figure()
fig.add_trace(helix)
fig.add_trace(tangline)
fig.add_trace(point)
fig.add_trace(normalplane)
fig.add_trace(norline1)
fig.add_trace(norline2)

hidegrid = {"showgrid" : False, "showbackground": False, "ticks" : "", "showticklabels" : False, "showaxeslabels" : False, "visible": False}
scene = {"xaxis" : hidegrid, "yaxis" : hidegrid, "zaxis": hidegrid, "aspectmode" : 'data'}
camera = {"eye" : dict(x=0.75, y=0.75, z=0.75)}
fig.update_layout(scene=scene, scene_camera=camera, height=600, width=600)

fig.write_image("../../docs/img/helix_tangent_normal.svg")
