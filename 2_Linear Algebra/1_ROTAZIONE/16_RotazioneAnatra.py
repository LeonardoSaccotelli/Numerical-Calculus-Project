# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 01:06:19 2020

@author: leona
"""

import numpy as np
import matplotlib.pyplot as plt


# Disegno della figura
x = np.array([ 6.0, 7, 12, 14, 14, 13, 11, 9 , 7, 8, 7,   6, 5, 6, 7, 6])
y = np.array([ 3.0, 2, 2 , 4,  6,  5,  6,  6,  4, 9, 10, 10, 9, 9, 8, 3])

plt.figure(1)
plt.plot(x,y,'b-',linewidth=1.2)
#plt.show(block=False)

# Costruzione matrice di rotazione
theta = -0.3 ;

zoom = 1.5

A = zoom *np.array([[ np.cos(theta), -np.sin(theta)], \
    [np.sin(theta) , np.cos(theta)]])

# Rotazione di ciascun punto della figura
xx = x*0 ; yy = y*0
for i in range(x.size):
    #Prendo coppie (x,y)
    z = np.array([x[i],y[i]])
    #applico ad ogni coppia la matrice di rotazione 
    w = np.dot(A,z)
    #Aggiorno le cordinate (x,y) dopo la rotazione
    xx[i] = w[0]+3
    yy[i] = w[1]+2.5

#plt.figure(2)
plt.plot(xx,yy,'r-',linewidth=1.2)
plt.show(block=False)

