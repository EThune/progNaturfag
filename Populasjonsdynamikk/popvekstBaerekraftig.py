# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:52:24 2019

@author: emithun
"""

# Leser inn bibliotek
from numpy import *
from pylab import *

# Setter opp startverdier
y0 = 100 # antall individer naar vi starter
M = 500 # baereevne
R = 0.05 # vekstrate naar vi starter
N = 12*10 # antall tidsintervaller

index_set = range (N +1) # array som går fra 0 til N
y = zeros (len( index_set )) # array med like mange 0'ere som antall element i index_set


# Regn ut loesning for hvert intervall
y [0] = y0
for n in index_set [1:]:
    y[n] = y[n -1] + R*y[n -1]*(1 - y[n -1]/ float (M))

# plot resultat
plot ( index_set , y)
ylim(bottom=0) # For at y-aksen skal starte på 0
xlabel ('mnd ')
ylabel ('antall harer ')
title ('Tetthetsavhengig populasjonsvekst harer ')
show ()