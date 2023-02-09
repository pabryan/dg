---
heading: Not Regular Curve
label: not_reg_curve
---

The curve
$$
C = \lbrace (x, y) \in \RR^2 : y = |x|) \rbrace
$$
is not regular. A reasonable choice of parametrisation is
$$
\gamma(t) = (t, |t|).
$$
This is not a regular parametrisation since $\gamma$ is not differentiable at $t=0$.

The curve
$$
C = \lbrace (x, y) \in \RR^2 : x^3 = y^2 \in \RR \rbrace
$$
is also not regular. A reasonable choice of parametrisation is
$$
\gamma(t) = (t^2, t^3).
$$
This parametrisation is smooth, but $\gamma'(0) = 0$, hence it is not a regular parametrisation.

In both cases, we've exhibited a non-regular parametrisation. In general, this does not mean no regular parametrisation exists (we already saw a non-regular parametrisation of the unit circle above). So we need some additional argument to show that these curves do not admit regular parametrisations and hence are not regular. We will give that argument below.

{% include img.html file="curves_not_reg_abs.svg" %}

{% include img.html file="curves_not_reg_cusp.svg" %}
