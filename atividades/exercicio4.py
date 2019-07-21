import math

def raiz_quadrada(a = 0,b = 0,c=0):
    
    delta = math.pow(b,2)-4 * a * c
    
    if delta == 0:
        x=(-(b)+(math.sqrt(delta)))/2*a
        msg = f'delta é igual a 0,possui apenas uma raiz realvalor de x é: {x}'
    elif delta < 0:
        msg = f'valor de delta {delta} delta menor que 0, não possui uma raiz real'
    elif delta >0:
        x1=(-(b)+(math.sqrt(delta)))/2*a
        x2=(-(b)-(math.sqrt(delta)))/2*a
        msg = f'valor de x1: {x1}, valor de x2: {x2}'
    return msg

print(raiz_quadrada(4,4,1))
print(raiz_quadrada(1,-4,5))
print(raiz_quadrada(1,-5,6))