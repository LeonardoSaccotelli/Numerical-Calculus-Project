# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:03:33 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from Algoritmi_Quadratura import CompositeTrapezoid

# Funzione test da integrare
def f(x):
    y = 1/x - 1/(x**2)
    return y

# Primitiva della funzione test
def F(x):
    y = np.log(abs(x))+1/x
    return y

# Intervallo di integrazione e integrale esatto
a =2.0; b = 4.0
I = F(b) - F(a)

# Formula trapezi composti al variare di N
N_max = 1000

N_range = range(2,N_max,10)

Err_Trap = np.zeros(len(N_range))

k = 0 

for N in N_range:
    TC = CompositeTrapezoid(f,a,b,N)
    Err_Trap[k] = abs(I-TC)
    k = k + 1 
   
# Grafico errori al variare di N
plt.figure(1,figsize=(14,8))
plt.semilogy(N_range,Err_Trap,'k--o',label='Trap. Comp.')
plt.xlabel('N',fontsize=26) 
plt.ylabel('Errore',fontsize=26)
plt.legend(prop={'size':26})
plt.title('Errore formule di quadratura composte al variare di N',fontsize=26)
rc('xtick',labelsize=26)
rc('ytick',labelsize=26)

