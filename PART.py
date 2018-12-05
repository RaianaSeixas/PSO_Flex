import FOBJ

def PART(x,pbest):
    YCAL=FOBJ.OBJ(pbest)
    NEW=FOBJ.OBJ(x)
    rows = len(x)
    for i in range(rows):
        if(YCAL[i]>NEW[i]):
            pbest[i][:]=x[i][:]
    return pbest

'''
import numpy as np

def PART(x,PBEST):
    rows = len(x)
    YCAL=FOBJ.OBJ(PBEST)
    NEW=FOBJ.OBJ(x)
    for i in range(rows):
        if(YCAL[i]>NEW[i]):
            PBEST[i,]=x[i,]
    return PBEST
'''