---
title: Parametrised Curves
name: curves-parametrised
num: 01
type: topic
---

{% include defn.html label="reg_param_curve" %}

- Regularity is **very** important. It allows us to transfer calculus on $(a, b)$ to calculus on $\operatorname{Img} (\gamma) := \lbrace\gamma(t) : t \in (a, b)\rbrace \subseteq \RR^n$.
- _Plane curves_ are the case $n=2$.
- _Space curves_ are the case $n=3$.

{% include eg.html label="curves_unit_circle" %}

{% include curves_unit_circle_plot.html %}

One thing to take away from this example, is that there are many ways to parametrise a curve. That is, defining

$$
\operatorname{Img}(\gamma) := \{\gamma(t) : a \leq t \leq b\}
$$

we have $\operatorname{Img}(\gamma_1) = \operatorname{Img}(\gamma_2)$ but $\gamma_1 \ne \gamma_2$. The paremetrisation $\gamma_1$ is regular, but $\gamma_2'(0) = 0$, hence $\gamma_2$ is not regular.

There is thus a distiction between the parametrisation, $\gamma$ and the image, $\operatorname{Img}(\gamma)$.

{% include defn.html label="reg_curve" %}

In other words, $C$ is a regular curve if there is at least one regular parametrisation of it. There will always be parametrisations that are not regular; for example, if $\gamma$ is any parametrisation (regular or not), $\sigma(s) = \gamma(a + (1/2)(s^3 + 1)(b-a))$ for $s \in (-1, 1)$ is not regular since by the chain rule, $\sigma'(0) = 0$.

It can be helpful to think of examples of sets $C$ that are not regular curves. To begin with, $C$ needs to be the image of a smooth map $(a, b) \to \RR^n$. But among such sets, there are examples of smooth, parametrised curves that are not regular.

{% include eg.html label="not_reg_curve" %}

{% include not_reg_curve_plot.html %}

<!-- #+BEGIN_eg -->
<!-- $$ -->
<!-- \gamma(t) = (t, |t|), t \in \RR. -->
<!-- $$ -->
<!-- This time $\gamma$ is not differentiable at $t=0$ so is not even a smooth parametrised curve. -->
<!-- #+END_eg -->

<!-- *** Examples of Curves -->

<!-- #+BEGIN_eg -->
<!-- $$ -->
<!-- \gamma(t) = (t^3, t^2), \quad t \in \RR. -->
<!-- $$ -->
<!-- We have $\Img(\gamma) = \lbracey = x^{2/3}\rbrace$ has a /cusp/ at $t=0$. This time, there is no regular parametrisation of $\Img(\gamma)$! /See the implicit function theorem/. -->
<!-- #+END_eg -->
<!-- \pause -->

<!-- #+BEGIN_eg -->
<!-- $$ -->
<!-- \gamma(t) = (t^3 - 4 t, t^2 - 4). -->
<!-- $$ -->
<!-- Here $\gamma$ is regular, but it is not one-to-one. That is, it crosses itself. -->
<!-- #+END_eg -->
<!-- \pause -->

<!-- #+BEGIN_eg -->
<!-- $$ -->
<!-- \gamma(t) = (\cos(t), \sin(t)). -->
<!-- $$ -->
<!-- Here $\gamma$ is one-to-one on $(0, 2\pi)$ but not on any larger interval. However, $\gamma^{(k)}(0) = \gamma^{(k)}(2\pi)$ so that $\gamma$ smoothly /closes up/ to give a closed curve. Any smooth periodic function satisfies this property. -->
<!-- #+END_eg -->


