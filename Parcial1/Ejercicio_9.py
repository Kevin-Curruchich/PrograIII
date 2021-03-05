# Ejercicio 9

barr = 112
sierra = 75

print('Ferreteria "El Ferretero"')
print('Pesos:\n- Barreno = {}kg\n- Sierras = {}kg'.format(barr,sierra))
u_barr = int(input("\nUnidade de barrenos vendidos: "))
u_sierra = int(input("Unidade de sierrras vendidas: "))

peso_total = (barr*u_barr)+(sierra*u_sierra)

print('\nPeso total de barrenos: {} kg'.format(barr*u_barr))
print('Peso total de sierras: {} kg'.format(sierra*u_sierra))
print('\nPeso total del paqueta a enviar: {} kg'.format(peso_total))
