#Sección 6.4.1 y 6.4.2
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

#Sección 6.4.3
aho = float(input("Ingresa tus ahorros: "))
if aho == 0:
    print("No tienes ahorros :(")
elif aho < 100:
    print("Sigue ahorrando!")
elif aho < 500:
    print("Ya puedes utilizar tu ahorros")
elif aho < 0:
    print("Numero no valido")
else:
    print("Tienes mucho dinero")