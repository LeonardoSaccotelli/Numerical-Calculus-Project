# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:15:29 2020

@author: Leonardo Saccotelli
"""


def NewtonMethod(f_x, df_x, n, i, x0, tolerance, maxIteration):
    # Calcolo f in xo
    f_x0 = f_x(x0, n, i)

    # Calcolo f' in xo
    df_x0 = df_x(x0, i)

    # Contatore di iterazioni
    iteration = 0
    # Flag sul termine del processo
    stop = False

    while not (stop) and iteration < maxIteration:
        # Calcolo la nuova sol x1 = x0 - f(x0)/f'(x0)
        x1 = x0 - f_x0 / df_x0

        # Calcolo f(x) in x1
        f_x1 = f_x(x1, n, i)

        # Verifica del criterio di arresto
        stop = abs(f_x1) + abs(x1 - x0) / abs(x1) < tolerance / 5

        # Incremento il contatore del numero di iterazioni
        iteration = iteration + 1

        # Se non ho raggiunto lo zero, aggiorno i dati del problema
        # per la prossima iterazione
        if not (stop):
            x0 = x1
            f_x0 = f_x1
            df_x0 = df_x(x0, i)

    # Controllo sull'avvenuta convergenza
    if not (stop):
        print(' The method doesn\'t converge in %d iterations' % iteration)

    return x1, iteration


def rootSquareProblem(x, number, i):
    y = x ** i - number
    return y


def df(x, i):
    return i * (x ** (i - 1))


def df_2(x, i):
    return i * (i - 1) * (x ** (i - 2))


def check_X0(x, i, a, b):
    if rootSquareProblem(a, x, i) * df_2(a, i) > 0:
        X0 = a
    elif rootSquareProblem(a, x, i) * df_2(a, i) < 0:
        X0 = b
    return X0


index = int(input('- Enter the index root: '))
number = float(input('- Enter a positive number: '))
print('-----------------------------------------------')

# Definisco l'intervallo in cui cercare la radice
a = 1
b = 6
# Definisco la tollerenza accettata nell'approssimare la soluzione esatta del problema
tolerance = 1.0e-10

# Verifico xo per innescare il metodo
x0 = check_X0(number, index, a, b)

# Stampo i risultati
x, max_iter = NewtonMethod(rootSquareProblem, df, number, index, x0, tolerance, 50)

print('The root is %f' % x)





