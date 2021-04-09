print("Imprimiendo numeros de 1 a 10")
romper = int(input("En que numero quiere parar: "))

for i in range (1,11):
    if i == romper+1:
        break
    print(i, end=" ")
print("\nFin")