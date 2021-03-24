# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:30:12 2020

@author: Leonardo Saccotelli
"""
import numpy as np
import matplotlib.pyplot as plt
import InterpolazionePolinomiale_Algoritmi as IP

def createMyFunction(x):
    y = 1/(1+x**2)
    return y

#----------------  DEFINIZIONI DATI DI INTERPOLAZIONE
#Estremo inferiore dell'intervallo da cui estrapolo i nodi
a = -1
#Estremo superiore dell'intervallo da cui estrapolo i nodi
b = 1

#Numero di nodi da estrapolare dall'intervallo [a,b]
n = 40

#Estrapolo n+1 nodi equidistanti dall'intervallo [a,b]
xEquidistantNodes = np.linspace(a, b, n + 1)

#Calcolo la funzione f(x) negli n+1 nodi equidistanti
yEquidistantNodes = createMyFunction(xEquidistantNodes)

#Estrapolo n+1 nodi di Chebyshev dall'intervallo [a,b]
xChebyshevNodes = IP.createChebyshevNodes(a, b, n)

#Calcolo la funzione f(x) negli n+1 nodi di Chebyshev
yChebyshevNodes = createMyFunction(xChebyshevNodes)

#Estrapolo i punti in cui calcolare il polinomio
xPoints = np.linspace(a, b, 10 * len(xEquidistantNodes) + 1)

#Creo e calcolo il polinomio con la formula di Newton in ogni punto xPoint
pol_Equi_Newton = IP.NewtonPolynomialInterpolation(xEquidistantNodes, yEquidistantNodes, xPoints)

#Creo e calcolo il polinomio con la formula di Newton in ogni punto xPoint
pol_Chebyshev_Newton = IP.NewtonPolynomialInterpolation(xChebyshevNodes, yChebyshevNodes, xPoints)

#Calcolo la funzione in ogni punto xPoints
f_xPoints = createMyFunction(xPoints)


#------------- Grafico del polinomio di interpolazione con nodi equidistanti
plt.figure(1, figsize=(12, 12))
plt.plot(xPoints, f_xPoints, label='F(x) = 1/(1+x^2)')

p_lab = 'Newton: %d nodi equidistanti' % n
plt.plot(xPoints, pol_Equi_Newton, label=p_lab)

plt.plot(xEquidistantNodes, yEquidistantNodes, 'ro')
plt.xlabel('x')
plt.legend(prop={'size': 20}, loc ='best')

#------------- Grafico del polinomio di interpolazione con nodi di Chebyshev
plt.figure(2, figsize=(12, 12))
plt.plot(xPoints, f_xPoints, label='F(x) = 1/(1+x^2)')

p_lab = 'Newton: %d nodi di Chebyshev' % n
plt.plot(xPoints, pol_Chebyshev_Newton, label=p_lab)

plt.plot(xEquidistantNodes, yEquidistantNodes, 'ro')
plt.xlabel('x')
plt.legend(prop={'size': 20}, loc ='best')


#----------------Grafico del resto del polinomio di interpolazione 
plt.figure(3, figsize=(12, 12))

r_lab = 'Nodi Equidistanti: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_Equi_Newton), label=r_lab)

r_lab = 'Nodi Chebyshev: %d nodi' % n
plt.semilogy(xPoints, abs(f_xPoints - pol_Chebyshev_Newton), label=r_lab)

plt.xlabel('x')

plt.legend(prop={'size': 20}, loc ='best')

plt.show()

