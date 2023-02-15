---
title: $\SS^1$ as a Manifold
name: S1_manifold
type: topic
---

We have defined smooth maps $\SS^1 \to \RR^n$ as smooth, periodic functions $\RR \to \RR^n$; that is as functions $f$ such that $f \circ q$ is smooth. But what about maps to $\SS^1$? Analogously, we might define a map $f : \RR^n \to \SS^1$ as being smooth provided there exists a smooth map $\bar{f} : \RR^n \to \RR$ such that $f = q \circ \bar{f}$. This poses some difficulties, since unlike the case of maps $\SS^1 \to \RR$ where we start with a given $f$ and just have to check if $f \circ q$ is smooth, now given a map $f$ to show it is smooth we must produce a smooth map $\bar{f}$ such that $f = q \circ \bar{f}$, and to show $f$ is not smooth we must somehow prove no such $\bar{f}$ exists.

In this section we will take a different approach. Fortunately we will generalise this approach later to define manifolds, so our efforts now will be a good warm up for then.

{% include defn.html label="S1_manifold_defn" %}

Note that $\varphi_{\pm}(t) = q(t \mp \pi/2)$; that is the plus and minus are swapped. The reason for this choice is that if we think of $\SS^1$ as the unit cirlce in the plane and $\theta$ as the angle counter-clockwise from the $x$-axis, then the image of $\varphi_+$ is the upper part of the circle, omitting only the point $(0, -1)$, while the image of $\varphi_-$ is the lower part of the circle, omitting only $(0, 1)$. These maps are similar to _stereographic coordinates_, which we will meet later in greater generality and detail.

{% include lem.html label="S1_quotient_manifold_equiv" %}

{% include pf.html label="S1_quotient_manifold_equiv_pf" %}

It will be convenient later to sometimes think of $\SS^1$ as the quotient $\RR/L\ZZ$ for any $L \in \RR$, $L > 0$. The idea being that a closed curve of length $L$ is more naturally parametrised over $\RR/L\ZZ$ rather than over $\RR/2\pi \ZZ$.

{% include ex.html label="S1_L" %}

The exercise means that from the point of view of differentiability, we may think of $\SS^1$ as $\RR/2\pi \ZZ$ or $\RR/L \ZZ$ equivalently. We also often think of $\SS^1$ as the set $\lbrace x^2 + y^2 = 1 \rbrace$. We will call this perspective the _standard embedding_ of $\SS^1$ in $\RR^2$. The standard embedding is also equivalent (i.e. diffeomorphic) to $\RR/2\pi \ZZ$.

{% include defn.html label="S1_standard_embedding" %}

Notice that $\psi_{\pm}$ are smooth, injective, regular parametrisations (i.e. $\psi_{\pm}' \neq 0$). They are analogous to $\varphi_{\pm}$ defined for $\SS^1$.

Consider the map $\bar{F} : \RR \to \tilde{\SS}^1$ defined by $x \mapsto (\cos(x), \sin(x))$. This is a smooth, periodic map, hence induces a smooth map $F : \SS^1 \to \tilde{\SS}^1$ defined by $F \circ q = \bar{F}$. Here to say that $F$ is smooth is to say that all of the four maps,

$$
F_{\pm,\pm} := \psi_{\pm}^{-1} \circ F \circ \varphi_{\pm}
$$

are smooth wherever defined. For example

$$
\begin{split}
F_{+,+} &= \psi_+^{-1}\left(\cos(q(t-\pi/2)), \sin(q(t-\pi/2))\right) \\
&= \psi_+^{-1} (\sin(t), -\cos(t)) \\
&= t
\end{split}
$$

since $\psi_+(t) = (\sin(t), -\cos(t))$. Thus $F_{+,+} = \psi_+^{-1} \circ F \circ \varphi_+ (t) = t$ is clearly smooth.

In fact, $F$ is a diffeomorphism, hence we may identify $\SS^1$ with $\tilde{\SS}^1$ when considering questions relating to differentiability and continuity.

{% include thm.html label="S1_equiv_defn" %}

{% include pf.html label="S1_equiv_defn_pf" %}

Another way to prove the theorem is to define the function $\operatorname{atan2}: \tilde{\SS}^1 \to \RR$ by

$$
\begin{cases}
\arctan(y/x), & x > 0 \\
\arctan(y/x) + \pi, & x < 0, y \geq 0 \\
\arctan(y/x) - \pi, & x < 0, y < 0 \\
\pm \pi/2, & (x, y) = (0, \pm 1)
\end{cases}
$$

Then $F^{-1} = q \circ \operatorname{atan2}$. It's an exercise in basic trigonometry, keeping track of quadrants to show that $F^{-1}$ is indeed the inverse of $F$. It's an interesting exercise to show that $F^{-1}$ is in fact smooth; that is that $\varphi_{\pm}^{-1} \circ F^{-1} \circ \psi_{\pm}$ is smooth. This latter boils down to writing out the definitions of the various maps involved similarly to how we did it above.

Either way, $\SS^1$ and $\tilde{\SS}^1$ are diffeomorphic. From now on we will freely use $\SS^1$ to refer to both $\RR/2\pi \ZZ$ and to $\lbrace x^2 + y^2 = 1\rbrace$.
