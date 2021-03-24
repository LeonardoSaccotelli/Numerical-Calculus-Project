# -*- coding: utf-8 -*-"""
#Author: Leonardo Saccotelli
#Data:   09/03/2020
#Content: Vogliamo aggiungere 0,1 dieci volte. Ci aspettiamo che il risultato sarà 1.
# In questo software vogliamo dimostrare che ciò non è vero perché 0.1 non è
# un numero di macchina. Poichè 0.1 non è un numero di macchina, di fatto prenderemo 
# una sua approssimazione e pertanto non arriverò mai ad un totale pari ad 1, condizione
# per la terminazione del ciclo; Avremo un ciclo infinito.
# Questo problema verrà risolto considerando come risultato un numero molto vicino a uno.

#Quantità da sommare
quantityToSum = 0.1

#Totale ottenuto
result = 0

#Numero di iterazioni
counter = 0

#Sommiamo 0.1 a result finchè non raggiungo il numero più vicino ad 1  

print('SUM OF NO MACHINE NUMBER')

while abs(result - 1) > 1.0e-14:
    #Aggiungo 0.1
    result = result + quantityToSum
    
	#Incremento il contatore di iterazioni
    counter = counter+1
		
	#Stampo la somma parziale
    print('%2d) Result : %20.23f' % (counter,result))
    
#Stampo il numero più vicino ad 1	
print('The number closest to one is %20.23f' % result )