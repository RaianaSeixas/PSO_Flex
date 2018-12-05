import M_Function

def OBJ(x): # calcula para uma lista de entradas
    rows = len(x)
#    cols = len(x[0])
    fobj=[0 for row in range(rows)]
    #fobj=np.zeros(rows)
    for i in range(rows):
#        for j in range(cols):
            fobj[i]=M_Function.Rosenbrock(x[i][:])
    return fobj

def VALOR(x): # calcula para um único ponto
    fob=M_Function.Rosenbrock(x)
    return fob

'''
#Versões anteriores
#V0

import numpy as np

def OBJ(x):
    rows = len(x)
#    cols = len(x[0]) # mudança: comentei linha não necessária
#    global fobj # mudança: para obter essa lista em outro módulo
    fobj=np.zeros(rows)
    for i in range(rows):
#        for j in range(cols): # mudança: linha não necessária
            fobj[i]=FUN.Rosenbrock(x[i,])
    return fobj
    # return fobj.min()

'''
