# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:19:11 2017

@author: Leonardo Saccotelli
"""
#In questo software vogliamo studiare il condizionamento dell'operazione di moltiplicazione.
# Inseriremo due numeri e l'ordine di grandezza della perturbazione, genereremo una
# perturbazione, perturberemo l'input; 
# Calcoleremo il prodotto dei due numeri iniziali e il prodotto dei due numeri disturbati.
# Alla fine studieremo l'errore relativo sui dati in input e sull'output.

from random import random

print(' ------------------------------------------------------')
print(' -------------------------------------------------------')
print('|   STUDYING OF CONDITIONING OF THE PRODUCT OPERATION   |')
print(' -------------------------------------------------------')

#Primo numero inserito
first_number = 0

#Secondo numero inserito
second_number = 0

#Perturbazione inseita in input dall'utente
orderPerturbation = 0

#----------------------------------------------
#   INSERIMENTO DEI DATI
#----------------------------------------------

first_number = float(input(' - Enter a first number: '))

second_number = float(input(' - Enter a second number: '))

orderPerturbation = float(input(' - Enter a order for perturbation: '))
#----------------------------------------------
#   PERTURBIAMO I DAII
#----------------------------------------------

#Generazione della perturbazione sul primo input
deltaFirstNumber = ((random()-0.5)*2)*orderPerturbation

#Generazione della perturbazione sul secondo input
deltaSecondNumber = ((random()-0.5)*2)*orderPerturbation

#Variabile utilizzato per memorizzare il primo numero che è stato perturbato
firstDisturbedNumber = first_number + deltaFirstNumber

#Variabile utilizzato per memorizzare il secondo numero che è stato perturbato
secondDisturbedNumber = second_number + deltaSecondNumber
#-------------------------------------------------
#   ESEGUIAMO L'OPERAZIONE
#-------------------------------------------------

#Risultato del prodotto sui dati non perturbati
correct_product = first_number * second_number

#Risultato del prodotto sui dati perturbati
product_perturbed = firstDisturbedNumber * secondDisturbedNumber

#-------------------------------------------------
#          CALCOLO DELL'ERRORE RELATIVO
#-------------------------------------------------
#Errore relativo sul primo valore in input
error_firstNumber = abs(first_number - firstDisturbedNumber) / abs(first_number)

#Errore relativo sul secondo valore in input
error_secondNumber = abs(second_number - secondDisturbedNumber) / abs(second_number)

#Errore relativo sull'output
error_product = abs(correct_product - product_perturbed) / abs(correct_product)

#-------------------------------------------------
#           PRINT THE RESULT
#-------------------------------------------------
print('  -----------------------------------------------------')
print('\n - CORRECT VALUE ENTEREDBY USER\n ')
print('    First number = %34.16f \n    Second number= %34.16f' % (first_number,second_number) )
print('  -----------------------------------------------------')
print('\n - PERTURBED VALUES\n ')
print('    First number = %34.16f \n    Second number= %34.16f' % (firstDisturbedNumber,secondDisturbedNumber) )
print('  -----------------------------------------------------')
print('\n - CORRECT PRODUCT\n ')
print('    First x Second = %34.16f' %correct_product)
print('  -----------------------------------------------------')
print('\n - PERTURBED PRODUCT\n ')
print('    First x Second = %34.16f' %product_perturbed)
print('  -----------------------------------------------------')
print('\n - ERROR ANALYSIS\n ')
print('    Error on the first number : %20e' %error_firstNumber)
print('    Error on the second number: %20e' %error_secondNumber)
print('    Relative error on the product: %17e' %error_product)
