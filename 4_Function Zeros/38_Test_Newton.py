# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:19:26 2020

@author: Leonardo Saccotelli
"""
import numpy as np
from Zeri_di_funzione_Algoritmi import *

#Definisco la funzione di cui voglio conoscere lo zero
def f_x(x):
    y = x**3 - 3
    return y

#Definisco la derivata prima di f
def df_x(x):
    y = 3*x**2
    return y


#Definisco l'intervallo in cui cercare la radice 
a = 0
b = 3
#Definisco la tollerenza accettata nell'approssimare la soluzione esatta del problema
tolerance = 1.0e-5

#Stampo i risultati
x, max_iter = NewtonMethod(f_x, df_x, b, tolerance, 50)

print('Risultato metodo di Newton:')
print('Numero di iterazioni eseguite: %d' %max_iter)
print('Soluzione trovata: %f' %x)


