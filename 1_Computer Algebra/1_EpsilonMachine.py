# -*- coding: utf-8 -*-
"""

@author: Leonardo Saccotelli
"""
#Vogliamo calcolare l'epsilon machine
#L'epsilon machine è il più piccolo numero maggiore di zero,
#ovvero eps è tale che, 1+eps > 1
#Dopo aver calcolato l'epsilon machine, calcoleremo la precisione
#e infine il numero di cifre significative
import math

InitialValue = 1.0
#Finchè (1+ InitialValue)>1 continuo a iterare
while(1 + InitialValue)>1:

    #Memorizzo il valore precedente che sarà l'espilon Machine
    epsilonMachine = InitialValue

    #Dimezzo InitialValue in modo tale che ad ogni iterazione sommo quantità
    #sempre più piccole
    InitialValue = InitialValue / 2

#Calcolo la precisione del calcolatore
machinePrecision = 1 - (math.log(epsilonMachine)/math.log(2))

#Cifre significative
significantNumber = machinePrecision*(math.log(2,10))

#Stampo i risultati
print('The decimal value of Epsilon Machine  : %.16f '% epsilonMachine)
print('Scientific notation of Epsilon Machine: %e' %epsilonMachine)
print('Precision: %d' %machinePrecision)
print('Significant: %f' %significantNumber)
