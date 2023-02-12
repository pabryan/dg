---
title: Change of Parameters
name: change_of_params
type: topic
---

We are mostly interested in the properties of a curve $C$ as a set in $\RR^n$. A regular curve is a set and a parametrisation is way of traversing that set. We will generally define properties of $C$ via parametrisations.  We should then figure out what properties of parametrisations depend on the choice and which properties that do not. The latter will then be intrinsic properties of a curve. For example, whether a parametrisation is regular or not is a property of the particular parametrisation, but whether or not a curve is regular (i.e. admits a regular parametrisation) is a property of the curve and not the parametrisation. Make sure you understand this!

In order to study a curve via it's parametrisations, we will begin by investigating what happens when we change parametrisations.

{% include defn.html label="curves_change_of_params" %}

By the chain rule, if $\gamma$ is a regular parametrisation, and $\varphi$ is a change of parameters, then $\gamma \circ \varphi$ is a regular parametrisation.

{% include eg.html label="change_of_params_log_spiral" %}

{% include ex.html label="interval_diffeo" %}

{% include ex.html label="mobius_S1" %}
