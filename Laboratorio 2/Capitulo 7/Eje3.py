print("Rango de 0 a 10")
for i in range(0, 10):
    print(i,end=" ")

print("\n\nDe 0 a 10 de 2 en 2")
for i in range(0, 10, 2):
    print(i,end=" ")

print("\n\nSin utilizar el iterador")
for _ in range(0,10):
    print("*", end="")