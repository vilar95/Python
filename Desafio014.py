#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
C = float(input('Informe a temperatura em °C:'))
F = 32 + ( C * 9/5)
print(f'A temperatura de {C:.1f}°C corresponde a {F:.1f}°F')