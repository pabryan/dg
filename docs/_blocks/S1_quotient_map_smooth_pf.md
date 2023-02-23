---
heading: Quotient Map is Smooth
label: S1_quotient_map_smooth_pf
---

We need to verify that $\varphi_{\pm}^{-1} \circ q : \RR \to (0, 2\pi) \subseteq \RR$ is smooth. We will just verify that $\varphi_+^{-1} \circ q$ is smooth, the case of $\varphi_-^{-1} \circ q$ being similar.

Note that $\varphi_+^{-1} \circ q$ is defined precisely for $x \in \RR$ such that $\varphi_+^{-1}$ is defined at $q(x)$. Since $\varphi_+$ maps $(0, 2\pi)$ to $\lbrace [x] : x \in (-\pi/2, 3\pi/2) \rbrace$, we have that $\varphi_+^{-1} \circ q$ is defined for $x = y + 2\pi n$ where $y \in (-\pi/2, 3\pi/2)$ and $n \in \ZZ$. That is for

$$
x \in \bigcup_{n \in \ZZ} (-\pi/2 + 2\pi n, 3\pi/2 + 2\pi n)
$$

So we take any $n \in \ZZ$ and let $x \in (-\pi/2 + 2\pi n, 3\pi/2 + 2\pi n)$ and let $y = x - 2\pi/n \in (-\pi/2, 3\pi/2)$. Then

$$
\varphi_+ (y) = q(y - \pi/2) = q(x - \pi/2)
$$

and hence

$$
\begin{split}
x - 2\pi n &= y = \varphi_+^{-1} \circ \varphi_+ (y) \\
&= \varphi_+^{-1} \circ q (x - \pi/2).
\end{split}
$$

Replacing $x$ by $x + \pi/2$ then gives

$$
\begin{split}
\varphi_+^{-1} \circ q(x) = \varphi_+^{-1} \circ q(x +\pi/2 - \pi/2) \\
&= x +\pi/2 - 2\pi n.
\end{split}
$$

which is smooth.
