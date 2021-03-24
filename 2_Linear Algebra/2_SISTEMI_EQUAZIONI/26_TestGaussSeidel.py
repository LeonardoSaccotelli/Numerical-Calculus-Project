# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:27:17 2020

@author: Leonardo Saccotelli

        Test metodo di Gauss - Seidel
        --------------------------------------------------------------
        Nel seguente test risolviamo matrici di varie dimensioni
        Raccogliamo due diverse informazioni:
            1) I tempi di esecuzione al variare della dimensione
            2) Il numero di ierazioni al variare della dimensione
        
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import AlgoritmiAlgebraLineare as AL

#Numero massimo di iterazioni 
k_max = 100

#Tolleranza dell'errore ammessa
eps = 1.0e-6

#Fisso un range della dimensione della matrice, in particolare 
#partiamo da una matrice di 100 fino ad una matrice di 1000 al passo di 50
n_matrix = range(100, 2000, 50)

#Vettore utilizzato per memorizzare il numero di iterazioni eseguite al
#variare della dimensione della matrice
count_GS= np.zeros(len(n_matrix))

#Vettore utilizzato per memorizzare il tempo di esecuzione al
#variare della dimensione della matrice
executionTime = np.zeros(len(n_matrix))

#indice usato per la gestione dei vettore count_GS, executionTime
i = 0

for n in n_matrix:

    # ----- COSTRUZIONE DELLA MATRICE TEST 
    #Costante da utilizzare sulla diagonale della matrice
    c = 4
    
    e1 = np.ones(n - 1)
    matrix = np.diag(e1, -1) - c * np.eye(n) + np.diag(e1, 1)
    
    #Fisso il vettore delle soluzioni 
    xsol = np.ones(n)
    
    #Calcolo il vettore dei termini noti
    b = np.dot(matrix, xsol)

    #Fisso la prima approssimazione da utilizzare da Gauss - Seidel
    x0 = 2 * np.random.rand(n) - 1

    iteration = 2
    
    #Avvio il cronometro
    startGS = time.time()
    
    for r in range(iteration):
        #Eseguo Gauss Seidel
        x_find, k = AL.GaussSeidel(matrix, b, x0, eps, k_max)
    
    #Fermo il cronometro
    stopGS = time.time()
    
    #Calcolo i tempi di esecuzione
    timeGS = (stopGS - startGS) / iteration
    
    #Salvo le informazioni
    count_GS[i] = k
    executionTime[i] = timeGS

    i = i + 1

#------ CREO IL GRAFICO DEL NUMERO DI ITERAZIONI
plt.figure(1)
plt.plot(n_matrix, count_GS, 'r*')
plt.xlabel('Matrix dimension');
plt.ylabel('Number of iteration')
plt.title('C = 4')

#----- CREO IL GRAFICO DEI TEMPI DI ESECUZIONE
plt.figure(2)
plt.plot(n_matrix, executionTime)
plt.semilogy(n_matrix, executionTime)
plt.xlabel('Matrix dimension');
plt.ylabel('Execution time')
plt.title('C = 4')
plt.show()