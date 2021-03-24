# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:13:31 2020

@author: leona
"""
import numpy as np
import matplotlib.pyplot as plt
from InterpolazionePolinomiale_Algoritmi import lagrangeFirstBarycentricFormula

"""
METODO PER LA RAPPRESENTAZIONE DEL METODO DEL TRAPEZIO
 Il metodo riceve:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
"""
def DrawTrapezoid(f_x, a, b):
    #Estrapolo 200 punti equidistanti sull'intervallo [a-0.2, b+0.2]
    x = np.linspace(a-0.2, b+0.2, 200)

    #Calcolo la funzione f nei 200 punti equidistanti
    fx = f_x(x)
    
    plt.figure(1, figsize=(10, 10))
    
    #Creo il grafico di f
    plt.plot(x, fx,'k-', label='f(x)')
     
    #Definisco i vertici del trapezio
    xx = np.array([a, a, b, b, a])
    yy = np.array([0, f_x(a), f_x(b), 0, 0])
    
    #Creo il trapezio
    plt.plot(xx, yy,'b')
    plt.fill([a, a, b, b, a], [0, f_x(a), f_x(b), 0, 0], color ='lavender')
    plt.xlabel('x')
    plt.legend(prop={'size':26})
    plt.show()
    
    
"""
METODO PER LA RAPPRESENTAZIONE DEL METODO DEL TRAPEZIO COMPOSTO
 Il metodo riceve:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
"""
def DrawCompositeTrapezoid(f_x, a, b, N):
    #Estrapolo 200 punti equidistanti sull'intervallo [a-0.2, b+0.2]
    x = np.linspace(a-0.2, b+0.2, 200)

    #Calcolo la funzione f nei 200 punti equidistanti
    fx = f_x(x)
    
    #Estrpolo N+1 intervalli equidistanti da [a,b]
    z = np.linspace(a,b,N+1)
    
    #Calcolo f_x() in ogni punto di z
    fz = f_x(z)
    
    plt.figure(1,figsize=(10, 10))
    
    #Creo il grafico di f
    plt.plot(x,fx,'k-',label='f(x)')
    
    #Creo i trapezi
    for i in range(0,N):
        xx = np.array([z[i], z[i], z[i+1], z[i+1], z[i]])
        yy = np.array([0, fz[i], fz[i+1], 0, 0])
        plt.plot(xx,yy,'b-')
        plt.fill(xx, yy, color ='lavender')

        
    plt.xlabel('x')
    plt.legend(prop={'size':26})
    plt.show()
    
    
"""
METODO PER LA RAPPRESENTAZIONE DEL METODO DEL TRAPEZIO
 Il metodo riceve:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
"""
def DrawSimpson(f, a, b):   
    #----- RAPPRESENTAZIONE GRAFICA
    plt.figure(1,figsize=(8,8))
    #------- Costruzione di f(x)
    #Estrapolo 200 punti equidistanti sull'intervallo [a-0.2, b+0.2]
    x = np.linspace(a-0.2,b+0.2,200)
    #Calcolo la funzione f nei 200 punti equidistanti
    fx = f(x)
    #Creo il grafico di f
    plt.plot(x,fx,'k-',label='f(x)')
    
    
    #------- Costruzione del polinomio di interpolazione
    x_Pol = np.array([a, (b+a)/2, b])
    y_Pol = np.array([f(a), f((b+a)/2), f(b)])
    xPoints = np.linspace(a, b, 200)
    P_x = lagrangeFirstBarycentricFormula(x_Pol, y_Pol, xPoints)
    
    #------- Costruzione del  grafico del polinomio di interpolazione
    xx = np.array([a,a])
    xx = np.append(np.append(xx, xPoints), np.array([b,b,a]))
    
    yy = np.array([0,f(a)])
    yy = np.append(np.append(yy, P_x), np.array([f(b), 0, 0]))
    
    plt.plot(xx,yy,'b')
    plt.fill(xx, yy, color ='lavender')
    
    plt.xlabel('x')
    plt.legend(prop={'size':26})
    plt.show()
    
"""
METODO PER LA RAPPRESENTAZIONE DEL METODO DEL TRAPEZIO
 Il metodo riceve:
     - la funzione integranda
     - l'estremo inferiore di integrazione
     - l'estremo superiore di integrazione
     - il numero di intervalli
"""    
def DrawCompositeSimpson(f, a, b, N):
    
    x = np.linspace(a-0.2,b+0.2,200)
    fx = f(x)
    
    #Estrpolo N+1 intervalli equidistanti da [a,b]
    z = np.linspace(a,b,N+1)
    
    #Calcolo f() in ogni punto di z
    fz = f(z)
    
    plt.figure(1,figsize=(10,8))
    plt.plot(x,fx,'k-',label='f(x)')
    
    for i in range(0,N):
        
        #------- Costruzione del polinomio di interpolazione
        x_Pol = np.array([z[i], (z[i+1] + z[i])/2, z[i+1]])
        y_Pol = np.array([fz[i], f((z[i]+z[i+1])/2), fz[i+1]])
        xPoints = np.linspace(z[i], z[i+1], 10)
        P_x = lagrangeFirstBarycentricFormula(x_Pol, y_Pol, xPoints)
        #plt.plot(x_Pol, y_Pol, 'ro')
        
        #------- Costruzione del  grafico del polinomio di interpolazione
        xx = np.array([z[i],z[i]])
        xx = np.append(np.append(xx, xPoints), np.array([z[i+1], z[i+1], z[i]]))
        
        yy = np.array([0,fz[i]])
        yy = np.append(np.append(yy, P_x), np.array([fz[i+1], 0, 0]))
            
        plt.plot(xx,yy,'b')
        plt.fill(xx, yy, color ='lavender')
       
    plt.xlabel('x')
    plt.legend(prop={'size':26})
    plt.show()   
    