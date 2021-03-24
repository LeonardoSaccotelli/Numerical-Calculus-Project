# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:56:06 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt
from Algoritmi_Quadratura import *
from Algoritmi_Grafico_Integrali import *
from matplotlib import rc

#Definizione della funzione da integrare
def f(x):
    y = np.exp(-x**2)
    return y 

#Definizione dell'intervallo di integrazione
a = -1.0 ; b = 1.0

# Formula Simpson e trapezi composti al variare di N
#Numero massimo di intervalli su cui integrare
N_max = 2000
N_range = range(2,N_max,50)

#Creazione dei vettori per memorizzare le approssimazioni
#trovate al variare del numero di intervalli
CS = np.zeros(len(N_range))
TC = np.zeros(len(N_range))

#Indice per i vettori degli errori
k = 0 

print('|------------+-----------------------+-----------------------|')
print('|     N      |    Trapezi composti   |    Simpson composti   |')
print('|------------+-----------------------+-----------------------|')

for N in N_range:
    #Calcolo l'integrale tramite Simpson
    CS[k] = CompositeSimpson(f,a,b,N)
    #Calcolo l'integrale tramite Trapezi
    TC[k] = CompositeTrapezoid(f, a, b, N)
    print('|     %2d     |%16f       |%16f       |' %(N, TC[k] , CS[k]))
    print('|------------------------------------------------------------|')
    
    """
    DrawCompositeTrapezoid(f, a, b, N)
    DrawCompositeSimpson(f, a, b, N)"""
    k = k + 1
    

