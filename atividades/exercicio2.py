import random as rd 

lista_numero = []

for item in range(20):
    lista_numero.append(rd.randrange(1,100))

def criar_lista(lista):
    return max(lista)

print(lista_numero)
print(f'O maior número da lista é :{criar_lista(lista_numero)}')