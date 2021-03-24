# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:42:23 2020

@author: Leonardo Saccotelli
"""

import numpy as np
import matplotlib.pyplot as plt
from Algoritmi_Quadratura import *
from matplotlib import rc

#Definizione della funzione da integrare
def f(x):
    y = 1/x + 1/(x**2)
    return y 

#Definizione della primitiva di f
def F(x):
    y = -1/x + np.log(abs(x))
    return y

#Definizione dell'intervallo di integrazione
a = 1.0 ; b = 10.0

#Calcolo l'integrale di f attraverso la sua primitiva
I = F(b) - F(a)

# Formula Simpson e trapezi composti al variare di N
#Numero massimo di intervalli su cui integrare
N_max = 10000
N_range = range(4000, N_max, 40)

#Creo i vettori che conterranno l'errore di integrazione al variare di N
Err_Simpson = np.zeros(len(N_range))
Err_Trapezi = np.zeros(len(N_range))

#Indice per i vettori degli errori
k = 0 

for N in N_range:
    #Calcolo l'integrale tramite Simpson
    CS = CompositeSimpson(f,a,b,N)
    #Calcolo l'integrale tramite Trapezi
    TC = CompositeTrapezoid(f, a, b, N)
    #Caloclo l'errore con Simpson
    Err_Simpson[k] = abs(I-CS)
    #Calcolo l'errore con Trapezi
    Err_Trapezi[k] = abs(I-TC)
    
    k = k + 1 
   
# Grafico errori al variare di N
plt.figure(1, figsize=(10,10))
plt.semilogy(N_range,Err_Simpson,'k--o',label='Simpson Comp.')
plt.semilogy(N_range,Err_Trapezi,'b--o',label='Trapezi Comp.')
plt.xlabel('N',fontsize=24) 
plt.ylabel('Errore',fontsize=24)
plt.legend(prop={'size':26})
plt.title('Errore formule di quadratura composte al variare di N',fontsize=26)
rc('xtick',labelsize=26)
rc('ytick',labelsize=26)