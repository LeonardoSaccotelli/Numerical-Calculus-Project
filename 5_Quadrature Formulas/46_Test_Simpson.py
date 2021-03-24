# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:14:07 2020

@author: Leonardo Saccotelli
"""

import numpy as np
import matplotlib.pyplot as plt
from Algoritmi_Quadratura import Simpson
from Algoritmi_Grafico_Integrali import DrawSimpson

# Funzione test da integrare
def f(x):
    y = -6*x**2 + 16*x - 4
    return y

# Primitiva della funzione test
def F(x):
    y = -2*x**3 + 8*x**2 - 4*x
    return y

# Intervallo di integrazione
a = 1.0 ; b = 2.0

# Calcolo formula della formula di Simpson
IS = Simpson(f, a, b)

# Calcolo errore formula di simpson
I = F(b) - F(a)
E = abs(I-IS)

# Visualizzazione risultati
print('Integrale esatto:     %f ' % I)
print('Formula di Simpson:   %f ' % IS)
print('Errore commesso:      %e ' % E)

DrawSimpson(f, a, b)


