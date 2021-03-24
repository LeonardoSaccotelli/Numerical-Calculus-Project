# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:05:49 2020

@author: Leonardo Saccotelli
"""
import numpy as np
from Zeri_di_funzione_Algoritmi import *

#Definisco la funzione di cui voglio conoscere lo zero
def f_x(x):
    y = x**3-3
    return y

#Definisco l'intervallo in cui cercare la radice 
a = 1
b = 3
#Definisco la tollerenza accettata nell'approssimare la soluzione esatta del problema
tolerance = 1.0e-5

#Stampo i risultati
x, max_iter = bisectionMethod(f_x, a, b, tolerance)
print('Risultati metodo di bisezione')
print('Numero di iterazioni eseguite: %d' %max_iter)
print('Radice trovata: %f' %x)
            