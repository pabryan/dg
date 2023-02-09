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

df = pd.DataFrame({"x" : (np.cos(t))/(1 + np.sin(t)**2), "y" : (np.cos(t) * np.sin(t))/(1 + np.sin(t)**2)})

fig = px.line(df, x="x", y="y", title="Lemniscate of Bernoulli : Closed non-Simple Curve")
fig.update_layout(showlegend=False)
fig.update_annotations(yshift=20)

fig.update_yaxes(scaleanchor="x", range=[-1.0, 1.0], scaleratio=1, row=1, col=1)

fig.write_image("../../docs/img/curves_bernoulli_lemniscate.svg")
