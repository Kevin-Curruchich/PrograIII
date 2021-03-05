#Ejercicio 3
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
