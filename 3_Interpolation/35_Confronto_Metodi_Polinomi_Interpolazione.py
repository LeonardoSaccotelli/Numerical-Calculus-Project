# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:24:02 2020

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
n = 50
#Estrapolo n+1 nodi equidistanti dall'intervallo [a,b]
xNodes = np.linspace(a, b, n + 1)
#Calcolo la funzione f(x) = sin(x) negli n+1 nodi
yNodes = createMyFunction(xNodes)


#-------------- COSTRUZIONE POLINOMIO DI INTERPOLAZIONE
#Estrapolo i punti in cui calcolare il polinomio
xPoints = np.linspace(a, b, 20 * len(xNodes) + 1)

#Creo e calcolo il polinomio con il metodo dei coefficienti indeterminati
pol_coeff_indet = IP.indeterminateCoefficientFormula(xNodes, yNodes, xPoints)

#Creo e calcolo il polinomio con la prima formula baricentrica di Lagrange in ogni punto xPoint
pol_1_Lagrange = IP.lagrangeFirstBarycentricFormula(xNodes, yNodes, xPoints)

#Creo e calcolo il polinomio con la seconda formula baricentrica di Lagrange in ogni punto xPoint
pol_2_Lagrange = IP.lagrangeSecondBarycentricFormula(xNodes, yNodes, xPoints)

#Creo e calcolo il polinomio con la formula di Newton in ogni punto xPoint
pol_Newton = IP.NewtonPolynomialInterpolation(xNodes, yNodes, xPoints)

#Calcolo la funzione in ogni punto xPoints
f_xPoints = createMyFunction(xPoints)

#------------- Grafico del polinomio di interpolazione
plt.figure(1, figsize=(12, 12))
plt.plot(xPoints, f_xPoints, label='F(x) = Sqrt(x)')

p_lab = 'Coeff Indet: %d nodi' % n
plt.plot(xPoints, pol_coeff_indet, label=p_lab)

p_lab = 'Lagrange_1: %d nodi' % n
plt.plot(xPoints, pol_1_Lagrange, label=p_lab)

p_lab = 'Lagrange_2: %d nodi' % n
plt.plot(xPoints, pol_2_Lagrange, label=p_lab)

p_lab = 'Newton: %d nodi' % n
plt.plot(xPoints, pol_Newton, label=p_lab)

plt.plot(xNodes, yNodes, 'ro')
plt.xlabel('x')
plt.legend(prop={'size': 20}, loc ='best')

#----------------Grafico del resto del polinomio di interpolazione
plt.figure(2, figsize=(12, 12))

r_lab = 'Coeff Indet: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_coeff_indet), label=r_lab)

r_lab = 'Lagrange_1: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_1_Lagrange), label=r_lab)

r_lab = 'Lagrange_2: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_2_Lagrange), label=r_lab)

r_lab = 'Newton: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_Newton), label=r_lab)

plt.xlabel('x')

plt.legend(prop={'size': 20}, loc ='best')

plt.show()


