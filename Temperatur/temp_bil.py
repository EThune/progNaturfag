# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:34:06 2019

@author: emithun
"""

from pylab import *

t0 = 0 # starttid
T0 = 7 # grader celsius
k = 0.16 # varmefaktor
N = 10000 # antall steg
tid = 30 # antall minutter

dt = ( tid - t0 ) /( N -1) # steglengde
t = zeros ( N )
T = zeros ( N )
Tder = zeros ( N )

# startverdier
t [0] = t0
T [0] = T0
T_o = 30

for i in range(N -1) :
    Tder [ i ] = -k *( T [ i ] - T_o )
    T [ i +1] = T [ i ] + Tder [ i ]* dt
    t [ i +1] = t [ i ] + dt

figure () # Til å plotte i eget vindu
plot (t , T )
title (" Temperaturutvikling inni en bil")
xlabel (" Antall minutter ")
ylabel (" Temperatur i celsius ")

T_o = zeros ( N )
for i in range(N -1) :
    T_o [ i ] = 5* cos ( pi **2/15* t [ i ]) + 19
    Tder [ i ] = -k *( T [ i ] - T_o [ i ])
    T [ i +1] = T [ i ] + Tder [ i ]* dt
    t [ i +1] = t [ i ] + dt

figure ()
plot (t , T )
title (" Temperaturutvikling inni en bil")
xlabel (" Antall minutter ")
ylabel (" Temperatur i celsius ")
show () # Til å vise frem begge vinduene
