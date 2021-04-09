km = input("Ingrese Km: ")

if km.isnumeric() == True: 
    if float(km)>0:
        millas = float(km) * 0.621371
        print(km,"kilometros = ","{0:.2f} millas".format(millas))
    else:
        print("Kilometros negativo") 
else:
    print("Usted no ingreso un numero")