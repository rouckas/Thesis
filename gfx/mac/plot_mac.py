import pylab as P
import numpy as N

def transmission(EB, E0, eta):
    EB = N.array(EB)
    T = N.ones(N.shape(EB))
    limit = E0*(1-eta)
    T[N.logical_and(EB>limit, EB < E0)] = 1-N.sqrt(1-(1-EB[EB>limit]/E0)/eta)
    T[EB>=E0] *= 0
    return T

EB = N.linspace(0, 1.1, 150)
E0 = 1
fig = P.figure()
ax = fig.add_subplot(111)
ax.plot(EB, transmission(EB, E0, 1))
ax.plot(EB, transmission(EB, E0, 0.33333))
ax.plot(EB, transmission(EB, E0, 0.1))
ax.plot([0, 1, 1, 1.1], [1, 1, 0, 0], ":k")
#ax.text(0.2, 0.3, r"${B_1}/{B_2} = 1$")
#ax.text(0.5, 0.4, r"${B_1}/{B_2} = 1$")
#ax.text(0.45, 0.6, r"${B_1}/{B_2} = 1$")
ax.annotate(r"ideal filter", xy=(1., 0.9),  xycoords='data',
        xytext=(-35, 22), textcoords='offset points',
        arrowprops=dict(arrowstyle="->")
        )
ax.annotate(r"${B_1}/{B_2} = 10$", xy=(0.9, 0.9),  xycoords='data',
        xytext=(-70, 22), textcoords='offset points',
        arrowprops=dict(arrowstyle="->")
        )
ax.annotate(r"${B_1}/{B_2} = 3$", xy=(0.68, 0.75),  xycoords='data',
        xytext=(-50, -22), textcoords='offset points',
        arrowprops=dict(arrowstyle="->")
        )
ax.annotate(r"${B_1}/{B_2} = 1$", xy=(0.45, 0.33),  xycoords='data',
        xytext=(-50, -22), textcoords='offset points',
        arrowprops=dict(arrowstyle="->")
        )
ax.set_ylim(ymax=1.2)
ax.set_xlim(xmax=1.1)
ax.set_xlabel("$U/E_0$")
ax.set_ylabel("transmission")
fig.savefig("transmission.pdf")
