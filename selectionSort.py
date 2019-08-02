from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    array = []
    while size > 0:
        array.append(size)
        size-=1
    return array
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista
  
def desenhaGrafico(x,y,y2,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]
def selectionSort(alist):
   count=0
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
               count+=1

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   operacoes.append(count)
   return alist

listas=[]
listaInversa=[]
x2 = [10000,20000,50000,100000]
y = []
y2=[]


for i in range(4):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))


for i in range(4):
  y.append(timeit.timeit("selectionSort({})".format(listas[i]),setup="from __main__ import selectionSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")

aux=operacoes
operacoes=[]
  
for i in range(4):
  y2.append(timeit.timeit("selectionSort({})".format(listaInversa[i]),setup="from __main__ import selectionSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")

operacoes2=operacoes
desenhaGrafico(x2,y,y2,'Quantidade','Tempo', 'selection')
desenhaGrafico(x2,aux,operacoes2,'Quantidade','Swaps', 'selectionSwap')
