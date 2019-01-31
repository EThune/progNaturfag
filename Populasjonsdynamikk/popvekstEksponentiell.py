# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:28:18 2019

@author: emithun
"""

from numpy import *

n = 12*2 # antall tidsintervaller
y0 = 100 # antall harer naar vi starter
vr = 0.05 # vekstrate ( dvs 5% per mnd )
dr = 0.02 # vekstrate for død (dvs. 2% per mnd)

# Array for plotting
index_set = range (n +1)
y = zeros ( len( index_set ))

# Startverdier
y [0] = y0

# Eksponentiell vekst
for k in index_set [: -1]:
    y[k +1] = y[k] + (vr-dr)*y[k]
    
from matplotlib . pyplot import *
plot ( index_set , y)
xlabel ('tid')
ylabel ('antall harer ')
title (' Populasjonsvekst harer ')
show ()