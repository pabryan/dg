---
heading: Transition Maps are Diffeomorphisms
label: curves_transition_diffeo_pf
---

We already observed that each $\tau_{ij}$ is a bijection and that $\tau_{ii}$ is the identity hence smooth. Thus we need to show that $\tau_{ij}$ is smooth for $i \neq j$. Without loss of generality, let us show that $\tau_{21}$ is smooth (then we get $\tau_{12}$ is smooth by the same argument after swapping $1$ and $2$).

Let $t_0 \in (a_1, b_1)$ be arbitrary. Since $\gamma_1(t) = (x_1(t), y_1(t))$ is regular, we must have either $x_1'(t_0) \neq 0$ or $y_1'(t_0) \neq 0$. Without loss of generality, assume $x_1'(t_0) \neq 0$. Then by the inverse function theorem, $x_1$ is smoothly invertible on $(t_0-\delta, t_0+\delta)$ for some $\delta > 0$. Thus we may write $t = x_1^{-1}(x)$ and

$$
\gamma_1(t) = (x_1(t), y_1(t)) = (x_1(x_1^{-1}(x)), y_1(x_1^{-1}(x))) = (x, y_1 \circ x_1^{-1}(x))
$$

Let $\pi : (x, y) \mapsto x$ be projection onto the first factor. Then $\pi \circ \gamma_1 (t) = x$ and hence

$$
t = x_1^{-1}(x) = x_1^{-1} \circ \pi \circ \gamma_1 (t) \quad \Longrightarrow \quad \gamma_1^{-1} (x, y) = x_1^{-1} \circ \pi (x, y) = x_1^{-1} (x).
$$

Thus, letting $u = \tau_{12} (t) = \gamma_2^{-1} \circ \gamma_1(t)$ we obtain

$$
\tau_{21} (u) = \gamma_1^{-1} \circ \gamma_2 (u) = \gamma_1^{-1} (x_2(u), y_2(u)) = x_1^{-1} \circ x_2 (u)
$$

which is smooth for $u \in \tau_{12} (t_0-\delta, t_0 + \delta)$. In particular, $\tau_{21}$ is smooth at $u_0 = \tau_{12} (t_0)$, and hence $\tau_{21}$ is smooth for every $u_0 \in (a_2, b_2)$ since every such $u_0$ is of the form $\tau_{12}(t_0)$ and $t_0$ was arbitrary.
