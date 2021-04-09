print("Factorial de un numero")
num = input('Ingrese numero: ')
fact = 1
if num.isnumeric() == True:
    if int(num) == 0:
        print("El factorial es 1")
    else:
        for i in range(1,int(num)+1):
            fact = fact * i
        print("El factorial de",num,"es: ",fact)
else:
    print("Usted no ingreso un numero positivo")