import random as rd
lista_10_aleatorio = []
impar = []
par = []
for  i in range(10):
    lista_10_aleatorio.append(rd.randrange(1,100))

for i in lista_10_aleatorio:
    if(i % 2 == 0):
        par.append(i)
    else:
        impar.append(i)
        
print(lista_10_aleatorio)
print('impar:',impar)
print('par: ',par)        
