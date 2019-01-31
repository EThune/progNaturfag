# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:21:14 2019

@author: emithun
"""

from pylab import *
gray() # Nødvendig for at gråtonebilder skal vises riktig

# Laster inn bilete fra fil
raw_img = imread("fig/matrix_red_dress.jpg")

# Funksjon som gjer eit bilete til gråtonebilete
def rgb2gray(img):
    red = img[:, :, 0]
    green = img[:, :, 1]
    blue = img[:, :, 2]
    gray = red/3 + green/3 + blue/3
    return gray

# Henter ut gråtoner og fargekanaler
gray = rgb2gray(raw_img)
red = raw_img[:, :, 0]
green = raw_img[:, :, 1]
blue = raw_img[:, :, 2]

# Henter ut kun de pikslene som oppfyller kravet i linje 29 og viser bilete
dress = (red > 2.5*green)*(red > 2.2*blue)
imshow(dress)
show()

# Lag en ny variant av bildet, så vi ikke endrer originalen
img = raw_img.copy()

img[:, :, 0] = gray
img[:, :, 1] = gray
img[:, :, 2] = gray
img[dress] = raw_img[dress] ## Legger på rødfargen
figure(figsize=(12, 8))
imshow(img)
axis('off')
show()