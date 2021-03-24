# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:13:15 2020

@author: Leonardo Saccotelli
"""
import numpy as np
from Algoritmi_Grafico_Integrali import *
from Algoritmi_Quadratura import *

#Definizione della funzione da integrare
def f(x):
    y = x**(1/3)
    return y 

#Definizione della primitiva di f
def F(x):
    y = 3/4 * x * x**(1/3)
    return y

#Definizione dell'intervallo di integrazione
a = 1.0 ; b = 6.0

#Definizone del numero di intervalli in [a,b] 
N = 2

#Calcolo dell'integrale di f(x) tramite trapezi composti
TC = CompositeTrapezoid(f, a, b, N)

#Calcolo dell'integrale di f(x) tramite Simpson composti
SC = CompositeSimpson(f, a, b, N)

#Calcolo dell'integrale di f(x) tramite la primitiva
I = F(b) - F(a)

#Calcolo dell'errore commesso tramite trapezi composti
E_tc = abs(I - TC)

#Calcolo dell'errore commesso tramite simpson composti
E_sc = abs(I - SC)

# Visualizzazione risultati relativi al metodo di trapezi
print('  Numero di nodi di quadratura:    %d' %N)
print('  ----------------------------------------------')
print('  Integrale esatto:                %f ' % I)
print('  Formula del trapezio composta:   %f ' % TC)
print('  Errore commesso:                 %e ' % E_tc)
print('  ----------------------------------------------')
# Visualizzazione risultati relativi al metodo di Simpson
print('  Integrale esatto:                %f ' % I)
print('  Formula di Simpson composta:     %f ' % SC)
print('  Errore commesso:                 %e ' % E_sc)

#Visualizzazione del grafico
DrawCompositeTrapezoid(f, a, b, N)
DrawCompositeSimpson(f, a, b, N)




