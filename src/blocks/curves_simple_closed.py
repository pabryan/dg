#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

t = np.linspace(0.0, 2 * np.pi, 100)
r = 1 + 0.5*np.cos(5*t)

df = pd.DataFrame({"x" : r*np.cos(t), "y" : r*np.sin(t)})

fig = px.line(df, x="x", y="y", title="Simple Closed Curve")
fig.update_layout(showlegend=False)
fig.update_annotations(yshift=20)

fig.update_yaxes(scaleanchor="x", scaleratio=1, row=1, col=1)

fig.write_image("../../docs/img/curves_simple_closed.svg")
