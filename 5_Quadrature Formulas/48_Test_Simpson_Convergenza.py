# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:07:18 2020

@author: Leonardo Saccotelli
"""

import numpy as np
import matplotlib.pyplot as plt
from Algoritmi_Quadratura import CompositeSimpson
from matplotlib import rc

# Funzione test da integrare
def f(x):
    y = 1/x - 1/(x**2)
    return y

# Primitiva della funzione test
def F(x):
    y = np.log(abs(x))+1/x
    return y

# Intervallo di integrazione e integrale esatto
a =2.0; b =4.0
I = F(b) - F(a)

# Formula Simpson composti al variare di N
N_max = 1000
N_range = range(2,N_max,10)
Err_Simpson = np.zeros(len(N_range))
k = 0 
for N in N_range:
    TN = CompositeSimpson(f,a,b,N)
    Err_Simpson[k] = abs(I-TN)
    k = k + 1 
   
# Grafico errori al variare di N
plt.figure(1,figsize=(10,8))
plt.semilogy(N_range,Err_Simpson,'k--o',label='Simpson Comp.')
plt.xlabel('N',fontsize=26) 
plt.ylabel('Errore',fontsize=26)
plt.legend(prop={'size':26})
plt.title('Errore formule di quadratura composte al variare di N',fontsize=26)
rc('xtick',labelsize=26)
rc('ytick',labelsize=26)

