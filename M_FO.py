'''
Calcula a função objetivo tendo como entrada um vetor de pontos e a função
'''


def FO(x,fun): # calcula p uma lista de entradas
    rows = len(x)
    fobj=[0 for row in range(rows)]
    for i in range(rows):
        fobj[i]=fun(x[i][:])
    return fobj

