#Faça um programa que leia um ângulo completo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ângulo = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f} ')
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f} ')
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f} ')