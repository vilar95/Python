#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçao ineira.
from math import trunc
num = float(input('Digite um valor:'))
print(f'O valor digitado pé {num} e a sua porção inteira é {trunc(num)}.')