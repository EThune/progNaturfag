# -*- coding: utf-8 -*-
"""
Her er koden for å finne nullpunkt for ein gitt funksjon.
Betingelse for at den skal fungere er at startverdiane a og b har 
funksjonsverdiar med forskjellege forteikn.
"""

from pylab import *

a=1
b=10

t = linspace(a,b,1000) # Lagar eit finfordelt array med tall fra a til b (1000 tall)
y = zeros(len(t)) # Lagar eit array som skal få funksjonsverdiane til funksjonen

# Lagar ein funksjon som returnerer funksjonverdi for gitt x
def f(x):
    return x**2-3*x-2   # Funksjonen


# Kode som blir kjørt så lenge betingelsen er oppfylt
while (abs(a-b)>0.00001):
    c=(b+a)/2
    if ((f(a)*f(c))<0):
        b=c
    elif (f(a)*f(c)>0):
        a=c
    else:
        a=b=0
        break
    print("Nedre grense er: ", a , " og øvre grense er ", b)

print((a+b)/2) # Skriv ut nullpunktet


#I denne delen kalkulerar me alle funksjonsverdiar og plottar grafen til funksjonen
for i in range(len(t)):
    y[i] = f(t[i])

plot(t,y)