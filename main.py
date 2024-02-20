chislo = 6
for i in range(chislo):
    for s in range(1, i + 1):
        print(s, end=" ")
    for s in range(i - 1, 0, -1):
        print(s, end=" ")
    print()
