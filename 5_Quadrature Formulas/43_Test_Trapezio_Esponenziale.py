# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:52:23 2020

@author: Leonardo Saccotelli
"""

import numpy as np
from Algoritmi_Quadratura import Trapezoid
from Algoritmi_Grafico_Integrali import DrawTrapezoid

# Funzione test da integrare
def f(x):
    y = np.exp(x)
    return y

# Primitiva della funzione test
def F(x):
    y = np.exp(x)
    return y

# Intervallo di integrazione
a = 0 ; b = 2.0

# Calcolo formula del trapezio
T = Trapezoid(f, a, b)

# Calcolo integrale esatto
I = F(b) - F(a)

#Calcolo errore commesso
E = abs(I-T)

# Visualizzazione risultati
print('Integrale esatto:     %f ' % I)
print('Formula del trapezio: %f ' % T)
print('Errore commesso:      %e ' % E)

#----- Rappresentazione grafica
DrawTrapezoid(f, a, b)