#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

t = np.linspace(-1, 1, 50)

absval = pd.DataFrame({"x" : t, "y" : np.abs(t)})
powtwothirds = pd.DataFrame({"x" : t**2, "y" : t**3})

fig = make_subplots(rows=1, cols=2, subplot_titles = (r"$\gamma(t) = (t, |t|) \quad -1 < t < 1$", r"$\gamma(t) = (t^2, t^3) \quad -1 < t < 1$"))
fig.update_annotations(yshift=20)

fig.update_yaxes(scaleanchor="x1", scaleratio=1, row=1, col=1)
fig.update_yaxes(scaleanchor="x2", scaleratio=1, row=1, col=2)

fig.add_trace(go.Scatter(x=absval["x"], y=absval["y"], showlegend=False), row=1, col=1)
fig.add_trace(go.Scatter(x=powtwothirds["x"], y=powtwothirds["y"], showlegend=False), row=1, col=2)

fig.write_html("../../docs/_includes/not_reg_curve_plot.html", include_plotlyjs="cdn", include_mathjax=False, full_html=False)
