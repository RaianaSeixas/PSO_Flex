
import random
#random.seed(1)

def VE(x,VEL,BEST,pbest,W,C1,C2):
    rows = len(x)
    cols = len(x[0])
    for i in range(rows):
        for j in range(cols):
            R1=random.random()
            R2=random.random()
            VEL[i][j]=W*VEL[i][j]+C1*R1*(pbest[i][j]-x[i][j])+C2*R2*(BEST[j]-x[i][j])
            x[i][j]=x[i][j]+VEL[i][j]
    return VEL,x


'''

import numpy as np
import random

def VE(X,VEL,BEST,PBEST,W,C1,C2):
    rows = len(X)
    cols = len(X[0])
    for i in range(rows):
        for j in range(cols):
            R1=np.random.random()
            R2=np.random.random()
            VEL[i,j]=W*VEL[i,j]+C1*R1*(PBEST[i,j]-X[i,j])+C2*R2*(BEST[j]-X[i,j])
            X[i,j]=X[i,j]+VEL[i,j]
    return VEL,X
'''
