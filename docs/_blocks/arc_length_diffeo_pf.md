---
heading: Arc Length Parameter is a Diffeomorphism
label: arc_length_diffeo_pf
---

We have

$$
s(t) = \int_{t_0}^t \lvert \gamma'(u) \rvert du
$$

and hence by the Fundamental Theorem of Calculus,

$$
s'(t) = \lvert \gamma'(t) \rvert > 0.
$$

Thus $s$ is strictly increasing and hence injective. Since $t \mapsto s(t)$ is continuous, by the intermediate value theorem, for any $t_1, t_2$ $s(t)$ attains all values on $[s(t_1), s(t_2)]$ hence the image of $s$ is an interval. Moreover, from $s' > 0$ the inverse function theorem implies $s$ is smoothly invertible hence a diffeomorphism.
