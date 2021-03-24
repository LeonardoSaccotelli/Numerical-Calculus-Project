# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:12:52 2017

@author: Leonardo Saccotelli
"""
#In questo software vogliamo studiare il condizionamento dell'operazione di addizione.
# Inseriremo due numeri e l'ordine di grandezza della perturbazione, genereremo una
# perturbazione, perturberemo l'input;
# Calcoleremo la somma dei due numeri iniziali e la somma dei due numeri disturbati.
# Alla fine studieremo l'errore relativo sui dati in input e sull'output.
print(' ------------------------------------------------------')
print('| STUDYING OF CONDITIONING OF THE ADDITIONAL OPERATION |')
print(' ------------------------------------------------------')
from random import random

#Primo numero inserito
first_number = 0
#Secondo numero inserito
second_number = 0
#Ordine di grandezza della perturbazione
orderPerturbation = 0

#----------------------------------------------
#               ACQUISIZIONE DEI DATI IN INPUT
#----------------------------------------------

first_number = float(input(' - Enter a first number: '))
second_number = float(input(' - Enter a second number: '))
orderPerturbation = float(input(' - Enter a order for perturbation: '))

#----------------------------------------------
#               PERTURBAZIONE DEI DATI
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
#          CALCOLO DELL'OPERAZIONE SOMMA
#-------------------------------------------------

#Risultato della somma sui dati non perturbati
correct_sum = first_number + second_number
#Risultato della somma sui dati perturbati
sum_perturbed = firstDisturbedNumber + secondDisturbedNumber

#-------------------------------------------------
#   CALCOLO DELL'ERRORE RELATIVO
#-------------------------------------------------
#Errore relativo sul primo valore in input
error_firstNumber = abs(first_number - firstDisturbedNumber) / abs(first_number)
#Errore relativo sul secondo valore in input
error_secondNumber = abs(second_number - secondDisturbedNumber) / abs(second_number)
#Errore relativo che occorre nel calcolo della somma
error_sum = abs(correct_sum - sum_perturbed) / abs(correct_sum)
#-------------------------------------------------
#   STAMPA DEI RISULTATI
#-------------------------------------------------
print('  -----------------------------------------------------')
print('\n - CORRECT VALUE ENTERED BY USER\n ')
print('    First number = %34.16f \n    Second number= %34.16f' % (first_number,second_number) )
print('  -----------------------------------------------------')
print('\n - PERTURBED VALUES\n ')
print('    First number = %34.16f \n    Second number= %34.16f' % (firstDisturbedNumber,secondDisturbedNumber) )
print('  -----------------------------------------------------')
print('\n - CORRECT SUM\n ')
print('    First+Second = %34.16f' %correct_sum)
print('  -----------------------------------------------------')
print('\n - PERTURBED SUM\n ')
print('    First+Second = %34.16f' %sum_perturbed)
print('  -----------------------------------------------------')
print('\n - ERROR ANALYSIS\n ')
print('    Error on the first number : %15e' %error_firstNumber)
print('    Error on the second number: %15e' %error_secondNumber)
print('    Error on the sum: %25e' %error_sum)
