# -*- coding: utf-8 -*-
"""
@author: emithun

Funksjonen som summerer alle tall opp til verdien til variabelen stop
"""

def sumopptil(stop):
    s = 0
    for i in range (stop+1) :
        s += i
    return s

print(sumopptil(100000))