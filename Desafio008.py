#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
n1 = float(input('Digite um número:'))
cm = n1 * 100
mm = n1 * 1000
print(f' Esse número é {n1}m \n que é igual a {cm}cm \n e é igual a {mm}mm.')