---
heading: Transition Maps are Diffeomorphisms
label: curves_transition_diffeo_pf
---

We already observed that each $\tau_{ij}$ is a bijection and that $\tau_{ii}$ is the identity hence smooth. Thus we need to show that $\tau_{ij}$ is smooth for $i \neq j$. Without loss of generality, let us show that $\tau_{21}$ is smooth (then we get $\tau_{12}$ is smooth by the same argument after swapping $1$ and $2$).

Let $t_0 \in (a_1, b_1)$ be arbitrary. Since $\gamma_1(t) = (x_1^1(t), \dots, x_1^n(t))$ is regular, we must have $(x_1^i)'(t_0) \neq 0$ for at least one index $1 \leq i \leq n$. Then by the inverse function theorem, $x_1^i$ is smoothly invertible on $(t_0-\delta, t_0+\delta)$ for some $\delta > 0$. Thus we may write $t = f_i(x_i)$ with $f_i = (x_1^i)^{-1}$ a smooth function.

Thus if $(x_1, \dots, x_n) = \gamma_1(t) \in \operatorname{Img}(\gamma_1)$ we get

$$
\gamma_1^{-1} (x_1, \dots, x_n) = t = f_i(x_i).
$$

For $u = \tau_{12} (t) = \gamma_2^{-1} \circ \gamma_1(t)$ with $t \in (t_0 -\delta, t_0+\delta)$ we obtain

$$
\tau_{21} (u) = \gamma_1^{-1} \circ \gamma_2 (u) = \gamma_1^{-1} (x_2^1(u), \dots, x_2^n(u)) = f_i \circ x_2^i (u)
$$

That is, $\tau_{21} = f_i \circ x_2^i$ is smooth for $u \in \tau_{12} (t_0-\delta, t_0 + \delta)$. In particular, $\tau_{21}$ is smooth at $u_0 = \tau_{12} (t_0)$, and hence $\tau_{21}$ is smooth for every $u_0 \in (a_2, b_2)$ since every such $u_0$ is of the form $\tau_{12}(t_0)$ and $t_0$ was arbitrary.
