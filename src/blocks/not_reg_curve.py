#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

t = np.linspace(-1, 1, 51)

absval = pd.DataFrame({"x" : t, "y" : np.abs(t)})
pow23 = pd.DataFrame({"x" : t**2, "y" : t**3})

absfig = go.Figure()
absfig.update_layout(title = r"$\gamma(t) = (t, |t|) \quad -1 < t < 1$")
absfig.update_annotations(yshift=20)
absfig.update_yaxes(scaleanchor="x")

absfig.add_trace(go.Scatter(x=absval["x"], y=absval["y"], showlegend=False))

powfig = go.Figure()
powfig.update_layout(title = r"$\gamma(t) = (t^2, t^3) \quad -1 < t < 1$")
powfig.update_annotations(yshift=20)
powfig.update_yaxes(scaleanchor="x")
powfig.add_trace(go.Scatter(x=pow23["x"], y=pow23["y"], showlegend=False))

absfig.write_image("../../docs/img/curves_not_reg_abs.svg")
powfig.write_image("../../docs/img/curves_not_reg_cusp.svg")
