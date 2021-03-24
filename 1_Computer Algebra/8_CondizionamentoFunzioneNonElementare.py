# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:32:07 2020

@author: leonardo
"""

# In questo software vogliamo studiare il condizionamento di alcune funzioni elementari.
# Studieremo la funzione f (x) = 1- Sqrt(1-x^2); prima di tutto studieremo la funzione
# in un intervallo di valori; inseriremo una perturbazione e perturberemo
# l'intervallo di punti in cui stiamo studiando la funzione.
# Calcoleremo il coseno ogni punto x perturbato.
# Alla fine studieremo l'errore verificatosi nella funzione quando l'abbiamo calcolato
# in un intervallo di valori perturbati. Stamperemo anche il grafico delle funzioni.

import numpy as np
import matplotlib.pyplot as plt

#Metodo per la costruzione della funzione che vogliamo studiare
#Riceve come parametro un array di ascisse, restituisce un array 
#di ordinate calcolate nella funzione che vogliamo analizzare
def createFunction(xArray):
    #Creo un vettore che conterrà le ordinate e lo azzero
    function = np.zeros(len(xArray))
    
    #Calcolo f in ogni punto x ricevuto
    for i in range(len(xArray)):
        function[i] = (1-np.sqrt(1-(xArray[i]**2)))
    
    #Restituisco il vettore di ordinate
    return function


#Metodo utilizzato per calcolare l'indice di condizionamento del problema
#Per ogni ascissa, calocliamo abs(x*f'/f)
def createK(xArray):
    #Creo un array che conterrà per ogni x, k(f(x))
    k = np.zeros(len(xArray))
    
    #Calcolo K(f(x)) per ogni x
    for i in range(len(xArray)):
        k[i] = abs((xArray[i]**2)/(np.sqrt(1-(xArray[i]**2))-1 +xArray[i]**2))
    #restituisco k(f(x))
    return k

print(' ----------------------------------------------------------------')
print('|  STUDYING OF CONDITIONING OF FUNCTION: F(x) = 1 - sqrt(1-x^2)  |')
print(' ----------------------------------------------------------------')

perturbation = 0

perturbation = float(input(' Enter a perturbation: '))

#Seleziono 100 punti diversi nell'intervallo (-1,1)
x = np.linspace(-(1-1.0e-14),(1-1.0e-14),100)

#Calcolo f(x) in ogni punto x selezionato
y = createFunction(x)

#Perturbo i dati in input
errorX = np.zeros(len(x))

for i in range(len(x)):
    errorX[i] = x[i] + perturbation
    

#Calcolo f(x) in ogni punto x perturbato
errorY = createFunction(errorX)

#Calcolo dell'errore relativo sui dati in input
relativeErrorX = np.zeros(len(x))

for i in range(len(x)):
    relativeErrorX[i] = abs(x[i]-errorX[i]) / abs(x[i])

#Calcolo dell'errore relativo sull'output
relativeErrorY = np.zeros(len(relativeErrorX))

#Calcolo l'indice di condizionamento della funzione in ogni punto x
k = createK(x)

for i in range(len(y)):
    relativeErrorY[i] = relativeErrorX[i] * k[i]

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
plt.ylabel('error_F')
plt.title('Relative error on the function f(x)= 1 - sqrt(1-x^2)')

errorGraphic = plt.figure(1)
errorGraphic.savefig("funzione.png")

plt.show()