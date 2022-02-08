#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos aluno. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteda.
import random
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p, s, t, q]
random.shuffle(lista)
print(f'A ordem de apresentação será: \n {lista}.')