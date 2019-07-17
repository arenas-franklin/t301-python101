def media(*valores):
    sum = 0
    for n in valores[0]:
        sum += float(n)
    return sum/len(valores[0]) 

valor = None
lista = []
while True:
    valor = input('quais valores para média? digite sair para parar : ')
    if valor == 'sair':
        break
    lista.append(valor)

print('sua média é', media(lista))

# import statistics
# print(statistics.mean([10,6]))
