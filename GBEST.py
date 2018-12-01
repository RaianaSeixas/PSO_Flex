import FOBJ

def BEST(X,BEST,FOBEST):
    rows = len(X)
    cols = len(X[0])
    YCAL=FOBJ.OBJ(X)
    for i in range(rows):
        if(YCAL[i]<FOBEST): #mudança: não estava atualizando o falor de NEW para cada partícula (so na proxima iteração)
            for j in range(cols):
                BEST[j]=X[i][j]
            FOBEST=YCAL[i]  #mudança: não estava atualizando o falor de NEW para cada partícula
    return BEST,FOBEST

'''
import numpy as np
import FOBJ

def BEST(X,BEST):
    rows = len(X)
    cols = len(X[0])
    YCAL=FOBJ.OBJ(X)
    NEW=FOBJ.VALOR(BEST)
    for i in range(rows):
        if(YCAL[i]<NEW): #mudança: não estava atualizando o falor de NEW para cada partícula (so na proxima iteração)
            for j in range(cols):
                BEST[j]=X[i,j]
            NEW=YCAL[i]  #mudança: não estava atualizando o falor de NEW para cada partícula
    return BEST
    
'''