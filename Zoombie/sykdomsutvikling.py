# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:41:37 2019

@author: emithun
"""
from numpy import *
from matplotlib . pyplot import *
T = 60  # utvikling over antall dager
dt = 1./24 # tidssteg per dag (1/12 blir hver 2.time)
n = int (T/dt) # antall tidssteg
s0=1999 # antall friske som kan bli smittet
i0=1 # antall som er smittet
r0=0 # antall som er immune
N=s0+i0+r0 # total befolkning
# Lager tomme lister med verdier for t ( tiden ), S ( friske ), I ( smitta ) og R (immune):
S = zeros (n+1)
I = zeros (n+1)
R = zeros (n+1)
t = zeros (n+1)
# Fyller inn startverdier for alle listene :
S[0] = s0
I[0] = i0
R[0] = r0
t[0] = t0

b = 0.0005 # smittrate
f = 0.1 # friskrate
a = 1./(7/dt)

for i in range (0, n):
    S[i +1] = S[i] - b*dt*S[i]*I[i] + S[i]*a*dt
    I[i +1] = I[i] + b*dt*S[i]*I[i] - f*dt*I[i]
    R[i +1] = R[i] + f*dt*I[i]
    t[i +1] = t[i] + dt
plot (t, S, t, I, t, R)
legend ([" Friske som kan bli smittet "," Syke ", " Immune "])
title ('Sykdomsutvikling')
xlabel ('dager ')
ylabel ('populasjon ')
show ()