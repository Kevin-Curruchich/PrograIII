#Ejercicio 4
print("Ingrese los datos que se le solicitan\n")
daysP = int(input('Cantidad de días que recibe Programacion III: '))
hours = float(input('Horas utilizadas para el curso Programación III: '))
prom = float(input('\nHoras promedio de estudio autodidacta por día: '))
daysA = int(input('Cantidad de días que estudia de manera autodidacta: '))

hours_day= hours + prom 
hours_progra = hours * daysP
hours_A = prom * daysA

print('\nRESULTADOS FINALES\n')
print('- Tiempo utilizado para estudio diario: ',hours_day, "horas")
print('- Tiempo utilizado para Programacion III a la semana: ',hours_progra, "horas")
print('- Tiempo utilizado para estudio autodidacta: ',hours_A, "horas")
