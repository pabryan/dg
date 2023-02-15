---
title: Arc Length
name: arclength
type: topic
---

As mentioned before, we tend to define properties of curves via parametrisations. Then to show a property is intrinsic to the curve we need to show that the property  is independent of the chosen parametrisation. For curves, there is another approach; namely we introduce an (almost) canonical parametrisation and then use that for our definitions.

{% include defn.html label="arc_length_param" %}

Notice that since our curves are smooth, the speed is continuous and hence for any $t_0 \in (a, b)$ and any $t \in (a, b)$, $v$ is continuous on $[t_0, t]$ (or $[t, t_0]$ if $t < t_0$) hence bounded, hence the integral is finite and $s(t)$ is well defined.

The arc length parameter, $s_{t_0}(t)$ measures the oriented, intrinsic distance along the curve from $p_0 = \gamma(t_0)$ to $p = \gamma(t)$. Here by oriented, we note that $s(t)$ is negative for $t < t_0$ which we interpret as moving backwards a distance $\lvert s(t) \rvert$ along the curve from $p_0$.

{% include lem.html label="arc_length_intrinsic_well_defined" %}

{% include pf.html label="arc_length_intrinsic_well_defined_pf" %}

{% include defn.html label="arc_length" %}

{% include lem.html label="arc_length_len" %}

{% include pf.html label="arc_length_len_pf" %}

The previous lemmas tell us that it doesn't matter which parametrisation we choose, nor which basepoint we choose. Thus we will simply write $s(t)$ for the arc length parameter without explicitly referring to the parametrisation or basepoint. It also means we can define the total length of the curve.

{% include lem.html label="arc_length_diffeo" %}

{% include pf.html label="arc_length_diffeo_pf" %}

We can use the arc length parameter to parametrise the curve.

{% include defn.html label="arc_length_parametrisation" %}

Thus the arc length parametrisation is defined on an interval of the form $(-c, -c + L)$. Provided $c \neq \infty$, we can change parametrisations $s \mapsto s - c$ giving a new parametrisation $s \mapsto \tilde{\gamma}(s - c)$ defined for $s \in (0, L)$.

{% include ex.html label="arc_length_unit_speed" %}

Thus we may also define arc length parametrisations to be unit speed parametrisations. The arc length parametrisation is unique up to choosing the base point $p \in C$ and the direction; i.e. the choice of unit tangent at $p$.

{% include ex.html label="arc_length_unique" %}
