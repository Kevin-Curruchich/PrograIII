temp = int(input("Ingrese los grados; "))
nevando = input("Está nevando s/n: ")

print("El clima :)")
if temp < 5:
    print('Hay mucho frio')
    if nevando == "s":
        print('Usa botas, esta nevando')
    else:
        print("No es necesario utilizar botas")