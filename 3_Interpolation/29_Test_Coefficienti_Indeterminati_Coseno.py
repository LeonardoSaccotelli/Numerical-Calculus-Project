# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:02:10 2020

@author: leonardo Saccotello
"""

import numpy as np
import matplotlib.pyplot as plt
import InterpolazionePolinomiale_Algoritmi as IP

#Funzione per il calcolo di f(x) = cos(x)
def createCos(x):
    y = np.cos(x)
    return y
    

#---------------------------------------------     DATI DI INTERPOLAZIONE
#Estremo inferiore dell'intervallo
a = 0
#Estremo superiore dell'intervallo
b = 6*np.pi
#Numero di nodi da estrapolare dall'intervallo [a,b]
n = 40

#Estrapolo n+1 nodi equidistanti dall'intervallo [a,b]
xNodes = np.linspace(a,b,n+1)

#Calolo la funzione f(x)=cos(x) in tutti i nodi xNodes
yNodes = createCos(xNodes)

#Ordine di grandezza della perturbazione
perturbationGrades = 1.0e-3

#Sommo le perturbazioni ai valori di yNodes (Perturbo le ordinate)
perturbationYNodes = yNodes + (np.random.rand(n+1)*2-1)*perturbationGrades

#-----------------------------------------------------------------------------------
#
#
#
#-------------------------------- METODO DEI COEFFICIENTI INDETERMINATI 
#-------------------------------- COSTRUZIONE E CALCOLO DEL POLINOMIO


#Estrapoliamo 10*(n+1) + 1 punti equidistanti in cui calcolare il polinomio
xPoints = np.linspace(a, b, 50*len(xNodes) + 1)

#Calcolo il polinomio di interpolazione sui coefficienti non perturbati nei punti xPoints
interpolationPol = IP.indeterminateCoefficientFormula(xNodes, yNodes, xPoints)

#Calcolo il polinomio di interpolazione sui coefficienti perturbati nei punti xPoints
pertInterpolationPol = IP.indeterminateCoefficientFormula(xNodes, perturbationYNodes, xPoints)

#Calcoliamo f(x) = cos(x) nei punti xPoints
f_xPoints = createCos(xPoints)

#---------------------------------Rappresentazione grafica dei risultati
plt.figure(0,figsize=(8,8))
#Stampo il grafico di f(x) = cos(x)
plt.plot(xPoints, f_xPoints, label = 'f(x)') 


p_lab = 'p%d(x)' % n
#Stampo il grafico del polinomio di interpolazione con coeff non perturbati
plt.plot(xPoints, interpolationPol, label = p_lab) 

p_lab = 'Pert%d(x)' % n
#Stampo il grafico del polinomio di interpolazione con coeff perturbati
plt.plot(xPoints, pertInterpolationPol, label=p_lab)

#Stampo i nodi di interpolazione
plt.plot(xNodes, yNodes,'ro')
plt.legend(prop={'size': 25})


#--------------------------------------Rappresentazione grafica del resto
plt.figure(1,figsize=(8,8))
r_lab = 'R%d(x)' % n
#Stampo l'errore commesso nell'approssimare F con il polinomio con coeff non perturbati
plt.semilogy(xPoints, abs(f_xPoints - interpolationPol), label=r_lab)


r_lab = 'RPert%d(x)' % n
#Stampo l'errore commesso nell'approssimare F con il polinomio con coeff perturbati
plt.semilogy(xPoints, abs(f_xPoints - pertInterpolationPol),label=r_lab)

plt.legend(prop={'size': 25})
plt.rcParams.update({'font.size': 28})
plt.show()