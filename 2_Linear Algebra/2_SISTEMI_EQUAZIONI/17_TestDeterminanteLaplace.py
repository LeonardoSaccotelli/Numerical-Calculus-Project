# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:17:42 2020

@author: Leonardo Saccotelli
"""

import numpy as np
import AlgoritmiAlgebraLineare as al
import matplotlib.pyplot as plt
from time import clock

#Testiamo l'algoritmo su matrici di dimensioni comprese tra 1 e 10
print('         ------------------------------------------------')
str1 = 'Matrix dimension'
str2 = 'Execution time'
print('%30s %20s' %(str1,str2))
print('         ------------------------------------------------')

#Numero massimo per la dimensione della matrice
max_n = 10

#Vettore per memorizzare i tempi di esecuzione di ogni determinante
timeDet = np.zeros(max_n)

for n in range(1, max_n+1):
    #popolo la matrice con valori random
    matrix = np.random.random((n, n))
    #Registro l'istante in cui inizia l'esecuzione del determinante
    startDet = clock()
    d = al.determinant(matrix)
    #d = np.linalg.det(matrix)
    #Registro l'istante in cui termina l'esecuzione del determinante
    endDet = clock()
    timeDet[n-1] = (endDet - startDet)

    print('%22d%28e' % (n, timeDet[n-1]))

#Creo un grafico
dimMatrix = np.array([i for i in range(1,max_n+1)])
plt.figure(1)
plt.plot(dimMatrix,timeDet,'r*')
plt.semilogy(dimMatrix,timeDet, 'k')
plt.title('Laplace Method')
plt.xlabel('Matrix dimension')
plt.ylabel('Time execution')
plt.show()