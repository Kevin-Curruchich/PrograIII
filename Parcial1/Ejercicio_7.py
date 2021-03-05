#Ejercicio 7

flo1 = float(input("Ingrese un número flotante: "))
flo2 = float(input("Ingrese un segundo número flotante: "))

div = flo1/flo2
res = flo1%flo2

print("\nEl cociente de la división entre",flo1,"y",flo2,"es: ","{0:.3f}".format(div))
print("\nEl reciduo de la división entre",flo1,"y",flo2,"es: ","{0:.3f}".format(res))
