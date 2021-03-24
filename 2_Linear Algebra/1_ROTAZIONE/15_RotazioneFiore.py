# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:39:09 2020

@author: leona
"""

import numpy as np
import matplotlib.pyplot as plt


# Disegno della figura
x = np.array([ 3.0, 3, 4, 4, 5, 4, 5, 4 , 4, 3,2,2,1,2,1,2,2,3])
y = np.array([ 1.0, 6, 5, 6, 6, 7, 8, 8, 9, 8,9,8,8,7,6,6,5,6])

plt.figure(1)
plt.plot(x,y,'b-',linewidth=1.2)
#plt.show(block=False)

# Costruzione matrice di rotazione
theta = 0.1 ;

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
    xx[i] = w[0]
    yy[i] = w[1]

#plt.figure(2)
plt.plot(xx,yy,'r-',linewidth=1.2)
plt.show(block=False)

