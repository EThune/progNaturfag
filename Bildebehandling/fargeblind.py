# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:30:06 2019


"""

from pylab import *

# Lager en funksjon som simulerer fargeblindhet
def fargeblindhet_simulator(img):
    rød = img[:, :, 0]
    grønn = img[:, :, 1]
    blå = img[:, :, 2]
    rødgrønn = 0.5*rød + 0.5*grønn
    fargeblind_bilde = img.copy()
    fargeblind_bilde[:, :, 0] = rødgrønn
    fargeblind_bilde[:, :, 1] = rødgrønn
    return fargeblind_bilde

# Lastar inn bilete
img = imread("fig/fargehjul.png")

# Vis originalen
imshow(img)
axis('off')
show()

# Vis rød-grønn fargeblind versjon
imshow(fargeblindhet_simulator(img))
axis('off')
show()

img = imread("fig/fargeblind_test2.jpg")

# Vis originalen
imshow(img)
axis('off')
show()

# Vis rød-grønn fargeblind versjon
imshow(fargeblindhet_simulator(img))
axis('off')
show()