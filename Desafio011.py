# Calcular quanto de tinta se usaria pra pintar uma parede
lp = float(input('Largura da parede:'))
ap = float(input('Altura da parede:'))
a = lp * ap
lt = a / 2
print(f'Sua parede tem a dimensão de {lp}x{ap} e sua área é de {a:.2f}M².')
print(f'para pintar essa parede, você precisará de {lt:.2f}L de tinta')
