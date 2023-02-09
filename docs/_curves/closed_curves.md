---
title: Closed Curves
name: closed_curves
type: topic
---

There is one situation where we want to think of non-injective parametrisations as injective. These are _closed curves_, which are naturally parametrised over $\SS^1$ rather than $(a, b)$.

{% include defn.html label="closed_curve" %}

The unit circle above is a particular example of a simple, closed curve.

{% include eg.html label="curves-simple-closed" %}

{% include eg.html label="lemniscate-bernoulli" %}

A closed curve joins up smoothly at the end points, and a simple, closed curve only crosses itself where the end-points join up. We can make a cleaner definition by parametrising over $\SS^1$ instead of over $[a, b]$ with a condition at the end points.

{% include defn.html label="S1" %}

We could think of $\SS^1$ as $[0, 2\pi]$ with the endpoint identified, or indeed as $[x, x + 2\pi]$ with endpoints identified, where $x \in \RR$ is arbitrary. For now at least, we want to think in terms of equivalance classes $[x]$. In particular $[x] = [x + 2\pi n]$ for any $n \in \ZZ$.- This is simlar to thinking of rational numbers as pairs of integers $(n, d)$ with $d \neq 0$ and where we identify $(n_1, d_1)$ with $(n_2, d_2)$ provided $n_1 d_2 = n_2 d_1$; this is essentially rearranging the equality $n_1/d_1 = n_2/d_2$.

{% include ex.html label="periodic-functions-correspondence" %}

{% include defn.html label="smooth-periodic" %}

{% include ex.html label="smooth-periodic-well-defined" %}

Now we may give a definition of regular, closed curves in terms of functions parametrised over $\SS^1$ rather than $(a,b)$.

{% include defn.html label="closed_curve_S1" %}

{% include ex.html label="smooth-periodic-defn-correspondence" %}

We have defined smooth maps $\SS^1 \to \RR^n$ as periodic functions $\RR \to \RR^n$. But what about maps to $\SS^1$? This is a little more indirect, but uses similar ides.

{% include defn.html label="smooth-to-S1" %}

The idea is that given a map $f : \RR^n \to \SS^1$, we can define a map $\bar{f} : \RR^n \to [0, 2\pi)$ where $\bar{f}(V)$ is the unique element in $[0, 2\pi)$ such that $f(V) = [\bar{f}(V)]$. By construction,

$$
f(V) = [\bar{f}(V)] = q \circ \bar{f} (V).
$$

Then we will say that $f$ is smooth precisely when $\bar{f}$ is smooth. Note that we could instead choose say $\bar{f}(V)$ to be the unique element in $[x_0, x_0 + 2\pi)$ for any $x_0 \in \RR$ and we get an equivalent definition. There is nothing special about $[0, 2\pi)$ except that by convention we often choose that interval.
