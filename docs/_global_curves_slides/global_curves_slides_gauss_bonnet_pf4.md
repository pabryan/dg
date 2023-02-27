---
name: global_curves_slides_gauss_bonnet_pf4
---

$$
\int_C \kappa ds = \int_0^{L} \theta'(s) ds = 2\pi n
$$

We aim to show that $n=\pm 1$

<p class="fragment">
For $(s_1, s_2)$ with $0 \leq s_1 \leq s_2 \leq L$ define

$$
H(s_1, s_2) = \begin{cases}
\gamma'(s_1), & s_1 = s_2 \\ 
\frac{\gamma(s_2) - \gamma(s_1)}{\lvert \gamma(s_2) - \gamma(s_1) \rvert}, & s_1 \neq s_2, (s_1, s_2) \neq (0, L) \\
-\frac{\gamma'(0)}{\gamma'(0)}, & (s_1, s_2) = (0, L)
\end{cases}
$$
</p>

