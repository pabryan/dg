---
heading: Standard Embedding of $\SS^1$
label: S1_standard_embedding
---

Denote the unit circle in the plane by

$$
\tilde{\SS}^1 = \lbrace x^2 + y^2 = 1 \rbrace.
$$

Define maps $(0, 2\pi) \to \tilde{\SS}^1$ by

$$
\begin{split}
\psi_{\pm} (t) &= (\cos(t \mp \pi/2), \sin(t \mp \pi/2)) \\
&= \pm (\sin(t), -\cos(t)).
\end{split}
$$

A function $f: \tilde{\SS}^1 \to \RR^n$ is smooth provided $f \circ \psi_{\pm}$ are smooth.

A function $f : \RR^n \to \tilde{\SS}^1$ is smooth provided $\psi_{\pm}^{-1} \circ f$ are smooth.