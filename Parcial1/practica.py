
# string = '¡Hola a \'"todas"\' y "\'todos!\'"'
# print(string)

# user = input("Ingrese su Nombre: \n")
# print ('¡Hola',user,'!')

print("Operaciones lógicas")
a = int(input("Ingrese A (0 o 1):  "))
b = int(input("Ingrese B (0 o 1):  "))
q = 0

if a == 0 and b == 0:
    q = 0

if a == 0 and b == 1:
    q = 1

if a == 1 and b == 0:
    q = 1

if a == 1 and b == 1:
    q = 1

print('A - B = Q')
print('{} - {} = {}'.format(a,b,q))


# print("Ingrese los datos que se le solicitan\n")
# daysP = int(input('Cantidad de días que recibe Programacion III: '))
# hours = float(input('Horas utilizadas para el curso Programación III: '))
# prom = float(input('\nHoras promedio de estudio autodidacta por día: '))
# daysA = int(input('Cantidad de días que estudia de manera autodidacta: '))

# hours_day= hours + prom 
# hours_progra = hours * daysP
# hours_A = prom * daysA

# print('\nRESULTADOS FINALES\n')
# print('- Tiempo utilizado para estudio diario: ',hours_day, "horas")
# print('- Tiempo utilizado para Programacion III a la semana: ',hours_progra, "horas")
# print('- Tiempo utilizado para estudio autodidacta: ',hours_A, "horas")


# #Programa No.6
# i = 10
# m = int(input("Ingrese un numero: "))

# for m in range(m):
#     print( "Suma =" , (m + 1 ) * (( m + 1 ) + 1) * 2)

# print("Suma desde 1 a {} es igual a {}".format(m,sum))

# peso = float(input("Ingrese peso (lbs): "))
# altura = float(input("Ingrese estatura (mts): "))
# imc = (peso*0.453592)/(altura)**2

# print("\nTu índice de masa corporal es: ","{0:.2f}".format(imc))

# flo1 = float(input("Ingrese un número flotante: "))
# flo2 = float(input("Ingrese un segundo número flotante: "))

# div = flo1/flo2
# res = flo1%flo2

# print("\nEl cociente de la división entre",flo1,"y",flo2,"es: ","{0:.3f}".format(div))
# print("\nEl reciduo de la división entre",flo1,"y",flo2,"es: ","{0:.3f}".format(res))

# print('TABLA DE INTERES ANUAL')
# print('A) Hasta Q.29,999 - 5%')
# print('B) Mayor a Q.30,000 - 7%')
# monto = float(input("\nIngrese monto a invertir: "))
# años = int(input("Años a invertir: "))
# interes_total = 0.0

# if monto < 29999:
#     for i in range(años):
#         interes = monto * 0.05
#         monto += interes
#         interes_total += interes

# if monto > 30000:
#     for i in range(años):
#         interes = monto * 0.07
#         monto += interes
#         interes_total += interes

# print("\n")
# print("Inversión inicial: ","{0:.3f}".format(monto-interes_total))
# print("Interes generado: ","{0:.3f}".format(interes_total))
# print("Capital: ","{0:.3f}".format(monto))

# barr = 112
# sierra = 75

# print('Ferreteria "El Ferretero"')
# print('Pesos:\n- Barreno = {}kg\n- Sierras = {}kg'.format(barr,sierra))
# u_barr = int(input("\nUnidade de barrenos vendidos: "))
# u_sierra = int(input("Unidade de sierrras vendidas: "))

# peso_total = (barr*u_barr)+(sierra*u_sierra)

# print('\nPeso total de barrenos: {} kg'.format(barr*u_barr))
# print('Peso total de sierras: {} kg'.format(sierra*u_sierra))
# print('\nPeso total del paqueta a enviar: {} kg'.format(peso_total))

# print('Tecnologia SA')
# print('Memorias RAM')
# print("- Nuevas $20\n- Usadas 60% off")

# uni = int(input("\nUnidades de memoria RAM usadas: "))

# ram = 20
# precio = ram * uni
# descuento = precio * 0.6
# total = precio - descuento

# print("\nTotal sin descuento: ${}".format(precio))
# print("Por ser usadas el descuento es de: ${}".format(descuento))
# print("Total a pagar: ${}".format(total))
