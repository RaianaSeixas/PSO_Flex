'''
Certos problemas a funcao objetivo e a propria funcao em estudo
outros problemas nao segue esta logica por isto usaremos um arquivo
FOBJ.py no lugar de apenas um arquivo de funcoes...
'''

import FUN

def OBJ(x): # calcula p uma lista de entradas
    rows = len(x)
#    cols = len(x[0])
    fobj=[0 for row in range(rows)]
    #fobj=np.zeros(rows)
    for i in range(rows):
#        for j in range(cols):
            fobj[i]=FUN.Rosenbrock(x[i][:])
    return fobj


def VALOR(x):
    fob=FUN.Rosenbrock(x)
    return fob



'''
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
