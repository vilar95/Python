#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e aquatidade de dias pelos quais ele alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$o,15 por km rodado.
dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodados?'))
total = (dias * 60)+(km * 0.15)
print(f'O total a pagar é de R${total:.2f}.')