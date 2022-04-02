## https://blogs.scientificamerican.com/guest-blog/making-mathematical-art/
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

res = 8*10**3
# a, b, c, d, e, f = 10, 14, 12, 8, 18, 10
# a, b, c, d, e, f = 13, 8, 16, 10, 12, 6
# a, b, c, d, e, f = 14, 14, 12, 8, 18, 10
# a, b, c, d, e, f = 6, 3, 10, 12, 9, 10
# a, b, c, d, e, f = 5, 8, 10, 16, 9, 12
a, b, c, d, e, f = 2, 16, 13, 18, 12, 9

fig, ax = plt.subplots(figsize=(5, 5))
lines = []
for k in range(1, res):
    lines.append(
        [
            (
                np.sin(a*np.pi*k/res)**3 * (np.sin(c*np.pi*k/res)**2 + np.sin(e*np.pi*k/res)**4),
                np.cos(a*np.pi*k/res)**3 * (np.sin(c*np.pi*k/res)**2 + np.sin(e*np.pi*k/res)**4)
            ),
            (
                np.sin(b*np.pi*k/res)**3 * (np.sin(d*np.pi*k/res)**2 + np.sin(f*np.pi*k/res)**4),
                np.cos(b*np.pi*k/res)**3 * (np.sin(d*np.pi*k/res)**2 + np.sin(f*np.pi*k/res)**4)
            )
        ]
    )
ax.add_collection(
    mc.LineCollection(lines, colors="k", linewidths=0.03)
)
ax.autoscale()
ax.axis("equal")
ax.axis("off")
fig.tight_layout()
fig.savefig(
    "seg_{}_{}_{}_{}_{}_{}.pdf".format(
        str(a), str(b), str(c), str(d), str(e), str(f)
    ),
    dpi=200
)
