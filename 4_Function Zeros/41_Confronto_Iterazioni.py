# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:09:08 2020

@author: Leonardo Saccotelli
"""
import numpy as np
from Zeri_di_funzione_Algoritmi import *

#Definisco la funzione di cui voglio conoscere lo zero
def f_x(x):
    y = 3*x**3 + 5*x**2 - 6*x - 5
    return y

#Definisco la derivata prima della funzione di cui 
#voglio conoscere lo zero
def df_x(x):
    y = 9*x**2 + 10*x - 6
    return y
    
#Definisco l'intervallo in cui cercare lo zero
a = 1

b = 5

#Definisco la tollerenza accettata nell'approssimare la soluzione esatta del problema
tolerance = 1.0e-5

#Fisso il numero massimo di iterazioni
maxIteration = 100 

#Calcolo dello zero attraverso il metodo di bisezione
xBis, iterBis = bisectionMethod(f_x, a, b, tolerance)

#Calcolo dello zero attraverso il metodo di Newton
xNewton, iterNewton = NewtonMethod(f_x, df_x, b, tolerance, maxIteration)

#Calcolo dello zero attraverso il metodo delle secanti
xSec, iterSec = SecantMethod(f_x, a, b, tolerance, maxIteration)

#Calcolo dello zero attraverso il metodo delle corde
xCor, iterCor = stringRootMethod(f_x, a, b, tolerance, maxIteration)

strBis = 'Bisezioni successive'
strNew = 'Newton (tangenti)'
strSec = 'Secanti'
strCor = 'Corde'
       
print('|-----------------------+-----------------------+------------------|')
print('|   Metodo utilizzato   |  Iterazioni eseguite  |     Soluzione    |')
print('|-----------------------+-----------------------+------------------|')
print('| %20s  |  %10d           |     %f     |' %(strBis, iterBis, xBis))
print('|-----------------------+-----------------------+------------------|')
print('| %19s   |  %10d           |     %f     |' %(strNew, iterNewton, xNewton))
print('|-----------------------+-----------------------+------------------|')
print('| %14s        |  %10d           |     %f     |' %(strSec, iterSec, xSec))
print('|-----------------------+-----------------------+------------------|')
print('| %13s         |  %10d           |     %f     |' %(strCor, iterCor, xCor))
print('|-----------------------+-----------------------+------------------|')