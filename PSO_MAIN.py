import os
os.chdir(r'C:\Users\raiana\Data file\doutorado py\PSO_new')

import time
start_time = time.time()

import copy
import PSOnew
import ENX
import FOBJ
import FSORT
import PSOvm

############################### Parâmetros

NPAR=50 #PARTICULAS
ITE=100 #ITERACOES
#PAR=2 #NUM DE PARAMETROS A SER OTIMIZADOS
MAX=[50,50] # MAXIMO DE CADA PARAMETRO
MIN=[-50,-50] # MINIMO DE CADA PARAMETRO
#NMET=2 #NUM DE MÉTODOS A SEREM RESOLVIDOS SIMULTANEAMENTE
PTRADE=5 #NUM DE PARTÍCULAS A SERERM TROCADAS ENTRE OS MÉTODOS
INTERV=4 #NUM DE INTERVENÇÕES (TROCAS) A SEREM REALIZADAS
ITE_M=int(round(ITE/INTERV)) #ITERACOES ENTRE CADA INTERVENÇÃO

print()
print('Iterações por etapa:',ITE_M)

############################## RESOLUÇÃO MÉTODO 1
# Parâmetros M1
W1=0.75   
Cc1=2
Cg1=2
##################################################

print('__________________Iteration= 0____________________')

X=ENX.Enxame(NPAR,MAX,MIN)
#print('X1=',X)

RESP1=PSOnew.PSO(W1,Cc1,Cg1,NPAR,ITE_M,MAX,MIN,X)

RPSO_1=[]
for n in range(len(RESP1)):
    RPSO_1.append(RESP1[n])

BEST_1=PSOnew.BEST
FOBEST_1=PSOnew.FOBEST

# Ordenando as particulas em ordem crescente de FO

Y=PSOnew.ycal
X_1,Y=FSORT.SORT(X,Y)

#print()
#print('X_sorted:',X_1)
#print()
#print('FO(X):',Y)

# Ordenando dados de PBEST E VELOCIDADE em ordem crescente de FO

PBEST_1=FSORT.SORT(PSOnew.PBEST,Y)[0]
VELOC_1=FSORT.SORT(PSOnew.VELOC,Y)[0]
    
#print()
#print('PBEST_sorted:',PBEST_1)
#print()
#print('FO(PBEST):',FOBJ.OBJ(PBEST_1))

# Imprimir resultados
print()
print('Resultados PSO1')
for i in range(0,ITE_M,20):
    print("iteracao=",i,"f obj=",RESP1[i])
print("iteracao=",ITE_M-1,"f obj=",RESP1[ITE_M-1])
print()
print('BEST POSITION=',BEST_1, 'BEST FO=',FOBEST_1)

running_time = '%.3f' %(time.time() - start_time)
print('Tempo=','--- %s seconds ---' % (running_time))


############################## RESOLUÇÃO MÉTODO 2
# Parâmetros M2
W2=0.65
Cc2=1.5
Cg2=2
##################################################

X=ENX.Enxame(NPAR,MAX,MIN)
#print('X2=',X)

RESP2=PSOnew.PSO(W2,Cc2,Cg2,NPAR,ITE_M,MAX,MIN,X)

RPSO_2=[]
for n in range(len(RESP2)):
    RPSO_2.append(RESP2[n])

BEST_2=PSOnew.BEST
FOBEST_2=PSOnew.FOBEST

# Ordenando as particulas em ordem crescente de FO
Y=PSOnew.ycal
X_2,Y=FSORT.SORT(X,Y)

#print()
#print('X_sorted:',X_2)
#print()
#print('FO2(X):',Y)

# Ordenando dados de PBEST E VELOCIDADE em ordem crescente de FO

PBEST_2=FSORT.SORT(PSOnew.PBEST,Y)[0]
VELOC_2=FSORT.SORT(PSOnew.VELOC,Y)[0]

#print()
#print('PBEST_sorted:',PBEST_2)
#print()

#Imprimir resultados

print()
print('Resultados PSO2')
for i in range(0,ITE_M,20):
    print("iteracao=",i,"f obj=",RESP2[i])
    
print("iteracao=",ITE_M-1,"f obj=",RESP2[ITE_M-1])
print()
print('BEST POSITION=',BEST_2, 'BEST FO=',FOBEST_2)

running_time = '%.3f' %(time.time() - start_time)
print('Tempo=','--- %s seconds ---' % (running_time))
print()

############################## TROCA DE PONTOS ENTRE MÉTODOS 

