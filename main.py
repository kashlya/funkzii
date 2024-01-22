nachalo = int(input("начало- "))
konez = int(input("конец- "))

for chislo in range(nachalo, konez + 1):
    if chislo % 7 == 0:
        print(chislo)