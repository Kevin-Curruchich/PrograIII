km = input("Ingrese Km: ")

if km.isnumeric() == True: 
    if float(km)>0:
        millas = float(km) * 0.621371
    else:
        print("Kilometros negativo")
print(km,"kilometros = ","{0:.2f} millas".format(millas))