# 1 - Escreva um programa que leia o nome de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.

nome_funcionario = input("Informe o nome do funcionario: ")
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
valor_trabalho = float(input("Informe as o valor do tranbalho por horas: "))

salario = (horas_trabalhadas*valor_trabalho)

print('nome do funcionario: ',nome_funcionario)
print('salário: ', salario)