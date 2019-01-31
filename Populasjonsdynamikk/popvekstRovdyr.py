# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:01:41 2019

@author: emithun
"""

from numpy import *
from matplotlib . pyplot import *

n = 12*100 # antall tidsintervaller
y0 = 100 # antall byttedyr naar vi starter
x0 = 50 # antall rovdyr naar vi starter
index_set = range (n +1)

# Array for plotting
x = zeros ( len( index_set ))
y = zeros ( len( index_set ))

# Prosentfaktor for vekst
a = 0.05 # sultrate gauper
b = 0.0003 # reproduksjonsrate gauper
c = 0.02 # vekstrare harer
d = 0.0001 # spistrate harer

# Startverdier
y [0] = y0
x [0] = x0

# Bereknar utvikling i bestandane
for k in index_set [: -1]:
    y[k +1] = y[k] + c*y[k] - d*y[k]*x[k]
    x[k +1] = x[k] - a*x[k] + b*x[k]*y[k]
    if (x[k+1]>x[k] and x[k]<x[k-1]):
        print(x[k])
        

plot ( index_set , x)
plot ( index_set , y)
legend ([" Gauper "," Harer "])
title ('Hare vs. gaupe : populasjonsutvikling ' )
xlabel ('mnd ')
ylabel ('populasjon ')
show ()