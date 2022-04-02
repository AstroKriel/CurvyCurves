## https://www.quantamagazine.org/solution-creating-art-with-mathematics-20151030
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

t = np.linspace(1, 5*10**3, 10**4)
a, b, c, d = 17, 4, 4, 3

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(
    np.cos(t) + np.cos(a*t)/c + np.sin(b*t)/d,
    np.sin(t) + np.sin(a*t)/c + np.cos(b*t)/d,
    "k-", linewidth=0.02
)
ax.axis("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(
    "curve_{}_{}_{}_{}.pdf".format(
        str(a), str(b), str(c), str(d)
    ),
    dpi=200
)
