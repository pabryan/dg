---
heading: Equivalence of Quotient and Manifold Definitions
label: S1_quotient_manifold_equiv_pf
---

Suppose that $f \circ q$ is smooth. Then

$$
f \circ \varphi_{\pm}(t) = f \circ q (t \mp \pi/2)
$$

is smooth.

Conversely, suppose that $f \circ \varphi_{\pm}$ are smooth. Then for $x \in (-\pi/2, 3\pi/2)$,

$$
f \circ q(x) = f \circ \varphi_+(x + \pi/2)
$$

is smooth. Similarly, for $x \in (\pi/2, 5\pi/2)$,

$$
f \circ q(x) = f \circ \varphi_-(x - \pi/2)
$$

is smooth.

Thus $f \circ q$ is smooth on $(-\pi/2, 5\pi/2)$, an open interval of length greater than $2\pi$. The result now follows from $2\pi$-periodicity of $f\circ q$:

For any $x_0$, there exists a $y_0 \in (-\pi/2, 5\pi/2)$ such that $x_0 - y_0 \in 2\pi \ZZ$. Moreover, this is true in a neighbourhood of $x_0$: there is a $\delta > 0$ (just take any $\delta < \pi$) such that for every $x \in (x_0-\delta, x_0+\delta)$, there is a unique $y \in (y_0 - \delta, y_0 + \delta)$ with $x - y \in 2\pi\ZZ$. Since $f \circ q$ is $2\pi$-periodic, $f\circ q(x) = f\circ(y)$; thus $f \circ q$ in a neighbourhood of $x_0$ equals $f\circ q$ in a neighbourhood of $y_0$. Since the latter is smooth, so is the former.
