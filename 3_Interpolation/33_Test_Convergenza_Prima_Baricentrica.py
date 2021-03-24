# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:21:35 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt
import InterpolazionePolinomiale_Algoritmi as IP

# Funzione da interpolare
def createMyFunction(x):
    y = 1/(1+x**2)
    return y

# Definzione intervallo di interpolazione
a = -1
b = 1

# Calcolo della funzione in un insieme di punti
xPoints = np.linspace(a, b, 200)
f_xPoints = createMyFunction(xPoints)

# Grado massimo del polinomio di interpolazione
n_max_nodes = 60

R = np.zeros(n_max_nodes)

for n in range(n_max_nodes):
    
    # Calcolo nodi e valori associati ai nodi
    xNodes = np.linspace(a, b, n + 1)
    yNodes = createMyFunction(xNodes)

    # Calcolo il polinomio di interpolazione
    interpolationPolynomial = IP.lagrangeFirstBarycentricFormula(xNodes, yNodes, xPoints)
    # Calcolo resto polinomio di grado n
    R[n] = max(abs(f_xPoints - interpolationPolynomial))

# Rappresentazione grafica dei risultati
plt.figure(1, figsize=(8, 8))
plt.semilogy(range(n_max_nodes), R, label='max|R(x)|')
plt.xlabel('n')
plt.legend()
plt.show()

