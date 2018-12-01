# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:13:56 2018

@author: raiana
"""
# Ordenando as particulas em ordem crescente de FO

def SORT(data,fo_data):
    Tupla_FO = [(indice, valor) for indice, valor in enumerate(fo_data)]
    #print('Tupla_FO',Tupla_FO)
    Tupla_FO.sort(key=lambda z: z[1])
    #print('Tupla_FO_sorted',Tupla_FO)
    # organizar dados de X em ordem crescente de FO
    X_sorted=[]
    Y_sorted=[]
    for indice, valor in Tupla_FO:
        X_sorted.append(data[indice])
        Y_sorted.append(fo_data[indice])
        
    return X_sorted, Y_sorted



    
#%% #Também posso usar a função zip(x,y) para criar as tuplas
    A=[2,6,3,1]
    B=[4,36,9,1]
    a,b=SORT(A,B)
    print('A=',A)
    print('B=',B)
    print(a,b)
    
    Tupla=zip(A,B)
    lista=list(Tupla)
    print(lista)
    #unpacking
    c,d=zip(*lista)
    print(c,d)