# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:25:21 2020

@author: Leonardo Saccotelli
Content:
    Libreria Algebra Lineare
    Modulo utilizzato per memorizzare gli algoritmi di algebra lineare:
    1) Determinante Laplace
    2) Sostituzione indietro
    3) Sostituzione avanti
    4) Eliminazioni Gauss
    5) Eliminazione Gauss con pivoting
    6) Fattorizzazione LU
"""
import numpy as np

#Metodo di Laplace per il determinante
def determinant(matrix):
    #Ritorna le dimensioni nella lista (r,c) quindi in shape[0] ritorna
    #la lunghezza della riga
    n = matrix.shape[0]
    #Controllo se la matrice è una 1x1
    if n == 1:
        #il determinante coincide con l'unico elemento della matrice
        det = matrix[0, 0]
    else:
        det = 0
        for j in range(1, n + 1):
            #rimuovo la colonna j-1 della matrice, rimuovo la riga 0
            matrix1j = np.delete(np.delete(matrix, j - 1, 1), 0, 0)
            #calcolo il determinante
            det = det + (-1) ** (j + 1) * matrix[0, j - 1] * determinant(matrix1j)
    return det

#Algoritmo di sostituzione all'indietro
def backwardSubstition(matrix, vettb):
    #estrapolo il numero di righe della matrice
    n = matrix.shape[0]

    #inizializzo il vettore delle soluzioni
    x = np.zeros(n)

    #Controllo se il determinante è uguale a zero
    #nel caso il sistema non è risolvibile
    if (abs(np.prod(np.diag(matrix))) < 1.0e-200):
        print(' Matrix could be singular.\n' +
              ' System without solution!')
    else:
        #Calcolo la soluzione immediata
        x[n-1] = vettb[n-1]/matrix[n-1][n-1]
        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1,n):
                s = s + matrix[i][j]*x[j]
            x[i] = (vettb[i]-s)/matrix[i][i]
    #restituisco le soluzioni
    return x

#Algoritmo di sostituzione in avanti
def forwardSubstition(matrix,vettb):
    #estrapolo la dimensione della matrice
    n = matrix.shape[0]

    #Creo il vettore che conterrà l'i-esima soluzione
    x = np.zeros(n)

    #Estrapolo la diagonale, effettuo il prodotto degli elementi sulla diagonale
    #Se il modulo del prodotto è minore di 10^(-18), allora la diagonale è pressochè nulla
    #La matrice è singolare quindi non invertibile
    if(abs(np.prod(np.diag(matrix)))< 1.0e-18):
        print(' Matrix could be singular.\n' +
              ' System without solution!')
    else:
        x[0] = vettb[0]/matrix[0][0]
        for i in range(1, n):
            s = 0
            for j in range(0, i):
                s = s + matrix[i][j]*x[j]
            x[i] = (vettb[i] - s) / matrix[i][i]

    #Restituisco il vettore con le soluzioni
    return x

#Algoritmo di eliminazione di Gauss
def GaussElimination(matrixA, bV):

    #Effettuo una copia dei valori contenuti nei parametri
    matrix = np.copy(matrixA)
    b = np.copy(bV)

    #Ricavo la dimensione della matrice
    n = matrix.shape[0]

    for j in range(0, n):
        for i in range(j+1, n):
            #Calcolo m = matrix[i][j]/matrix[j][j]
            m = matrix[i][j] / matrix[j][j]

            #Azzero l'elemento sotto la diagonale principale
            matrix[i][j] = 0

            #Aggiorno i valori dell'i-esima riga della matrice
            for k in range(j+1, n):
                matrix[i][k] = matrix[i][k] - m * matrix[j][k]
            #Aggiorno i-esimo elemento del vettore dei termini noti
            b[i] = b[i] - m * b[j]
    #Restituisco la matrice triangolare e il vettore dei termini noti
    return matrix, b

#Algoritmo di eliminazione di Gauss con Pivoting
def GaussEliminationPivoting(matrixA, bV):

    #Effettuo una copia dei valori contenuti nei parametri
    matrix = np.copy(matrixA)
    b = np.copy(bV)

    #Ricavo la dimensione della matrice
    n = matrix.shape[0]

    for j in range(0, n):
        #INDIVIDUAZIONE ELEMENTO PIVOT
        pivotMax = abs(matrix[j][j])
        indexPivotMax = j

        for i in range(j+1, n):
            if abs(matrix[i][j]) > pivotMax:
                pivotMax = abs(matrix[i][j])
                indexPivotMax = i

        #SCAMBIO RIGA j CON RIGA indexPivotMax
        if (indexPivotMax > j):
            #Scambio le righe della matrice
            for k in range (j,n):
                Atemp = np.copy(matrix[j][k])
                matrix[j][k] = np.copy(matrix[indexPivotMax][k])
                matrix[indexPivotMax][k] = np.copy(Atemp)
            #Scambio l'ordine del vettore dei termini noti
            btemp = np.copy(b[j])
            b[j] = np.copy(b[indexPivotMax])
            b[indexPivotMax] = np.copy(btemp)

        #ELIMINAZIONE DI GAUSS
        for i in range(j+1, n):
            #Calcolo m = matrix[i][j]/matrix[j][j]
            m = matrix[i][j] / matrix[j][j]

            #Azzero l'elemento sotto la diagonale principale
            matrix[i][j] = 0

            #Aggiorno i valori dell'i-esima riga della matrice
            for k in range(j+1, n):
                matrix[i][k] = matrix[i][k] - m * matrix[j][k]
            #Aggiorno i-esimo elemento del vettore dei termini noti
            b[i] = b[i] - m * b[j]
    #Restituisco la matrice triangolare e il vettore dei termini noti
    return matrix, b

#Fattorizzazione LU
def LUfactorization (matrixA):

    matrix = np.copy(matrixA)
    #dimensione matrice
    n = matrix.shape[0]

    for j in range(0,n-1):
        for i in range(j+1,n):
            #salvo il coeff m per la matrice L
            matrix[i][j] = matrix[i][j]/matrix[j][j]
            #salvo i coeff per la matrice U
            for k in range(j+1, n):
                matrix[i][k] = matrix[i][k] - matrix[i][j]*matrix[j][k]
    return matrix

#Estrapola L
def createMatrixL (matrix):

    #trovo la dimensione della matrice
    n = matrix.shape[0]

    #inizializzo la matrice L
    L = np.zeros((n,n))

    #Salvo sulla diagonale principale 1
    np.fill_diagonal(L, 1)

    #Salvo i coefficienti m nella matrice L
    for j in range(0, n-1):
        for i in range(j+1,n):
            L[i][j] = matrix[i][j]
    return L

#Estrapola U
def createMatrixU (matrix):

    #Creo la matrice U
    U = np.copy(matrix)

    #trovo la dimensione della matrice
    n = U.shape[0]

    for j in range(0, n-1):
        for i in range(j+1,n):
            U[i][j] = 0
    return U

#Fattorizzazione LU con pivoting
def LUpivotingFactorization(matrixA ):

    matrix = np.copy(matrixA)

    #dimensione della matrice
    n = matrix.shape[0]
    #vettore per registrare le permutazioni
    index = np.array([i for i in range(0,n)])

    # Ricavo la dimensione della matrice
    n = matrix.shape[0]

    for j in range(0, n):
        # INDIVIDUAZIONE ELEMENTO PIVOT
        pivotMax = abs(matrix[j][j])
        indexPivotMax = j

        for i in range(j + 1, n):
            if abs(matrix[i][j]) > pivotMax:
                pivotMax = abs(matrix[i][j])
                indexPivotMax = i

        # SCAMBIO RIGA j CON RIGA indexPivotMax
        if (indexPivotMax > j):
            # Scambio le righe della matrice
            for k in range(j, n):
                Atemp = np.copy(matrix[j][k])
                matrix[j][k] = np.copy(matrix[indexPivotMax][k])
                matrix[indexPivotMax][k] = np.copy(Atemp)
            # Scambio l'ordine del vettore degli indici
            temp = np.copy(index[j])
            index[j] = np.copy(index[indexPivotMax])
            index[indexPivotMax] = np.copy(temp)

        # ELIMINAZIONE DI GAUSS
        for i in range(j+1,n):
            #salvo il coeff m per la matrice L
            matrix[i][j] = matrix[i][j]/matrix[j][j]
            #salvo i coeff per la matrice U
            for k in range(j+1, n):
                matrix[i][k] = matrix[i][k] - matrix[i][j]*matrix[j][k]
    # Restituisco la matrice triangolare e il vettore dei termini noti
    return matrix, index

#Funzione per permutare il vettore dei termini noti
def indexPermutation(b, indexVett):
    n = len(b)
    #Creo il vettore b permutato
    newB = np.zeros(n)

    for i in range(0, n):
        newB[i] = b[indexVett[i]]

    return newB

#Metodo iterativo di Gauss-Seidel
def GaussSeidel (matrix, b, x0, eps, k_max):
    #dimensione della matrice
    n = matrix.shape[0]

    #Variabile usata per interrompere il metodo
    stop = False

    #Variabile usata per contare il numero di iterazioni
    k = 0

    #Variabile per memorizzare la soluzione dell'iterazione corrente
    x1 = np.zeros(n)

    while not(stop) and k < k_max:
        for i in range(0, n):
            sum = 0

            for j in range(0, i):
                sum = sum + matrix[i][j] * x0[j]

            for j in range(i+1, n):
                sum = sum + matrix[i][j] * x1[j]

            x1[i] = (b[i] - sum) / matrix[i][i]

        #Controllo sui criteri di arresto

        #Calcolo del residuo
        res =  np.linalg.norm(b - np.dot(matrix, x1)) / np.linalg.norm(b)

        #Calcolo della differenza tra due iterazioni successive
        diff_iter = np.linalg.norm(x1-x0)/np.linalg.norm(x1)

        stop = (res < eps ) and (diff_iter < eps)

        #Incremento il numero di iterazioni eseguite
        k = k + 1

        x0 = np.copy(x1)

    if not(stop):
        print('Process does not converge in %d iterations!' %k)

    return x1, k

#Metodo iterativo di Jacobi
def Jacobi(matrix, b, x0, eps, k_max):
    #dimensione della matrice
    n = matrix.shape[0]

    #Variabile usata per interrompere il metodo
    stop = False

    #Variabile usata per contare il numero di iterazioni
    k = 0

    #Variabile per memorizzare la soluzione dell'iterazione corrente
    x1 = np.zeros(n)

    while not(stop) and k < k_max:
        for i in range(0, n):
            sum = 0

            for j in range(0, n):
                if j != i:
                    sum = sum + matrix[i][j] * x0[j]

            x1[i] = (b[i] - sum) / matrix[i][i]

        #Controllo sui criteri di arresto

        #Calcolo del residuo
        res =  np.linalg.norm(b - np.dot(matrix, x1)) / np.linalg.norm(b)

        #Calcolo della differenza tra due iterazioni successive
        diff_iter = np.linalg.norm(x1-x0)/np.linalg.norm(x1)

        stop = (res < eps ) and (diff_iter < eps)

        #Incremento il numero di iterazioni eseguite
        k = k + 1

        x0 = np.copy(x1)

    if not(stop):
        print('Process does not converge in %d iterations!' %k)

    return x1, k


#Funzione per la creazione della matrice di Hilbert
def hilbertMatrix(n):
    #Creo la matrice
    matrix = np.zeros((n,n))

    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i-1][j-1]= 1/(i+j-1)

    return matrix
