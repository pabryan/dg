---
heading: Tangent Line
label: tangent_line
---

Let $\gamma$ be an injective, regular, parametrised curve. The _velocity vector_ is the vector $\gamma'(t)$. The _speed_ is the magnitude of the velocity vector, $v(t) = \lvert \gamma'(t) \rvert$. The (oriented) _unit tangent vector_ is the vector

$$
T(t) = \frac{\gamma'(t)}{\lvert \gamma'(t) \rvert} = \frac{\gamma'(t)}{v(t)}.
$$

For each $t_0$, the tangent line at $\gamma(t_0)$ is the line, $TL$ passing through the point $\gamma(t_0)$ in the direction $\gamma'(t_0)$. Some common ways to parametrise the tangent line are

$$
\begin{split}
TL_{t_0} (u) &= \gamma(t_0) + u \gamma'(t_0) \\
TL_{t_0} (v) &= \gamma(t_0) + v T(t_0) \\
TL_{t_0} (t) &= \gamma(t_0) + (t-t_0) \gamma'(t_0) \\
\end{split}
$$
