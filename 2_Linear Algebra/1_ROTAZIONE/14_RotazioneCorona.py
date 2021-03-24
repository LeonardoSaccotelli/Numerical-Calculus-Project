# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:22:17 2020

@author: leona
"""

import numpy as np
import matplotlib.pyplot as plt


# Disegno della figura
x = np.array([ 6.0, 12,12, 11, 9,7,6,6 ])
y = np.array([ 3.0, 3, 6, 5,7,5,6,3])

plt.figure(1)
plt.plot(x,y,'b-',linewidth=1.2)
#plt.show(block=False)

# Costruzione matrice di rotazione
theta = 10 ;

zoom = 2

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
    xx[i] = w[0]
    yy[i] = w[1]

#plt.figure(2)
plt.plot(xx,yy,'y-',linewidth=1.2)
plt.show(block=False)

