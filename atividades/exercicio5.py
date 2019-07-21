import math
raio = float(input('informe o raio do circulo: '))
pi = math.pi
def comprimento_circulo(r):
    c = 2 * pi * r
    return round(c,2)

def area_circulo(r):
    a = pi *math.pow(r,2)
    return round(a,2)




print('comprimento do circulo ', comprimento_circulo(raio))
print(' area do circulo ',area_circulo(raio))