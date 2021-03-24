# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 02:33:21 2020

@author: Leonardo Saccotelli
        
        Test fattorizzazione A = LU
"""

import numpy as np
import AlgoritmiAlgebraLineare as myLA
from fractions import Fraction

def printMatrix(matrix, header):
    #Ricavo la dimensione della matrice
    n = matrix.shape[0]
    print('  ' + header)
    
    for i in range(0, n):
        for j in range (0, n):
            #Stampo un numero razionale sotto forma di frazione
            matrixF = Fraction(matrix[i,j]).limit_denominator()
            print('  %7s ' %matrixF ,end=' ')  
        print(' ')
    



#Creo una matrice test da fattorizzare    
A = np.array([[1,-3,2,4], \
              [1, 6, -3, 7] , \
              [-1, 9, 4, 2], \
              [4,-4,-2,5 ]
             ]).astype(float)

#Fattorizzo la matrice in A = LU
LU = myLA.LUfactorization(A)

#Estrapolo la matrice triangolare inferiore
L = myLA.createMatrixL(LU)

#Estrapolo la matrice triangolare superiore
U = myLA.createMatrixU(LU)

#Calcolo l'errore commesso nella fattorizzazione
errorLU = np.linalg.norm(np.dot(L,U) - A)

print(' ---------------------------------------------')
print('|             A = LU DECOMPOSITION            |')
print(' ---------------------------------------------')

printMatrix(A, ' Matrix: A' )
print(' ---------------------------------------------')

printMatrix(LU, ' Matrix: LU' )
print(' ---------------------------------------------')

printMatrix(L, ' Matrix: L' )
print(' ---------------------------------------------')

printMatrix(U, ' Matrix: U' )
print(' ---------------------------------------------')

print('   Difference ||LU - A|| = %e' % errorLU)





