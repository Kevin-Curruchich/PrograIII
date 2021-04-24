from arbol import Arbol

arbolDeNumeros = Arbol(10)
arbolDeNumeros.agregar(99)
arbolDeNumeros.agregar(45)
arbolDeNumeros.agregar(8)
arbolDeNumeros.agregar(15)
arbolDeNumeros.agregar(11)
arbolDeNumeros.agregar(35)
arbolDeNumeros.agregar(75)
arbolDeNumeros.agregar(24)
arbolDeNumeros.agregar(13)
arbolDeNumeros.preorden()
arbolDeNumeros.inorden()
arbolDeNumeros.postorden()

opc = input("Quiere buscar un numero (s/n): ")

if opc == 's':
    busqueda = int(input("Ingresa un número para buscar en el árbol: "))
    n = arbolDeNumeros.buscar(busqueda)
    if n is None:
        print(busqueda," no esta en el arbol")
    else:
        print(busqueda," si esta en el arbol")
elif opc == 'n':
    print("Fin de la ejecucion")
else:
    printn("Opcion invalida")