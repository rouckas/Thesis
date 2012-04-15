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
print V0

data[:,1] *= m # forgot to multiply by mass in analyze_resonances.py

fig = P.figure()
ax = fig.add_subplot(111)
ax.semilogy(data[:,0]/B1, data[:,1]/V0)
ax.set_xlabel(r"$\Xi$")
ax.set_ylabel(r"$E_{\rm max}/V_0^*$")
ax.set_xlim([0, 2.5])

from matplotlib.ticker import FixedLocator
xticks = N.array([0, 1/3., 1/2., 1, 2])
ax.xaxis.set_major_locator(FixedLocator(xticks))
ax.set_xticklabels(["0",  \
        "1/3    ", "    1/2", "1", "2"])
fig.savefig("resonances.pdf")
