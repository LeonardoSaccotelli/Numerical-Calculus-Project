# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:50:58 2020

@author: leonardo Saccotelli
"""


import numpy as np
import matplotlib.pyplot as plt

# Disegno della figura
x = np.array([ 2.0, 2, 1, 8, 15, 14, 14, 5, 5, 8, 8, 2])
y = np.array([ 1.0, 10, 9, 16, 9, 10, 1, 1, 6, 6, 1, 1])
plt.figure(1)
plt.plot(x,y,'b-',linewidth=1.2)
#plt.show(block=False)

# Costruzione matrice di rotazione
theta = 2.3 ;

zoom = 0.5

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
plt.plot(xx,yy,'g-',linewidth=1.2)
plt.show(block=False)