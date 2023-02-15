---
heading: Intrinsic Distance is Well Defined
label: arc_length_intrinsic_well_defined_pf
---

Let $\gamma : (a, b) \to \RR^n$ and $\sigma : (c, d) \to \RR^n$ be any two injective parametrisations and let $t_0 \in (a, b)$ and $u_0 \in (c, d)$ any choice of basepoints. Note we allow here that $\gamma = \sigma$ and $t_0, u_0 \in (a, b)$ any choices of basepoints.

Let $t_1, t_2 \in (a, b)$ and $u_1, u_2 \in (c, d)$ be such that $\gamma(t_i) = p_i = \sigma(u_i)$, $i = 1,2$.  Let us write

$$
\begin{split}
\ell_{\gamma,t_0} (t_1, t_2) &= \left \lvert \int_{t_0}^{t_2} v dt - \int_{t_0}^{t_1} v dt \right \rvert \\
\ell_{\sigma,u_0} (t_u, u_2) &= \left \lvert \int_{u_0}^{u_2} v du - \int_{u_0}^{u_1} v du \right \rvert \\
\end{split}
$$

Recall that $v = \lvert \gamma' \rvert$ in the $\gamma$ parametrisation and $v = \lvert \sigma' \rvert$ in the $\sigma$ parametrisation. Now we have

$$
\begin{split}
\pm \ell_{\gamma,t_0} &= \int_{t_0}^{t_2} v dt - \int_{t_0}^{t_1} v dt \\
&= \int_{t_0}^{t_1} v dt + \int_{t_1}^{t_2} v dt - \int_{t_0}^{t_1} v dt \\
&= \int_{t_1}^{t_2} v dt.
\end{split}
$$

with plus when $t_2 > t_1$ and minus when $t_2 < t_1$ since $v > 0$. Thus

$$
\ell_{\gamma,t_0} (t_1, t_2) = \left\lvert \int_{t_1}^{t_2} \lvert \gamma'(t) \rvert dt \right \rvert
$$

does not depend on the choice of $t_0$. Similarly, the analogous formula holds for $\ell_{\sigma,u_0}(u_1, u_2)$ which does not depend on the choice of $u_0$.

To finish we need to show that $\ell_{\gamma,t_0}(t_1, t_2) = \ell_{\sigma,u_0} (u_1, u_2)$. The change of parameters $\tau = \gamma^{-1} \circ \sigma$ is a diffeomorphism $(a, b) \to (c, d)$ giving $\sigma = \gamma \circ \tau$ and $\gamma = \sigma \circ \tau^{-1}$. Since $\gamma(t_i) = \sigma(u_i)$, $i=1,2$ we have that $\tau(u_i) = t_i$. Substituting $t = \tau(u)$ gives $dt = \tau' du$ and hence

$$
\begin{split}
\int_{u_1}^{u_2} \lvert \sigma'(u) \rvert du &= \int_{u_1}^{u_2} \lvert \sigma'(\tau^{-1}(\tau(u))) \rvert du \\
&= \int_{t_1}^{t_2} \lvert \sigma' (\tau^{-1}(t)) \rvert \frac{1}{\tau'(\tau^{-1}(t))} dt \\
&= \int_{t_1}^{t_2} \lvert (\sigma \circ \tau^{-1})' (t) \frac{1}{(\tau^{-1})'(t)} \rvert (\tau^{-1})' (t) dt \\
&= \pm \int_{t_1}^{t_2} \lvert \gamma'(t) \rvert.
\end{split}
$$

Taking absolute values gives the result.
 
