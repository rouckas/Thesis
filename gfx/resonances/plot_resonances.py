#!/usr/bin/env python

import pylab as P
import numpy as N

data = N.loadtxt("resonances.txt")
Omega = 2*N.pi*20e6
m = 1.67262158e-27
q0 = 1.602189e-19
B1 = m*Omega/q0
E00 = 100
r00 = 5e-5
r0 = 5e-5
V0 = q0**2*(E00*r00/r0)**2/(4*m*Omega**2)
print B1
print V0/q0

data[:,1] *= m # forgot to multiply by mass in analyze_resonances.py

fig = P.figure(figsize=(4.5,2.6))
ax = fig.add_axes([0.12, 0.13, 0.48, 0.8])
ax.semilogy(data[:,0]/B1, data[:,1]/V0)
ax.set_xlabel(r"$\Xi$")
ax.set_ylabel(r"$E_{\rm max}/V_0^*$")
ax.set_xlim([0, 2.3])

from matplotlib.ticker import FixedLocator
xticks = N.array([0, 1/3., 1/2., 1, 2])
ax.xaxis.set_major_locator(FixedLocator(xticks))
ax.set_xticklabels(["0",  \
        "1/3    ", "    1/2", "1", "2"])


ax2 = fig.add_axes([0.73, 0.13, 0.265, 0.33])
ax2.semilogy(data[:,0]/B1, data[:,1]/V0)
ax2.set_xlim([1./3-.0015, 1./3+.0015])
xticks = N.array([1/3.-0.001, 1/3., 1/3.+0.001])
ax2.xaxis.set_major_locator(FixedLocator(xticks))
ax2.set_xticklabels(["-0.001",  \
        "0", "0.001"])
ax2.set_ylabel(r"$E_{\rm max}/V_0^*$")
ax2.set_xlabel(r"$\Xi-1/3$")
ax2.set_ylim([3,3e6])


ax3 = fig.add_axes([0.73, 0.6, 0.265, 0.33])
ax3.plot(data[:,0]/B1, data[:,1]/V0)
ax3.set_xlim([1./4-.0003, 1./4+.00015])
ax3.set_ylim([3.38,3.5])
xticks = N.array([1/4.-0.0002, 1/4.])
ax3.xaxis.set_major_locator(FixedLocator(xticks))
ax3.set_xticklabels(["-0.0002",  \
        "0"])
ax3.set_ylabel(r"$E_{\rm max}/V_0^*$")
ax3.set_xlabel(r"$\Xi-1/4$")
ax3.tick_params(axis='y', labelsize=7)
fig.savefig("resonances.pdf")
