# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:14:46 2019

@author: emithun
"""
from pylab import *
gray() # Nødvendig for at gråtonebilder skal vises riktig

# Funksjon som returnerer eit gråtonebilete
def rgb2gray(img):
    red = img[:, :, 0]
    green = img[:, :, 1]
    blue = img[:, :, 2]
    gray = red/3 + green/3 + blue/3
    return gray

img = imread("fig/1337_shrk.jpg")
gray = rgb2gray(img)
imshow(img)
axis('off')
show()
imshow(gray)
axis('off')
show()