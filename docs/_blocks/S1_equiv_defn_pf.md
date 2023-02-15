---
heading: Equivalence of $\SS^1$ and $\tilde{\SS}^1$
label: S1_equiv_defn_pf
---

To see that $F$ is a diffeomorphism, we need to exhibit a smooth inverse. As we saw above,

$$
\psi_+^{-1} \circ F \circ \varphi_+  = \operatorname{Id}.
$$

This map is defined from $(-\pi/2, 3\pi/2)$ to itself and is it's own inverse, which of course is also smooth. Then for $(x, y) \in \tilde{\SS}^1 \backslash \{(0, -1)\}$ we may define

$$
F^{-1} (x, y) = \varphi_+ \circ \psi_+^{-1} (x, y).
$$

We also define
$$
F^{-1} (0, -1) = [-\pi/2].
$$

Using the definitions we see that

$$
\begin{split}
\psi_+^{-1} \circ F \circ F^{-1} &= \psi_+^{-1} \circ F \circ \varphi_+ \circ \psi_+^{-1} \\
&= \operatorname{Id} \circ \psi_+^{-1} \\
&= \psi_+^{-1}.
\end{split}
$$

Since $\psi_+^{-1}$ is a bijection, $F \circ F^{-1}$ is the identity on $\tilde{\SS}^1 \backslash (0, -1)$. We can directly check that  $F \circ F^{-1} (0, -1) = (0, =1)$. Thus $F \circ F^{-1}$ is the identity on $\tilde{\SS}^1$. Similarly, $F^{-1} \circ F$ is the identity on $\SS^1$ and thus $F^{-1}$ is indeed the inverse of $F$.

To verify smoothness of $F^{-1}$, we use the definitions again:

$$
\begin{split}
\varphi_+^{-1} \circ F^{-1} \circ \psi_+ (t) &= \varphi_+^{-1} \circ \varphi_+ \circ \psi_+^{-1} \circ \psi_+(t) \\
&= t
\end{split}
$$

which is smooth. To check smoothness of $F^{-1}$ near $(0, -1)$ we can argue similarly, but this time using $\varphi_-^{-1} \circ F^{-1} \circ \psi_-$.

FInally, we should also verify that $\psi_+^{-1} \circ F \circ \varphi_-$ and $\psi_-^{-1} \circ F \circ \varphi_+$ are smooth. This is similar to our arguments so far and is left to the reader.
