#!/usr/bin/env python

import pylab as P
import numpy as N

recalculate = False
if recalculate:
    x0 = 1e-2
    y0 = 1e-2
    Tmax = 4600
    traj_exact = N.loadtxt("./m5.000000e-02T_rf/H_NEG_traj_1.dat")[:Tmax,:]
    traj_adiab = N.loadtxt("./m5.000000e-02T/H_NEG_traj_1.dat")[:Tmax,:]
    traj_exact[:,0] -= x0
    traj_exact[:,1] -= y0
    traj_adiab[:,0] -= x0
    traj_adiab[:,1] -= y0
    Tx = traj_exact[:,0]
    Ty = traj_exact[:,1]
    Tr = N.sqrt(Tx**2 + Ty**2)
    Tp = N.arctan2(Ty, Tx)
    Tp -= 0.01
    traj_exact[:,0] = N.cos(Tp)*Tr
    traj_exact[:,1] = N.sin(Tp)*Tr

    U = 100
    r0 = 5.3e-5
    r00 = 5e-5
    Omega = 2*N.pi*20e6
    m = 1.67e-27
    q = 1.6e-19
    B = 0.05
    dt = 1e-9
    oc = q*B/m

    time_axis = N.arange(len(Tx))*dt
    v = 0.5*q*(U*r00/r0)**2/(r0*m*Omega**2*B)
    x_drift = -N.sin(v/r0*time_axis)*(r0)
    y_drift = N.cos(v/r0*time_axis)*(r0)


    traj_drift = N.hstack((
        x_drift.reshape((len(x_drift),1)),
        y_drift.reshape((len(y_drift),1))
        ))

    plot_data = N.hstack((traj_exact[:,:2], traj_adiab[:,:2], traj_drift))
    N.savetxt("traj_plot_data.txt", plot_data)
else:
    plot_data = N.loadtxt("traj_plot_data.txt")

traj_exact = plot_data[:,:2]
traj_adiab = plot_data[:,2:4]
traj_drift = plot_data[:,4:]

xdim = 3.5
ydim = xdim/2
fig = P.figure(figsize=(xdim, ydim))
P.rcParams["legend.fontsize"] = 7

ax = fig.add_axes([0,0,1,1])
ax.plot(traj_exact[:,0], traj_exact[:,1], "r", linewidth=0.5, label="exact trajectory")
ax.plot(traj_adiab[:,0], traj_adiab[:,1], "k", linewidth=1.2, label="adiabatic approximation")
ax.plot(traj_drift[:,0], traj_drift[:,1], "--", color="gray", linewidth=2, label="adiabatic + drift approximation")
ax.legend(loc="lower right", frameon=False, scatterpoints=4)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.axis("equal")
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
#ax.axis["right"].set_visible(False)
fig.savefig("traj.pdf")
