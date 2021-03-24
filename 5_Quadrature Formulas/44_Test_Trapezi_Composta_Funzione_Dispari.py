# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:25:59 2020

@author: Leonardo Saccotelli
"""


import numpy as np
from Algoritmi_Quadratura import CompositeTrapezoid
from Algoritmi_Grafico_Integrali import DrawCompositeTrapezoid

# Funzione test da integrare
def f(x):
    y = 5*(x**3) + 6*x - 2
    return y

# Primitiva della funzione test
def F(x):
    y = 5*(x**4)/4 + 3 * (x**2) - 2 * x
    return y

# Intervallo di integrazione
a = - 1.0 ; b = 1.0
# Nodi della formula composta: estrapolo un certo numero di nodi equidistanti
N =  50

#Calcolo dell'integrale attraverso trapezio composto
TC = CompositeTrapezoid(f, a, b, N)

# Calcolo errore formula del trapezio
I = F(b) - F(a)
E = abs(I-TC)

# Visualizzazione risultati
print('Integrale esatto:              %f ' % I)
print('Formula del trapezio composta: %f ' % TC)
print('Errore commesso:                %e ' % E)

#----- Rappresentazione grafica
DrawCompositeTrapezoid(f, a, b, N)

