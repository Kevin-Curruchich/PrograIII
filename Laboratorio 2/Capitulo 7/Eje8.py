import random

min = 1
max = 6

otro = 's'
conteo = 1
while otro == 's':
    print('\nJuego de dados No.',conteo)
    print("Los numeros son...")
    print("Dado uno: ",random.randint(min,max))
    print("Dado dos: ",random.randint(min,max))
    otro = input('Quieres jugar de nuevo (s/n): ')
    conteo += 1
