# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:08:24 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import AlgoritmiAlgebraLineare as al


#------------------- TEST MEDOTO DI ELIMINAZIONE DI GAUSS CON PIVOTING

#Dimensione della matrice
n = 5000

#Creo la matrice
matrix = np.random.random((n, n)).astype(float)

#Vettore delle soluzioni
xSol = np.array([i for i in range(1,n+1)])

#Vettore dei termini noti
b = np.dot(matrix, xSol)

# ------ APPLICO GLI ALGORITMI a matrix e b

#Creo la matrice triangolare superiore
matrix, b = al.GaussEliminationPivoting(matrix, b)

#Calcolo le soluzioni tramite la backwardSubstition
xFind = al.backwardSubstition(matrix, b)

#Calcolo l'errore relativo sulla struttura
#applicando la norma 2
xError = np.linalg.norm((xSol - xFind), 2)

#Calcolo dell'indice di condizionamento del problema
conditionNumber = np.linalg.cond(matrix,1 )

#Stampo la matrice triangolare superiore
print(' Gaussian elimination with pivoting')
print(' ------------------------------------------------------------')
for i in range(n):
    print('   xFind[%2d] = %18.16f xSol[%2d] = %5.3f' % (i, xFind[i], i, xSol[i]))

print(' ------------------------------------------------------------')
print('   Difference ||xFind-xSol|| = %e\n' %xError)
print('   Matrix condition number   = %e' %conditionNumber )
