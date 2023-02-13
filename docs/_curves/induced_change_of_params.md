---
title: Induced Change of Parameters
name: induced_change_of_params
type: topic
---

Given a regular, parametrised curve $\gamma : (a, b) \to \RR^n$ and a diffeomorphism $\varphi : (c, d) \to (a, b)$, we obtain a new parametrisation $\gamma \circ \varphi : (c, d) \to \RR^n$. Now suppose we are given two parametrisations $\gamma_1 : (a_1, b_1) \to \RR^n$ and $\gamma_2 : (a_2, b_2) \to \RR^n$ with $\operatorname{Img}(\gamma_1) = \operatorname{Img}(\gamma_2)$. The next question we address is whether there exists a diffeomorphism $\tau_{21} : (a_2, b_2) \to (a_1, b_1)$ such that $\gamma_2 = \gamma_1 \circ \tau_{21}$. We will prove this in the case of simple curves (recall they don't cross themselves) where both $\gamma_1, \gamma_2$ are regular, injective parametrisations.

{% include defn.html label="curves_transition" %} 

{% include thm.html label="curves_transition_diffeo" %}

{% include pf.html label="curves_transition_diffeo_pf" %}

{% include ex.html label="curves_regular_locally_graphical" %}

