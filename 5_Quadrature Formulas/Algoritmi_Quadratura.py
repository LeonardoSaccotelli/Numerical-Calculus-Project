# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:58:09 2020

@author: Leonardo Saccotelli
"""

import numpy as np

"""
FORMULA DEI TRAPEZI
 Al metodo vengono passati:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
"""
def Trapezoid(f_x, a, b):
    #Calcolo l'integrale
    T = (b-a)*(f_x(a)+f_x(b))/2
    return T

"""
FORMULA DEI TRAPEZI COMPOSTI
 Al metodo vengono passati:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
     - il numero di intervallini 
"""
def CompositeTrapezoid(f_x, a, b, N):
    #Estrpolo N+1 intervalli equidistanti da [a,b]
    z = np.linspace(a,b,N+1)
    
    #Calcolo f_x() in ogni punto di z
    fz = f_x(z)
    
    S = 0
    #Calcolo del trapezio composto
    for i in range(1,N):
        S = S + fz[i]

    TC = (fz[0] + 2*S + fz[N])*(b-a)/2/N
    
    return TC

"""
FORMULA DI SIMPSON
 Al metodo vengono passati:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
"""
def Simpson(f_x, a, b):
    #Calcolo l'integrale
    T = ((b-a)/6) * (f_x(a) +4 * f_x((b+a)/2) + f_x(b))
    return T

"""
FORMULA DI SIMPSON COMPOSTA
 Al metodo vengono passati:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
     - il numero di intervalli
"""
def CompositeSimpson(f, a, b, N):
    #Genero n+1 intervallini in [a,b]
    z = np.linspace(a,b,N+1)
    #Calcolo f negli intervalli z
    fz = f(z)
    
    #Definisco le somme dispari e le somme pari
    S_d = 0
    S_p = 0
    
    #Definisco l'ampiezza dei singoli intervalli
    h = (b-a)/N
    
    #Calcolo le somme dispari
    for i in range(1,N,2):
        S_d = S_d + fz[i]
    #Calcolo le somme pari
    for i in range(2,N-1,2):
        S_p = S_p + fz[i]
        
    Tsc = (fz[0] + 4*S_d + 2*S_p + fz[N])*h/3
    
    return Tsc
    
    
    



