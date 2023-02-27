---
name: global_curves_slides_isoperimetric_inequality_pf3
---

Write $X = (x, y)$ so $\operatorname{div} X = 2$.

<p class="fragment">
$$
\begin{split}
2 A &= \int_{\Omega} \operatorname{div} X dA = \int_C \langle X, N \rangle ds \\
&\leq \int_C \lvert X \rvert ds \leq \big(\int_C \lvert X \rvert^2 ds \big)^{1/2} \big(\int_C 1^2 ds \big)^{1/2}
\end{split}
$$
</p>

<p class="fragment">
$$
\begin{split}
2A &\leq \sqrt{2\pi} \big(\int_0^{2\pi} x^2 + y^2 ds\big) \\
&\leq \sqrt{2\pi} \big(\int_0^{2\pi} (x')^2 + (y')^2 ds \big)^{1/2} \\
&= 2\pi = \frac{L^2}{2\pi}
\end{split}
$$
</p>
