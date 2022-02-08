#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
n1 = float(input('Quantos reais você tem na carteira? R$'))
usd = n1 / 5.40
print(f' Com esse valor de R${n1:.2f} \n você pode comprar US${usd:.2f}')