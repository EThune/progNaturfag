# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:30:52 2019

@author: emithun
"""

from pylab import *
gray() # Nødvendig for at gråtonebilder skal vises riktig

from skimage import data
img = data.camera() #Henter test-bilete frå biblioteket

imshow(img)
colorbar() # Viser ein fargeskala med verdiar for alle fargane (gråfargane)
show()

print(img) # Array med gråfarge verdier

print(img.shape) # Oppløsning på bilete (pixlar)

print(img.min() , img.max()) # Minste og høgste verdi

print(img.dtype)    # Datatype i arrayet (uint8 står for unsigned integer med 8 bits/1 Byte)