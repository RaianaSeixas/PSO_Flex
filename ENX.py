import random
#random.seed(1)

def Enxame(NPAR,MAX,MIN):
    x= [[0 for col in range(len(MAX))] for row in range(NPAR)]
    #x=np.zeros((NPAR, len(MAX)))
    for j in range(len(MAX)):
        for i in range(NPAR):
            x[i][j]=MIN[j]+(MAX[j]-MIN[j])*random.random()
    return x


'''
import numpy as np

def Enxame(NPAR,MAX,MIN):
    x=np.zeros((NPAR, len(MAX)))
    for j in range(len(MAX)):
        for i in range(NPAR):
            x[i,j]=MIN[j]+(MAX[j]-MIN[j])*np.random.random()
    return x
    
'''