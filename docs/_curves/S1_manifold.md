---
title: $\SS^1$ as a Manifold
name: S1_manifold
type: topic
---

We have defined smooth maps $\SS^1 \to \RR^n$ as smooth, periodic functions $\RR \to \RR^n$; that is as functions $f$ such that $f \circ q$ is smooth. But what about maps to $\SS^1$? Analogously, we might define a map $f : \RR^n \to \SS^1$ as being smooth provided there exists a smooth map $\bar{f} : \RR^n \to \RR$ such that $f = q \circ \bar{f}$. This poses some difficulties, since unlike the case of maps $\SS^1 \to \RR$ where we start with a given $f$ and just have to check if $f \circ q$ is smooth, now given a map $f$ to show it is smooth we must produce a smooth map $\bar{f}$ such that $f = q \circ \bar{f}$, and to show $f$ is not smooth we must somehow prove no such $\bar{f}$ exists.

In this section we will take a different approach. Fortunately we will generalise this approach later to define manifolds, so our efforts now will be a good warm up for then.

{% include defn.html label="S1_manifold_defn" %}

Note that $\varphi_{\pm}(t) = q(t \mp \pi/2)$; that is the plus and minus are swapped. The reason for this choice is that if we think of $\SS^1$ as the unit cirlce in the plane and $\theta$ as the angle counter-clockwise from the $x$-axis, then the image of $\varphi_+$ is the upper part of the circle, omitting only the point $(0, -1)$, while the image of $\varphi_-$ is the lower part of the circle, omitting only $(0, 1)$. These maps are known as _stereographic coordinates_, which we will meet later in greater generality and detail.

{% include lem.html label="S1_quotient_manifold_equiv" %}

{% include pf.html label="S1_quotient_manifold_equiv_pf" %}
