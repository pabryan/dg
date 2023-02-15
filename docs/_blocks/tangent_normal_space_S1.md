---
heading: Tangent and Normal Space to $\SS^1$
label: tangent_normal_space_S1
---

Let $C = \lbrace x^2 + y^2 = 1 \rbrace$ denote the unit circle in the plane. A counter-clockwise parametrisation of $C$ is

$$
\gamma(t) = (\cos t, \sin t)
$$

Then

$$
T = \gamma' = (-\sin t, \cos t)
$$

and the positively oriented unit normal is

$$
N(t) = (-\cos t, - \sin t) = - \gamma(t)
$$

Notice that $N$ points inward. Also if we write $p = (x, y) = (\cos t, \sin t)$ for a point on $C$, we have $T(p) = (-y, x)$ and $N(p) = -p$. That is $T(p) = R_{\pi/2} (p)$ and $N(p) = R_{\pi/2} (T(p)) = R_{\pi} (p) = -p$.

If we choose $N(p) = p$ to be the outer pointing normal to the unit circle, then we must parametrise in the clockwise direction to ensure $\lbrace T, N \rbrace$ is positively oriented. Thus $\gamma(t) = (\sin t, \cos t)$ leads to $T = (\cos t, -\sin t)$ and $N = R_{\pi/2} (T) = (\sin t, \cos(t) = \gamma(t)$.

