# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:14:24 2020

@author: Leonardo Saccotelli
"""

import numpy as np
import matplotlib.pyplot as plt
import InterpolazionePolinomiale_Algoritmi as IP

def createMyFunction(x):
    y = np.sqrt(x)
    return y

#----------------  DEFINIZIONI DATI DI INTERPOLAZIONE
#Estremo inferiore dell'intervallo da cui estrapolo i nodi
a = 0
#Estremo superiore dell'intervallo da cui estrapolo i nodi
b = 1
#Numero di nodi da estrapolare dall'intervallo [a,b]
n = 60
#Estrapolo n+1 nodi equidistanti dall'intervallo [a,b]
xNodes = np.linspace(a, b, n + 1)
#Calcolo la funzione f(x) = sqrt(x)) negli n+1 nodi
yNodes = createMyFunction(xNodes)

#-------------- COSTRUZIONE POLINOMIO DI INTERPOLAZIONE
#Estrapolo i punti in cui calcolare il polinomio
xPoints = np.linspace(a, b, 10 * len(xNodes) + 1)

#Creo e calcolo il polinomio di Lagrange in ogni punto xPoint
interpolationPolynomial = IP.lagrangeSecondBarycentricFormula(xNodes, yNodes, xPoints)

#Calcolo la funzione in ogni punto xPoints
f_xPoints = createMyFunction(xPoints)

#------------- Grafico del polinomio di interpolazione
plt.figure(1, figsize=(8, 8))
plt.plot(xPoints, f_xPoints, label='f(x)')
p_lab = 'p%d(x)' % n
plt.plot(xPoints, interpolationPolynomial, label=p_lab)
plt.plot(xNodes, yNodes, 'ro')
plt.xlabel('x')
plt.legend(prop={'size': 25})

# Grafico del resto del polinomio di interpolazione
plt.figure(2, figsize=(8, 8))
r_lab = 'R%d(x)' % n
plt.semilogy(xPoints, abs(f_xPoints - interpolationPolynomial), label=r_lab)
plt.xlabel('x')
plt.legend(prop={'size': 25})

plt.show()