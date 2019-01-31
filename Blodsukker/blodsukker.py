# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:11:17 2019

@author: emithun
"""

from pylab import*

tid = [0, 10, 20, 45, 60, 90]
kontroll = [4.5, 4.8, 4.3, 4.5, 4.9, 5]
cola = [4.0, 8.0, 9.3, 6.5, 5.4, 4.5]
zero = [4.3, 5.6, 5.4, 4.9, 4.0, 4.2]

nyTid = array(tid)*2

plot(tid,kontroll,tid,cola,tid,zero)
legend(["Kontroll","Cola","Zero"])
xlabel("Tid i minutter")
ylabel("Blodsukkernivå")
title("Blodsukkernivå-forsøk")
show()