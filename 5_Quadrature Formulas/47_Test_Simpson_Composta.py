# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:29:31 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt
from Algoritmi_Quadratura import CompositeSimpson
from Algoritmi_Grafico_Integrali import DrawCompositeSimpson

# Funzione test da integrare
def f(x):
    y = x**3 - x 
    return y

#Primitiva della funzione test
def F(x):
    y = x**4/4 - x**2/2 
    return y

# Intervallo di integrazione
a = 1.0; b = 4.0
# Nodi della formula composta: estrapolo un certo numero di nodi equidistanti
N = 10 ; 

ISC = CompositeSimpson(f, a, b, N)

# Calcolo errore formula di simpson
I = F(b) - F(a)
E = abs(I-ISC)

# Visualizzazione risultati
print('Integrale esatto:              %f ' % I)
print('Formula del Simpson composto:  %f ' % ISC)
print('Errore commesso:               %e ' % E)

DrawCompositeSimpson(f, a, b, N)
