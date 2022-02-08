#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
s = n1 + n2
f = s / 2
print (f'A soma das notas é {s:.2f}')
print(f' e a média final é  {f:.2f} . Parabéns !!! ')