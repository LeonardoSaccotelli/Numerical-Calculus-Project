# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:12:46 2020

@author: Leonardo Saccotelli

    Content:
        Nel seguente programma vogliamo mettere a confronto i tempi di esecuzione
        dei vari metodi diretti e iterativi per risolvere un sistema lineare.
        In particolare varieremo la dimensione della matrice registrando di volta in volta
        il tempo richiesto per risolverlo dai vari algoritmi
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import AlgoritmiAlgebraLineare as AL


def createMatrix(n):
    #Costante da utilizzare sulla diagonale della matrice
    c = 50
    e1 = np.ones(n - 1)
    matrix = np.diag(e1, -1) - c * np.eye(n) + np.diag(e1, 1)

    return matrix

#Funzione per cronometrare i tempi per l'esecuzione dell'algoritmo di GaussSeidel
def timeGaussSeidel(matrix, b1, x0, eps, k_max, xSol):

    A = np.copy(matrix)

    b = np.copy(b1)

    #Avvio il cronometro
    start = time.time()

    xFind, k = AL.GaussSeidel(A, b, x0, eps, k_max)

    #Fermo il cronomtro
    end = time.time()

    #Calcolo il tempo di esecuzione
    timeDiff = end - start

    #Calcolo l'errore commesso
    errX = np.linalg.norm(xSol - xFind)

    return timeDiff, errX

#Funzione per cronometrare i tempi per l'esecuzione dell'algoritmo di GaussSeidel
def timeJacobi(matrix, b1, x0, eps, k_max, xSol):

    A = np.copy(matrix)

    b = np.copy(b1)

    #Avvio il cronometro
    start = time.time()

    xFind, k = AL.Jacobi(A, b, x0, eps, k_max)

    #Fermo il cronomtro
    end = time.time()

    #Calcolo il tempo di esecuzione
    timeDiff = end - start

    #Calcolo l'errore commesso
    errX = np.linalg.norm(xSol - xFind)
    
    return timeDiff, errX

#Numero massimo di iterazioni
k_max = 100

#Tolleranza dell'errore ammessa
eps = 1.0e-6

#Fisso un range della dimensione della matrice, in particolare
#partiamo da una matrice di 1000 fino ad una matrice di 10000
#incrementando di 250 la dimensione
n_matrix = range(1000, 10000, 200 )

#Vettore utilizzato per memorizzare il tempo di esecuzione
#del metodo di Gauss-Seidel al variare della dimensione della matrice
executionGaussSeidelTime = np.zeros(len(n_matrix))

#Vettore utilizzato per memorizzare il tempo di esecuzione
#del metodo di Jacobi al variare della dimensione della matrice
executionJacobiTime = np.zeros(len(n_matrix))

#Vettore utilizzato per memorizzare l'errore commesso
#con l'algortimo di Gauss-Seidel
errorGaussSeidel = np.zeros(len(n_matrix))

#Vettore utilizzato per memorizzare l'errore commesso
#con l'algortimo di Jacobi
errorJacobi = np.zeros(len(n_matrix))


#indice usato per la gestione dei vettore dei tempi e degli errori
i = 0

for n in n_matrix:

    #Creo la matrice
    matrix = createMatrix(n)

    #Fisso la soluzione del sistema
    x_sol = np.array([i for i in range(1,n+1)])

    #Calcolo il vettore dei termini noti
    b = np.dot(matrix, x_sol)

    #Fisso la prima approssimazione da utilizzare
    #nei metodi iterativi
    x0 = 2 * np.random.rand(n) - 1

    #Registro il tempo di Gauss-Seidel
    executionGaussSeidelTime[i], errorGaussSeidel[i] = timeGaussSeidel(matrix, b, x0, eps, k_max, x_sol)

    #Registro il tempo di Jacobi
    executionJacobiTime[i], errorJacobi[i] = timeJacobi(matrix, b, x0, eps, k_max, x_sol)

    #Incremento l'indice dei cronometri
    i = i + 1


# ------- CREO I GRAFICI DEI CRONOMETRI
plt.figure(1, figsize = (10, 10))
plt.title('Direct method vs Iterative method: Time')

plt.grid(True)

plt.plot(n_matrix, executionGaussSeidelTime)
plt.semilogy(n_matrix, executionGaussSeidelTime,'bo-', label = 'Gauss-Seidel method')

plt.plot(n_matrix, executionJacobiTime)
plt.semilogy(n_matrix, executionJacobiTime,'ro-', label = 'Jacobi method')

plt.xlabel('Matrix dimension');
plt.ylabel('Execution time')
plt.legend(loc = 'best')


# ------------- CREO IL GRAFICO DELL'ERRORE
plt.figure(2, figsize=(10,10))
plt.title('Direct method vs Iterative method: Error')

#plt.plot(n_matrix, errorGauss)
#plt.loglog(n_matrix, errorGauss,'b', label = 'Gauss elimination')

#plt.plot(n_matrix, errorGaussPivoting)
#plt.loglog(n_matrix, errorGaussPivoting,'y', label = 'Gauss elimination pivoting')

plt.grid(True)

plt.plot(n_matrix, errorGaussSeidel)
plt.semilogy(n_matrix, errorGaussSeidel, 'bo-', label = 'Gauss-Seidel method')

plt.plot(n_matrix, errorJacobi)
plt.semilogy(n_matrix, errorJacobi,'ro-', label = 'Jacobi method'  )

plt.xlabel('Matrix dimension');
plt.ylabel('Error ||x_sol - x_find||')
plt.legend(loc = 'best')

plt.show()
