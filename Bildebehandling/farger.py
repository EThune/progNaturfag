# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:30:52 2019

@author: emithun

I dette eksempelet viser ein korleis eit digitalt bilde er bygd opp av lag med fargar.
Eksempelet viser forskjellege effektar ein kan legge på bilete

Til slutt blir bilete redigert til gråfilter
"""

from pylab import *
gray() # Nødvendig for at gråtonebilder skal vises riktig

from skimage import data

img = imread("fig/peppers.png") # Leser inn bilete fra fil
imshow(img) # Viser bilete
show() # Viser bilete


# Viser bildene i gråskala med berre eit lag farge
red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

imshow(red)
axis('off')
title('Red')
show()
imshow(green)
axis('off')
title('Green')
show()
imshow(blue)
axis('off')
title('Blue')
show()

#Viser eit og eit fargebilde
red = img.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0
green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0
blue = img.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0

imshow(red)
axis('off')
title('Red')
show()
imshow(green)
axis('off')
title('Green')
show()
imshow(blue)
axis('off')
title('Blue')
show()

# Lage gråtoner utifra et bilde
red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]
imshow(red/3 + green/3 + blue/3)
show()

# Meir avansert med vekting av fargar
imshow(red * 299. / 1000 + green * 587. / 1000 + blue * 114. / 1000)
show()