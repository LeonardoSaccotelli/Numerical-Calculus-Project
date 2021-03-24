# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:51:00 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import AlgoritmiAlgebraLineare as al

#Funzione per perturbare il vettore dei termini noti
def perturbation(bvett):

    b = np.copy(bvett)

    n = len(b)

    # Creo un vettore di perturbazioni
    bDelta = np.array([i for i in range(1,n+1)])*10**(-8)

    #bDelta = 0
    #Perturbo il vettore dei termini noti
    for i in range(0, n):
        b[i] = b[i] + bDelta[i]
    return b

#------------------- TEST ELIMINAZIONE DI GAUSS PIVOTING

#Dimensione della matrice
n = 10

#Creo la matrice di Vandermonde
matrix = al.hilbertMatrix(n).astype(float)

#Vettore delle soluzioni
xSol = np.array([i for i in range(1, n+1)])

#Vettore dei termini noti, a cui applico una perturbazione
b = perturbation(np.dot(matrix, xSol))

#b = np.dot(matrix, xSol)

#Calcolo dell'indice di condizionamento del problema
conditionNumber = np.linalg.cond(matrix,1 )
# ------ APPLICO GAUSS CON PIVOTING

#Creo la matrice triangolare superiore
matrix, b = al.GaussEliminationPivoting(matrix, b)

#Calcolo le soluzioni tramite la backwardSubstition
xFind = al.backwardSubstition(matrix, b)

#Calcolo l'errore relativo sulla struttura
#applicando la norma 2
xError = np.linalg.norm((xSol - xFind), 2)


# ------- PRINT RESULT GAUSS ELIMANTION WITH PIVOTING

print('\n Gaussian elimination with Pivoting: Test on Hilbert matrix')
print(' -----------------------------------------------------------------')
for i in range(n):
    print('   xFind[%2d] = %24.16f    xSol[%2d] = %5.3f' % (i, xFind[i], i, xSol[i]))

print(' -----------------------------------------------------------------')
print('   Difference ||xFind-xSol|| = %e' %xError)
print('   Matrix condition number   = %e' %conditionNumber )
