#!/usr/bin/env python
import numpy as N
import pylab as P

recalculate = False
if recalculate:
    data = N.loadtxt("./1.290000e+00T_rf/H_NEG_traj_0.dat")[:2450,:2]
    N.savetxt("data_beat.txt", data)
else:
    data = N.loadtxt("data_beat.txt")

fig = P.figure()
ax = fig.add_axes([0,0,1,1])

phi = N.linspace(-0.5, 1, 100)
r0 = 0.00005
x0 = 0.01
y0 = 0.01
ax.plot(-N.sin(phi)*r0+x0, N.cos(phi)*r0+y0,"r")

ax.plot(data[:,0], data[:,1],"k", linewidth=0.5)

ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.axis("equal")
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

fig.savefig("beats.pdf")
