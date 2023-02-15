---
title: Tangent and Normal Space
name: tangent_and_normal
type: topic
---

{% include defn.html label="tangent_line" %}

- The regularity condition ensures $\gamma'(t_0) \neq 0$ hence the unit tangent is well defined, and the tangent line is indeed a line (as opposed to a single point which occurs precisely when $\gamma'(t_0) = 0$).
- Below we show that the tangent line is independent of the parametrisation, hence $T$ is defined up to sign independently of the parametrisation. A consistent choice of sign is an _orientation_.
- Let us note that $\gamma' = v T$, a simple relation we will make use of later.
- The first parametrisation is a constant speed parametrisation of $TL$ with speed $\lvert TL'(u) \rvert = \lvert \gamma'(t_0) \rvert$.
- The second parametrisation is a constant, unit speed parametrisation.
- The third parametrisation shows the tangent line is the first order Taylor polynomial for $\gamma$ at $t_0$.

{% include lem.html label="tangent_line_independent_param" %}

{% include pf.html label="tangent_line_independent_param_pf" %}

Notice, as remarked earlier, that if $\gamma_1, \gamma_t$ are two parametrisations with respective unit tangents $T_1, T_2$, then $T_2 = \pm T_1$.

{% include defn.html label="normal_space" %}

In the particular case of the plane ($n=2$), we can choose a preferred normal vector in several ways:

1. Let $N(p) = R_{\pi/2} (T(p))$ where $R_{\pi/2}$ is counter clockwise rotation by $\pi/2$. We then say by convention that $\lbrace T, N \rbrace$ is positively oriented. Explicitly if $T(p) = (T_1(p), T_2(p))$, then

   $$
   \begin{split}
   N(p) &= \begin{pmatrix}
   0 & -1 \\
   1 & 0
   \end{pmatrix}
   \begin{pmatrix}
   T_1(p) \\
   T_2(p)
   \end{pmatrix}
   \\ 
   & = \begin{pmatrix}
   -T_2(p) \\
   T_1(p)
   \end{pmatrix}.
   \end{split}
   $$

   In particular, with $T = \tfrac{\gamma'}{v} = \tfrac{1}{v} (x', y')$,
   
   $$
   N = \frac{1}{v} (-y', x').
   $$

2. We could take $N = R_{-\pi/2} (T) = -R_{\pi/2}(T)$. We then say that $\lbrace T, N \rbrace$ is negatively oriented. Note that then $\lbrace N, T \rbrace$ is positively oriented.

3. For simple, closed curves that are the boundary of a region $\Omega$ (Jordan's curve theorem actually implies all simple closed curves are boundaries), then we could choose $N$ to point inwards or outwards. Whether or not $\lbrace T, N \rbrace$ is positively oriented then depends on how $T$ was chosen. By reversing the direction of parametrisation, we may ensure positive orientation.

{% include eg.html label="tangent_normal_space_S1" %}

{% include ex.html label="tangent_normal_space_graphs" %}
