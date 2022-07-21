from random import Random, randint, random
num1 = float(input("insira um numéro: "))
num2 = float(input("insira outro numéro: "))
soma = num1 + num2

if soma % 2 == 0:
    print(soma + randint(0, 10))
else:
    print(soma - randint(0, 10))
