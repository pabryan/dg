---
heading: Arc Length Parameter
label: arc_length_param
---

Let $\gamma : (a, b) \to \RR^n$ be a regular curve and let $t_0 \in (a, b)$. We define the arc-length parameter $s_{t_0}$ based at $t_0$ and oriented in the direction of $\gamma$ by

$$
s(t) = \int_{t_0}^t v(u) du = \int_{t_0}^t \lvert \gamma'(u) \rvert du.
$$

We define the _intrinsic distance_ between any points $p_1 = \gamma(t_1)$ and $p_2 = \gamma(t_2)$ to be

$$
\ell(p_1, p_2) = \lvert s_{t_0}(t_2) - s_{t_0}(t_1) \rvert.
$$
