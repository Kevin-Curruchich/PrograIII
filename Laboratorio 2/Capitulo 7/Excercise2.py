ran = input('Ingrese rango:')

if ran.isnumeric():

    num = int(ran)

    if num <= 2:
        print('El numero debe ser mayor a 2')
    else:
        primo = True
        for i in range(2, num):
            for j in range(2, i):
                if i % j == 0:
                    primo = False
                    break
            if primo:
                print('Numero Primo:', i)
            primo = True

else:
    print('El numero debe ser positivo')