iteration=1
while (iteration < INTERV):

    print('__________________Iteration=',iteration,'____________________')
    print()
        
    #Coleta as melhores particúlas de um método (que estão dispostas em ordem crescente)
    #(Automatizar depois com um for até o pamametro NMET)
    TRADE_X1=X_1[0:PTRADE] # PTRADE=NUM DE PARTÍCULAS A SERERM TROCADAS
    TRADE_X2=X_2[0:PTRADE]
    
    #Substitui as partículas de pior FO de data_old (fim da lista) de 1 método pelo conjunto de melhores partículas (trade) de outro método  
    def TRADE(data_old,trade):
        for p in range(PTRADE):
            data_old[len(data_old)-1-p]=trade[p]
        return data_old
        
#    print('x1=',X_1)
#    print('x2=',X_2)    
    X_1=TRADE(X_1,TRADE_X2) 
    X_2=TRADE(X_2,TRADE_X1)
#    print('x1new=',X_1,'____________________________________')
#    print('x2new=',X_2,'____________________________________')    
    
    # Para cada patícula i trocada, PBESTi=Xi
    PBEST_1=TRADE(PBEST_1,TRADE_X2) 
    PBEST_2=TRADE(PBEST_2,TRADE_X1)
    
    '''Velocidade e Best global?'''
    # ? Gerar novas velocidades aleatórias qd da troca de partículas? Ou manter as antigas (V para piores valores de FO)? Ou outra solução
    # ? Trocar também o parametro BEST para do met pior?


    
    ############################## Execução M1
    
    RESP1,X_1,PBEST_1,VELOC_1,BEST_1,FOBEST_1=PSOvm.PSO(W1,Cc1,Cg1,NPAR,ITE_M,MAX,MIN,X_1,PBEST_1,VELOC_1,BEST_1,FOBEST_1)

    n=0
    for n in range(len(RESP1)):
        RPSO_1.append(RESP1[n])
        
    # Ordenando PARTÍCULAS, PBEST E VELOCIDADE em ordem crescente de FO
    Y=PSOvm.ycal
    X_1,Ysorted=FSORT.SORT(X_1,Y)
    PBEST_1=FSORT.SORT(PBEST_1,Y)[0]
    VELOC_1=FSORT.SORT(VELOC_1,Y)[0]
    
#    print()
#    print('X1:',X_1)
#    print()
#    print('FO_1(X):',Ysorted)

   
    ### Imprimir resultados
    print ()
    print('Resultados PSO1')
    for i in range(0,ITE_M,20):
        print("iteracao=",i,"f obj=",RESP1[i])
        
    print("iteracao=",ITE_M-1,"f obj=",RESP1[ITE_M-1])
    print()
    print('BEST POSITION=',BEST_1, 'BEST FO=',FOBEST_1)
#    print()
    
    ############################## Execução M2
    
    RESP2,X_2,PBEST_2,VELOC_2,BEST_2,FOBEST_2=PSOvm.PSO(W2,Cc2,Cg2,NPAR,ITE_M,MAX,MIN,X_2,PBEST_2,VELOC_2,BEST_2,FOBEST_2)   

    for n in range(len(RESP2)):
        RPSO_2.append(RESP2[n])
          
    # Ordenando PARTÍCULAS, PBEST E VELOCIDADE em ordem crescente de FO
    Y=PSOvm.ycal
    X_2,Ysorted=FSORT.SORT(X_2,Y)
    PBEST_2=FSORT.SORT(PBEST_2,Y)[0]
    VELOC_2=FSORT.SORT(VELOC_2,Y)[0]

#    print()
#    print('X2:',X_2)
#    print()
#    print('FO2(X):',Y)
    
    ### Imprimir resultados
    print()
    print('Resultados PSO2')
    for i in range(0,ITE_M,20):
        print("iteracao=",i,"f obj=",RESP2[i])
        
    print("iteracao=",ITE_M-1,"f obj=",RESP2[ITE_M-1])
    print()
    print('BEST POSITION=',BEST_2, 'BEST FO=',FOBEST_2)
    print()
    
    iteration=iteration+1
    
############################## Cálculo e impressão tempo de execução
  
running_time = '%.3f' %(time.time() - start_time)
print('Tempo Total=','--- %s seconds ---' % (running_time))
#print(X_1,'/n',PBEST_1,'/n',VELOC_1)

############################## Gráfico de resultados 

import matplotlib.pyplot as plt
#plt.subplot(3, 1, 1)
plt.plot(RPSO_1,'bo-',label='PSO1 vm')
#plt.subplot(3, 1, 2)
plt.plot(RPSO_2,'r^-',label='PSO2 vm')
plt.legend()
plt.grid(True)
ax=plt.gca()
ax.axis([-10,ITE,-10,100])
plt.xlabel('Iterations')
plt.ylabel('Objetive Function')
plt.savefig('metodos.png')

############################## Definição melhor resultado entre métodos
if FOBEST_1>FOBEST_2: 
    print()
    print('FINAL BEST POSITION=',BEST_2, 'BEST FO=',FOBEST_2)
else:
    print()
    print('FINAL BEST POSITION=',BEST_1, 'BEST FO=',FOBEST_1)


