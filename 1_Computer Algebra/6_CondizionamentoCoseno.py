# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:56:42 2017

@author: Leonardo Saccotelli
"""
# In questo software vogliamo studiare il condizionamento di alcune funzioni elementari.
# Studieremo la funzione f (x) = cos (x); prima di tutto studieremo la funzione
# cos (x) in un intervallo di valori; inseriremo una perturbazione e perturberemo
# l'intervallo di punti in cui stiamo studiando la funzione.
# Calcoleremo il coseno ogni punto x perturbato.
# Alla fine studieremo l'errore verificatosi nella funzione cos (x) quando l'abbiamo calcolato
# in un intervallo di valori perturbati. Stamperemo anche il grafico delle funzioni.

import numpy as np
import math
import matplotlib.pyplot as plt

print(' -------------------------------------------------------')
print('|  STUDYING OF CONDITIONING OF FUNCTION: F(x) = cos(x)  |')
print(' -------------------------------------------------------')

perturbation = 0

perturbation = float(input('  Enter a perturbation: '))

#Selezioniamo 50 punti equidistanti nell'intervallo [2Pi,6Pi]
x = np.linspace(2*np.pi, 6*np.pi,100)



#Calcoliamo il valore di cos(x) in ogni punto 
y = np.cos(x)

errorX = np.zeros(len(x))

#Perturbo tutti i punti x nell'intervallo scelto
for i in range(len(y)):
    errorX[i] = x[i] + perturbation

#Calcolo il coseno in ogni punto di x peturbato
errorY = np.cos(errorX)    

relativeErrorX = np.zeros(len(errorX))

#Calcolo l'errore relativo commesso sul dato x
for i in range(len(y)):
    relativeErrorX[i] = abs(x[i]- errorX[i]) / abs(x[i])
    
relativeErrorY = np.zeros(len(relativeErrorX))

#Calcolo dell'errore relativo commesso nel calcolo del seno in punti di x perturbati
for i in range(len(y)):
    relativeErrorY[i] = relativeErrorX[i] * abs(-x[i]*math.tan(x[i]))

#Stampo a video una tabella per confrontare gli errori su input e output
print('\n -------------------------------------------------------')

strErrorX = 'Error_X'
strErrorY = 'Error_Y'

print('%25s %25s' %(strErrorX,strErrorY))
print(' -------------------------------------------------------')

for i in range(len(y)):
    print('%25e %25e' %(relativeErrorX[i],relativeErrorY[i]))


#stampa dei risultati e visualizzazione grafico
plt.loglog(relativeErrorX,relativeErrorY,':k')
plt.xlabel('error_X')
plt.ylabel('error_Cos')
plt.title('Relative error on the function f(x)=cos(x)')

errorGraphic = plt.figure(1)
errorGraphic.savefig("Coseno.png")

plt.show()



