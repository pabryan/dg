---
Heading: Total Length is Well Defined
label: arc_length_len_pf
----

We have

$$
\begin{split}
L &= \int_a^b \lvert \gamma'(t) \rvert dt &= \lim_{t_1\to a} \lim_{t_2 \to b} \int_{t_1}^{t_2} \lvert \gamma'(t) \rvert dt
&= \lim_{t_1\to a} \lim_{t_2 \to b} \ell(t_1, t_2).
\end{split}
$$

The result follows since $\ell(t_1, t_2)$ depends only on $p_i = \gamma(t_i)$. $i = 1,2$.
