print("Arreglo de 1 a 10")
num = int(input("Numero a encontrar: "))

for i in range(1,11):
    if i == num+1:
        print("\nNumero encontrado")
        break
    print(i,end=" ")
else:
    print("\nNumero no encontrado")

