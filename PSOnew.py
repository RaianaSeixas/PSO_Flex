
"""
Created on Fri Dec 06 2017
@author: ucfilho
"""
import os
os.chdir('C:\\Users\\raiana\\Data file\\doutorado py\\PSO_new')


import copy
import pandas as pd
import FOBJ
import ENX
import VEL
import PART
import GBEST



def PSO(W,C1,C2,NPAR,ITE,MAX,MIN,x): # mudança: add X aqui
    
    global X
    global BEST
    global PBEST
    global ycal
    global y_PBEST
    global VELOC
    global FOBEST
    
    # INICIALIZA O METODO-
#    X=ENX.Enxame(NPAR,MAX,MIN) # CRIA A POPULACAO
    PBEST=copy.deepcopy(x) # O MELHOR LOCAL DE CADA PARTICULA INICIALMENTE ALEATORIA
#   PBEST=PART.PART(X,PBEST)  # Mudança: Faz X e PBEST serem sempre os mesmos 
    BEST=[]
    FOBEST=1e10
    for i in range(len(MIN)):
       BEST.append(1e10)
    BEST,FOBEST=GBEST.BEST(x,BEST,FOBEST)
    VELOC=ENX.Enxame(NPAR,MAX,MIN)# VELOCIDADES INICIALMENTE ALEATORIAS
    RESP=[]
    for k in range(ITE):
#        FOBEST=VALOR(BEST)
        VELOC, X=VEL.VE(x,VELOC,BEST,PBEST,W,C1,C2)
        BEST,FOBEST=GBEST.BEST(X,BEST,FOBEST)
        PBEST=PART.PART(X,PBEST)
#        print(k,'-','X=',X)
#        print('PBEST=',PBEST)

#        FOBEST=VALOR(BEST)
        RESP.append(FOBEST)
    ycal=FOBJ.OBJ(x) # CALCULA A FUNCAO OBJETIVO PARA TODAS PARTICULAS
    y_PBEST=FOBJ.OBJ(PBEST)
    return RESP
'''
#Verificar PBEST <> X

NPAR=10#PARTICULAS
ITE=4 #ITERACOES
#PAR=2 #NUM DE PARAMETROS A SER OTIMIZADOS
MAX=[50,50] # MAXIMO DE CADA PARAMETRO
MIN=[-50,-50] # MINIMO DE CADA PARAMETRO

W=0.75   
C1=2
C2=2
X=ENX.Enxame(NPAR,MAX,MIN)

PSO1=PSO(W,C1,C2,NPAR,ITE,MAX,MIN,X)

print('Resultados PSO1')
for i in range(ITE):
    print("iteracao=",i,"f obj=",PSO1[i])
print ()
#print(PSO1)
'''