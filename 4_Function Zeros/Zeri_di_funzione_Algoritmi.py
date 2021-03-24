# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:07:20 2020

@author: Leonardo Saccotelli
"""
from math import *
from fractions import Fraction

"""
METODO DI BISEZIONE
 Al metodo viene passata:
  - la funzione di cui cercare uno zero
  - l'estremo inferiore dell'intervallo
  - l'estemo superiore dell'intervallo
  - la tollerenza dell'errore'
 Il metodo restituisce:
  - Lo zero di funzione
  - il numero di iterazioni eseguite
"""

def bisectionMethod(f_x, a, b, tolerance ):
    #Controllo la presenza di almeno uno zero nell'intervallo [a, b]
    f_a = f_x(a)
    f_b = f_x(b)
        
    if (f_a * f_b)>0:
        print('Error: root in [%f , %f] not guaranteed' % (a,b))
    #Assicurata la presenza di almeno uno zero in [a,b]
    else:
    #Determino il numero di iterazione necessario per convergere 
    #allo zero di funzione entro l'errore stabilito
        n = int(ceil((log(b-a)-log(tolerance))/log(2)))
        
        for k in range(n+1):
            #Calcolo il punto medio dell'intervallo [a,b]
            c = a + (b-a)/2
            
            #Calcolo il valore di in c
            f_c = f_x(c)
            
            """ast = Fraction(a).limit_denominator(100)
            bst = Fraction(b).limit_denominator(100)
            cst = Fraction(c).limit_denominator(100)
            print('%2d: [a,b]=[%5s,%5s] f(a)=%f f(b)=%f c=%s f(c)=%f' % (k+1, ast,bst,f_a,f_b,cst,f_c))
            """
            #Verifico che lo zero trovato coincida con lo zero del problema
            if abs(f_c) < 1.0e-12:
                #c è lo zero di funzione
                break
            
            #Controllo se lo zero si trova nell'intervallo [a, c]
            if (f_a * f_c) < 0:
                b = c
                f_b = f_c
            else:
            #Lo zero si trova nell'intervallo [c, b]
                a = c
                f_a = f_c                
        
    #Restituisco i risultati del problema
    return c, k+1


"""
METODO DI NEWTON(DELLE TANGENTI)
 Al metodo viene passata:
  - la funzione di cui cercare uno zero
  - la derivata prima della funzione 
  - la prima approssimazione da cui avviare il metodo
  - la tollerenza dell'errore'
  - il numero massimo di iterazioni
 Il metodo restituisce:
  - Lo zero di funzione
  - il numero di iterazioni eseguite
"""
def NewtonMethod ( f_x , df_x , x0 , tolerance , maxIteration ) :
   
    #Calcolo f in xo
    f_x0 = f_x(x0)
    
    #Calcolo f' in xo
    df_x0 = df_x(x0)
    
    #Contatore di iterazioni
    iteration = 0
    #Flag sul termine del processo
    stop = False

    while not (stop) and iteration < maxIteration :
        #Calcolo la nuova sol x1 = x0 - f(x0)/f'(x0)
        x1 = x0 - f_x0 / df_x0
            
        #Calcolo f(x) in x1
        f_x1 = f_x(x1)
        
        #Verifica del criterio di arresto
        stop = abs(f_x1) +abs(x1-x0)/abs(x1) < tolerance/5
        
        #Incremento il contatore del numero di iterazioni
        iteration = iteration+1
        
        #Se non ho raggiunto lo zero, aggiorno i dati del problema
        #per la prossima iterazione
        if not(stop):
            x0 = x1
            f_x0 = f_x1
            df_x0 = df_x(x0)
    
    #Controllo sull'avvenuta convergenza
    if not(stop):
        print (' The method doesn\'t converge in %d iterations' %iteration)
            
    return x1, iteration
    
    
"""
METODO DELLE SECANTI
 Al metodo viene passata:
  - la funzione di cui cercare uno zero
  - la prima approssimazione da cui avviare il metodo
  - la seconda approssimazione da cui avviare il metodo
  - la tollerenza dell'errore'
  - il numero massimo di iterazioni
 Il metodo restituisce:
  - Lo zero di funzione
  - il numero di iterazioni eseguite
"""
def SecantMethod ( f_x, x0, x1, tolerance , maxIteration ) :
   
    #Calcolo f in xo
    f_x0 = f_x(x0)
    
    #Calcolo f in x1
    f_x1 = f_x(x1)
    
    #Contatore di iterazioni
    iteration = 0
    #Flag sul termine del processo
    stop = False

    while not (stop) and iteration < maxIteration :
        #Calcolo la nuova sol x2
        x2 = x1 - ( f_x1 / ((f_x0 - f_x1)/(x0 - x1)))
            
        #Calcolo f(x) in x2
        f_x2 = f_x(x2)
        
        #Verifica del criterio di arresto
        stop = abs(f_x2) +abs(x2-x1)/abs(x2) < tolerance/5
        
        #Incremento il contatore del numero di iterazioni
        iteration = iteration+1
        
        #Se non ho raggiunto lo zero, aggiorno i dati del problema
        #per la prossima iterazione
        if not(stop):
            x0 = x1
            f_x0 = f_x1
            
            x1 = x2
            f_x1 = f_x2
    
    #Controllo sull'avvenuta convergenza
    if not(stop):
        print (' The method doesn\'t converge in %d iterations' %iteration)
            
    return x2, iteration
    

"""
METODO DELLE CORDE
 Al metodo viene passata:
  - la funzione di cui cercare uno zero
  - la derivata prima della funzione 
  - la prima approssimazione da cui avviare il metodo
  - la tollerenza dell'errore'
  - il numero massimo di iterazioni
 Il metodo restituisce:
  - Lo zero di funzione
  - il numero di iterazioni eseguite
"""
def stringRootMethod ( f_x , a, x0 , tolerance , maxIteration ) :
   
    #Calcolo f in xo
    f_x0 = f_x(x0)
    
    #Contatore di iterazioni
    iteration = 0
    #Flag sul termine del processo
    stop = False

    while not (stop) and iteration < maxIteration :
        
        m = (f_x(a) - f_x0)/(a - x0)
        
        if (abs(m) < 1.0e-14):
            print('\'m\'= 0.')
            break
        
        #Calcolo la nuova sol x1 = x0 - f(x0)/m
        x1 = x0 - f_x0 / m
            
        #Calcolo f(x) in x1
        f_x1 = f_x(x1)
        
        #Verifica del criterio di arresto
        stop = abs(f_x1) +abs(x1-x0)/abs(x1) < tolerance/5
        
        #Incremento il contatore del numero di iterazioni
        iteration = iteration+1
        
        #Se non ho raggiunto lo zero, aggiorno i dati del problema
        #per la prossima iterazione
        if not(stop):
            x0 = x1
            f_x0 = f_x1
    
    #Controllo sull'avvenuta convergenza
    if not(stop):
        print ('The method doesn\'t converge in %d iterations' %iteration)
            
    return x1, iteration
   
