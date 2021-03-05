#Ejercicio 6

peso = float(input("Ingrese peso (lbs): "))
altura = float(input("Ingrese estatura (mts): "))
imc = (peso*0.453592)/(altura)**2

print("\nTu índice de masa corporal es: ","{0:.2f}".format(imc))
