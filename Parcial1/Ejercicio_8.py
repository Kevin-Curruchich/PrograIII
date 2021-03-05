#Ejercicio 8

print('TABLA DE INTERES ANUAL')
print('A) Hasta Q.29,999 - 5%')
print('B) Mayor a Q.30,000 - 7%')
monto = float(input("\nIngrese monto a invertir: "))
años = int(input("Años a invertir: "))
interes_total = 0.0

if monto < 29999:
    for i in range(años):
        interes = monto * 0.05
        monto += interes
        interes_total += interes

if monto > 30000:
    for i in range(años):
        interes = monto * 0.07
        monto += interes
        interes_total += interes

print("\n")
print("Inversión inicial: ","{0:.3f}".format(monto-interes_total))
print("Interes generado: ","{0:.3f}".format(interes_total))
print("Capital: ","{0:.3f}".format(monto))
