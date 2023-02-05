#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

t = np.linspace(-2.5, 2.5, 50)

df = pd.DataFrame({"x" : t**3-4*t, "y" : t**2-4})

fig = px.line(df, x="x", y="y", title="Regular, not simple curve")
fig.update_layout(showlegend=False)
fig.update_annotations(yshift=20)

fig.update_yaxes(scaleanchor="x", scaleratio=1, row=1, col=1)

fig.write_html("../../docs/_includes/regular_non_simple_curve.html", include_plotlyjs="cdn", include_mathjax=False, full_html=False)
