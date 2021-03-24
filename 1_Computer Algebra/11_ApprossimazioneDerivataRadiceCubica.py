# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:07:14 2020

@author: leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt

#Definizione della funzione f(x) = x^(1/3) di cui si vuole calcolare la derivata
def f(x):
    function = np.power(x,1/3)
    return function

#Definizione della derivata prima della funzione f(x) = x^(1/3)
def f1(x) :
    derivative = 1/(3*(np.power(x,2/3)))
    return derivative

def createTable():
    str1 = 'h'
    str2 = 'Derivative'
    str3 = 'Approximation'
    str4 = 'Error'
    print(' --------------------------------------------------------------')
    print('|                  Derivative approximation                    |')   
    print(' --------------------------------------------------------------')
    print('   %6s%21s %15s%13s' %(str1,str2,str3,str4))
    print(' --------------------------------------------------------------')



#Punto in cui effettuare l'esperimento e valore derivata
x = 4

#Calcolo la derivata prima nel punto x scelto
df = f1(x)

# Sequenza di passi di grandezza decrescente (Calcolo h via via più piccolo)
h = 2.0**(-np.array(range(50)))

# Approssimazione della derivata
Err = np.zeros(len(h))

createTable()

for i in range(len(h)):
    
    #Calcolo dell'approssimazione della derivata
    dfh = (f(x+h[i]) - f(x))/h[i]
    
    #Calcolo dell'errore totale commesso dall'approssimazione
    Err[i] = np.abs(df - dfh)/np.abs(df)
    print(' %13e  %14.8f  %13.8f  %15e ' % (h[i],df,dfh,Err[i]))
    
#calcolo dell'errore di discretizzazione  attraverso f''(x) 
discretizationError = abs(-2/(9*np.power(x,5/3)))*h/2

    
#Rappresentazione grafica, rappresentiamo l'errore totale e l'errore di 
#discretizzazione
plt.figure(1,figsize=(14,7))
plt.loglog(h,discretizationError)
plt.loglog(h,Err,'*-r')
plt.xlabel('h')
plt.ylabel('Error')
plt.savefig("rad3.png")
plt.show()