# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:42:27 2020

@author: Leonardo Saccotelli
    
    Content:
        Libreria contenente gli algorimti per l'interpolazione polinomiale
"""
import numpy as np

"""------------------------------------------------
    METODO DEI COEFFICIENTI INDETERMINATI
   ------------------------------------------------"""
#Funzione per la creazione della matrice di Vandermonde dei termini noti
def createVandermonde(value):
    
    #Calcolo la dimensione della matrice
    n = len(value)
    
    #Creo la matrice
    vandermondeMatrix = np.zeros((n,n))
        
    #Inizializzo la matrice
    for i in range(n):
        for j in range(n):
            vandermondeMatrix[i][j] = value[i]**j
    
    return vandermondeMatrix

#Funzione per il calcolo del polinomio di intepolazione con il metodo
#dei coefficienti indeterminati    
def indeterminateCoefficientFormula(xNodes, yNodes, xPoints):
    #Creo la matrice di Vandermonde partendo da xNodes
    vandermondeMatrix = createVandermonde(xNodes).astype(float)
    
    #Risolvo il sistema lineare dato dalla matrice di Vandermonde e il vettore dei 
    #termini noti yNodes per trovare i coefficienti
    coefficient  = np.linalg.solve(vandermondeMatrix, yNodes)
    
    #Calcolo il polinomio di interpolazione sui coefficienti non perturbati 
    #nei punti xPoints
    interpolationPolynomial = np.polyval(np.flipud(coefficient), xPoints)
       
    return interpolationPolynomial
    

"""------------------------------------------------
        PRIMA FORMULA BARICENTRICA DI LAGRANGE
   ------------------------------------------------"""
#Funzione per calcolare il polinomio di Lagrange (formula 1) in un insieme di punti x
def lagrangeFirstBarycentricFormula(xNodes, yNodes, xPoints):
    # Cacolo dei coefficienti formula baricentrica
    z = Z_Coeff(xNodes, yNodes)

    # Calcolo poliniomio di interpolazione nei punti di x
    p = np.zeros(len(xPoints))
    
    for i in range(len(xPoints)):
        p[i] = ComputeLagrange_1(xPoints[i], xNodes, z, yNodes)

    return p


# Routine per il cacolo coefficienti Zj formula baricentrica
def Z_Coeff(xNodes, yNodes):
    #Determino il numero di nodi di interpolazione
    n = len(xNodes)

    #Creo la matrice identità di dimensione n x n
    X = np.eye(n)

    #Calcolo PROD[(Xj - Xk)] PER K = 0 .... N, CON K != J
    for i in range(n):
        for j in range(n):
            #Calcolo le differenze (Xj - Xk) con j != k
            if j > i:
                X[i, j] = xNodes[i] - xNodes[j]
            elif j < i:
                X[i, j] = -X[j, i]
    #Creo il vettore Z per memorizzare i coeff Zj
    z = np.zeros(n)
    for j in range(n):
        #Calcolo i coefficienti Zj = Yj / PROD[(Xj - Xk)] PER K = 0 .... N, CON K != J
        z[j] = yNodes[j] / np.prod(X[j, :])
    return z

#Calcolo del polinomio in un singolo punto x
def ComputeLagrange_1(xPoints, xNodes, z, yNodes):
    #Verifico che la distanza fra il punto x in cui voglio calcolare il polinomio e i 
    #valori dei nodi usati sia minore di 10^-14. 
    #Se questo è vero, vuol dire che stiamo calcolando il polinomio in uno dei nodi
    #di interpolazione. 
    #In questo caso è noto il valore assunto dal polinomio nei nodi di interpolazione.
    check_nodes = abs(xPoints - xNodes) < 1.0e-14
    if True in check_nodes:
        #Salvo il punto x che coincide con il nodo
        temp = np.where(check_nodes == True)
        #Salvo il suo valore in una variabile i
        i = temp[0][0]
        #Uso i come indice per ricavare il valore associato al xNodes
        #in cui vogliamo calcolare il polinomio, valore che è già noto.
        p = yNodes[i]
    else:
        #Ricavo il numero di nodi
        n = len(xNodes)
        S = 0
        #Calcolo la sommatoria per j = 0...n di (Zj/(x-xNodes[j])
        for j in range(n):
            S = S + z[j] / (xPoints - xNodes[j])
        #Moltiplico la sommatoria per PROD(x - xNodes) k = 0 ... n
        p = np.prod(xPoints - xNodes) * S
    return p   

 
"""------------------------------------------------
        SECONDA FORMULA BARICENTRICA DI LAGRANGE
   ------------------------------------------------"""
#Funzione per calcolare il polinomio di Lagrange (formula 2) in un insieme di punti x
def lagrangeSecondBarycentricFormula(xNodes, yNodes, xPoints):
    # Cacolo dei coefficienti formula baricentrica
    lambdaCoeff = Lambda_Coeff(xNodes)

    # Calcolo poliniomio di interpolazione nei punti di x
    p = np.zeros(len(xPoints))
    
    for i in range(len(xPoints)):
        p[i] = ComputeLagrange_2(xPoints[i], xNodes, lambdaCoeff, yNodes)

    return p

#Routine per il cacolo coefficienti LambdaJ formula baricentrica
def Lambda_Coeff(xNodes):
    #Determino il numero di nodi di interpolazione
    n = len(xNodes)

    #Creo la matrice identità di dimensione n x n
    X = np.eye(n)

    #Calcolo PROD[(Xj - Xk)] PER K = 0 .... N, CON K != J
    for i in range(n):
        for j in range(n):
            #Calcolo le differenze (Xj - Xk) con j != k
            if j > i:
                X[i, j] = xNodes[i] - xNodes[j]
            elif j < i:
                X[i, j] = -X[j, i]
    #Creo il vettore lambda per memorizzare i coeff Lambdaj
    Lambda_j = np.zeros(n)
    for j in range(n):
        #Calcolo i coefficienti Zj = Yj / PROD[(Xj - Xk)] PER K = 0 .... N, CON K != J
        Lambda_j[j] = 1 / np.prod(X[j, :])
    return Lambda_j

#Calcolo del polinomio in un singolo punto x
def ComputeLagrange_2(xPoints, xNodes, lam, yNodes):
    #Verifico che la distanza fra il punto x in cui voglio calcolare il polinomio e i valori dei nodi usati
    #sia minore di 10^-14. Se questo è vero, vuol dire che stiamo calcolando il polinomio in uno dei nodi
    #di interpolazione. In questo caso è noto il valore assunto dal polinomio nei nodi di interpolazione.
    check_nodes = abs(xPoints - xNodes) < 1.0e-14
    if True in check_nodes:
        #Salvo il punto x che coincide con il nodo
        temp = np.where(check_nodes == True)
        #Salvo il suo valore in una variabile i
        i = temp[0][0]
        #Uso i come indice per ricavare il valore associato al xNodes
        #in cui vogliamo calcolare il polinomio, valore che è già noto.
        p = yNodes[i]
    else:
        #Ricavo il numero di nodi
        n = len(xNodes)
        S_Num = 0
        S_Den = 0
        #Calcolo la sommatoria per j = 0...n di (Zj/(x-xNodes[j])
        for j in range(n):
            S_Num = S_Num + ((lam[j] / (xPoints - xNodes[j]))*yNodes[j])
            S_Den = S_Den + (lam[j] / (xPoints - xNodes[j]))
        p = S_Num/S_Den
    return p


 
"""------------------------------------------------
    INTERPOLAZIONE DI NEWTON ALLE DIFFERENZE DIVISE
   ------------------------------------------------"""

#Algorimto per il calcolo delle differenze divise di f sui nodi x
def differenceDivision (x, y):
    #Creo una copia dei nodi di interpolazione
    #e dei valori associati ai nodi di interpolazione
    xNodes = np.copy(x)
    diagonalCoeff = np.copy(y)

    #Determino il numero dei nodi
    n = len(xNodes)
    #Parto dalla prima colonna sino all'ultima colonna
    for j in range(0, n):
        #Parto dall'ultima riga sino all'elemento sulla diagonale
        for i in range(n-1, j, -1):
            #Calcolo la differenza divisa
            diagonalCoeff[i] = (diagonalCoeff[i]- diagonalCoeff[i-1])/(xNodes[i]-xNodes[i-j-1])
    return diagonalCoeff


#Funzione per il calcolo del Polinomio di interpolazione di Newton
#alle differenze divise in un insieme di punti x
def NewtonPolynomialInterpolation(xNodes, yNodes, xPoints):
    #Determino il numero di punti in cui calcolare la funzione
    n = len(xPoints)
    
    #Determino i coeffiecienti del polinomio di interpolazione
    #attraverso le differenze divise
    coeff = differenceDivision(xNodes, yNodes)

    #Creo il vettore che conterrà il
    #valore assunto dal polinomio nei punti xPoints
    p = np.zeros(n)

    #Calcolo il valore assunto dal polinomio in ogni punto
    for i in range(len(xPoints)):
        p[i] = ComputeNewton(xNodes, coeff, xPoints[i])

    return p

#Funzione per calcolare il polinomio in un singolo punto x
def ComputeNewton(xNodes, coeff, xPoint):
    #Numero di nodi
    n = len(xNodes)
    #Salvo l'ultima differenza divisa
    p = coeff[n-1]
    #Calcolo il polinomio nel punto x
    for i in range(n-2, -1, -1):
        p = p *(xPoint - xNodes[i]) + coeff[i]
    return p


"""------------------------------------------------
        CREAZIONE NODI DI CHEBYSHEV
   ------------------------------------------------"""
def createChebyshevNodes(a, b, n):
    k = np.array(range(n, -1, -1))
    t = np.cos((2*k+1)*np.pi/2/(n+1))
    xNodes = (a+b)/2 + (b-a)/2*t
    return xNodes
   