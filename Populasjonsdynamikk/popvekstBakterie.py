# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:28:18 2019

@author: emithun
"""

from numpy import *

n = 50 # antall tidsintervaller (timer)
y0 = 1 # antall bakterier naar vi starter
vr = 2 # vekstrate ( per time )
dr = 2.3 # dødsrate (etter 18 timer)

# Oppretter array for plotting
index_set = range (n +1)
y = zeros ( len( index_set ))

# Initialisering av startverdier
y [0] = y0

# Første 13 periodene er det eksponentiell vekst
for k in index_set [0:14]:
    y[k +1] = y[k] + vr*y[k]
    
# Neste 3 periodene er det ingen vekst
for i in index_set [14:17]:
    y[i+1] = y[i]
    
# Resten av periodene er det eksponentiell vekst (nedgang)
for j in index_set [17:-1]:
    y[j+1] = y[j] + (vr-dr)*y[j]
    if(y[j+1]<1000):
        print(j+1)
        break
    
from matplotlib . pyplot import *
plot ( index_set , y)
xlabel ('tid')
ylabel ('antall bakterier ')
title (' Populasjonsvekst bakterier ')
show ()