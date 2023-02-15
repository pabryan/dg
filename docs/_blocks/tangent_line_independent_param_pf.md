---
heading: Tangent Line is Independent of Parametrisation
label: tangent_line_independent_param_pf
---

Let $\gamma_1, \gamma_2$ be two different parametrisations an let $t_1, t_2$ be such that $p = \gamma_1(t_1) = \gamma_2(t_2)$. The tangent lines $TL_{t_1}$ and $TL_{t_2}$ both pass through the point $p$. Thus we just need to show that the direction vectors $\gamma_1'(t_1)$ and $\gamma_2'(t_2)$ are proportional.

Let $\tau_{21}$ denote the transition map so that $\gamma_2 = \gamma_1 \circ \tau_{21}$ and $t_1 = \tau_{21} (t_2)$. By the chain rule

$$
\begin{split}
\gamma_2'(t_2) &= \tau_{21}'(t_2) \gamma_1'(\tau_{21}(t_2)) \\
&= \tau_{21}'(t_2) \gamma_1'(t_1).
\end{split}
$$

Thus $\gamma_2'(t_2)$ is proportional to $\gamma_1'(t_1)$ as required.
