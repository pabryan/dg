import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def arrowhead(x, y, th, **kwargs):
    eps = 10**(-1)
    ax = x - eps*np.cos(th)
    ay = y - eps*np.sin(th)
    return dict(x=x, y=y, ax=ax, ay=ay, text="", showarrow=True, arrowhead=1, arrowsize=2, **kwargs)

th = np.linspace(-np.pi, np.pi, 100)
ph = np.linspace(0.0, np.sqrt(2*np.pi), 100)

unit_circle = pd.DataFrame({'th' : th, 'x': np.cos(th), 'y': np.sin(th)})
unit_circle_alt = pd.DataFrame({'ph' : ph, 'x': np.cos(ph**2), 'y': -np.sin(ph**2)})

colors = px.colors.qualitative.Plotly
fig = make_subplots(rows=2, cols=1, row_heights=[0.8, 0.2])
fig.update_annotations(yshift=20)
fig_alt = make_subplots(rows=2, cols=1, row_heights=[0.8, 0.2])
fig_alt.update_annotations(yshift=20)

#fig.update_xaxes(range=[-1.5, 1.5], row=1, col=1)
fig.update_yaxes(scaleanchor="x1", scaleratio=1, row=1, col=1)
fig.update_xaxes(zeroline=False, showline=False, range=[-(np.pi + 0.5), np.pi + 0.5], tickmode = "array", tickvals=np.linspace(-np.pi, np.pi, 5), ticktext=[r"$-\pi$", ".", ".", ".", r"$\pi$"], row=2, col=1)
fig.update_yaxes(showgrid=False, zeroline=False, showline=False, showticklabels=False, row=2, col=1)

fig_alt.update_yaxes(scaleanchor="x1", scaleratio=1, row=1, col=1)
fig_alt.update_xaxes(zeroline=False, showline=False, range=[-0.5, np.sqrt(2*np.pi) + 0.5], tickmode = "array", tickvals=np.linspace(0.0, np.sqrt(2*np.pi), 5), ticktext=[r"$0$", ".", ".", ".", r"$\sqrt{2\pi}$"], row=2, col=1)
fig_alt.update_yaxes(showgrid=False, zeroline=False, showline=False, showticklabels=False, row=2, col=1)

fig.add_trace(go.Scatter(x=unit_circle["x"], y=unit_circle["y"], name="standard unit circle", showlegend=False, line=dict(color=colors[0])), row=1, col=1)
fig.add_trace(go.Scatter(x=unit_circle["th"], y=np.zeros_like(unit_circle["th"]), showlegend=False, line=dict(color=colors[0])), row=2, col=1)

fig_alt.add_trace(go.Scatter(x=unit_circle_alt["x"], y=unit_circle_alt["y"], name="alternative unit circle", showlegend=False, line=dict(color=colors[1])), row=1, col=1)
fig_alt.add_trace(go.Scatter(x=unit_circle_alt["ph"], y = np.zeros_like(unit_circle_alt["ph"]), showlegend=False, line=dict(color=colors[1])), row=2, col=1)


t0 = 0.0
t1 = np.pi/2+0.5
p0 = np.sqrt(2*np.pi)
p1 = np.sqrt(2*np.pi - np.pi/2-0.5)

x0 = 1.0
y0 = 0.0

x1 = np.cos(t1)
y1 = np.sin(t1)

th1 = t1 + np.pi/2

arcth = np.linspace(t0, t1, 20)
arcph = np.linspace(p0, p1, 20)

fig.add_trace(go.Scatter(x=[x0], y=[y0], mode="markers", showlegend=False, marker=dict(color="black", size=10)), row=1, col=1)
fig.add_trace(go.Scatter(x=np.cos(arcth), y=np.sin(arcth), showlegend=False, line=dict(color="black")), row=1, col=1)
fig.add_annotation(arrowhead(x1, y1, th1, xref="x1", yref="y1", axref="x1", ayref="y1"), row=1, col=1)

fig.add_trace(go.Scatter(x=[0.0], y=[0.0], mode="markers", showlegend=False, marker=dict(color="black", size=10)), row=2, col=1)
fig.add_trace(go.Scatter(x=arcth, y=np.zeros_like(arcth), showlegend=False, line=dict(color="black")), row=2, col=1)
fig.add_annotation(arrowhead(t1, 0, 0, xref="x2", yref="y2", axref="x2", ayref="y2"), row=2, col=1)

fig_alt.add_trace(go.Scatter(x=[x0], y=[y0], mode="markers", showlegend=False, marker=dict(color="black", size=10)), row=1, col=1)
fig_alt.add_trace(go.Scatter(x=np.cos(arcph**2), y=-np.sin(arcph**2), showlegend=False, line=dict(color="black")), row=1, col=1)
fig_alt.add_annotation(arrowhead(x1, y1, th1, xref="x1", yref="y1", axref="x1", ayref="y1"), row=1, col=1)

fig_alt.add_trace(go.Scatter(x=[np.sqrt(2*np.pi)], y=[0.0], mode="markers", showlegend=False, marker=dict(color="black", size=10)), row=2, col=1)
fig_alt.add_trace(go.Scatter(x=arcph, y=np.zeros_like(arcph), showlegend=False, line=dict(color="black")), row=2, col=1)
fig_alt.add_annotation(arrowhead(p1, 0, -np.pi, xref="x2", yref="y2", axref="x2", ayref="y2"), row=2, col=1)
fig_alt.update_yaxes(range=[-1, 1], row=2, col=1)

fig.update_layout(title = {'text': r"$\gamma(t) = (\cos(t), \sin(t)), \quad -\pi < t < \pi$", 'x': 0.5, 'xanchor': 'center'})
fig_alt.update_layout(title = {'text': r"$\gamma(t) = (\cos(t^2), -\sin(t^2)), \quad 0 < t < \sqrt{2\pi}$", 'x': 0.5, 'xanchor': 'center'})

fig.write_image("../../docs/img/unit_circle_example.svg")
fig_alt.write_image("../../docs/img/unit_circle_alt_example.svg")

