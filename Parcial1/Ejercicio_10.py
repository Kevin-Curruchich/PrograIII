# Ejercicio 10

print('Tecnologia SA')
print('Memorias RAM')
print("- Nuevas $20\n- Usadas 60% off")

uni = int(input("\nUnidades de memoria RAM usadas: "))

ram = 20
precio = ram * uni
descuento = precio * 0.6
total = precio - descuento

print("\nTotal sin descuento: ${}".format(precio))
print("Por ser usadas el descuento es de: ${}".format(descuento))
print("Total a pagar: ${}".format(total))
