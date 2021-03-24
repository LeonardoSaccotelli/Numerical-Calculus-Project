# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:30:32 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import AlgoritmiAlgebraLineare as al


# -------- Test del metodo di sostituzione in avanti ------

print('\n  TESTING FORWARD SUBSTITION')
print('  -------------------------------------')
print('  Dimension: 5x5')
matrix = np.array([[1, 0, 0, 0, 0],
                   [5, 1, 0, 0, 0],
                   [6, 1, 2, 0, 0],
                   [4, 2, 6, 5, 0],
                   [1, 1, 3, 5, 2]])

#Fisso ad uno le soluzioni del sistema
xsol = np.ones(5)
#Calcolo il vettore dei termini noti
b = np.dot(matrix,xsol)

#Applico forwardSubstition a matrix e b e mi aspetto
#di ritrovare xsol
findSol = al.forwardSubstition(matrix, b)
print('  Solution of linear system:\n ', findSol)



print('\n  TESTING FORWARD SUBSTITION')
print('  -------------------------------------')
print('  Dimension: 50x50')

#Dimensione matrice
n = 50
M = 10

#Creo una matrice 50x50 con valori compresi tra 0 e 20
matrix = np.random.random((n, n))*2*M

#converto in float tipo dei coefficienti
matrix = matrix.astype(float)

#trasformo la matrice in una matrice triangolare INFERIORE
matrix = np.tril(matrix)

#Fisso ad 1 la soluzione
xs = np.ones(n)

#Calcolo il vettore dei termini noti
b = np.dot(matrix, xs)

#Applico l'algoritmo di sostituzione  in avanti e controllo
#se le x restituite dall'algoritmo coincidono con quelle fissate
findSol = al.forwardSubstition(matrix, b)
print('  Solution of linear system:\n ', findSol)


