pervaia = int(input("первая цифра: "))
vtoraia = int(input("вторая цифра: "))
for i in range(pervaia, vtoraia + 1):
    print(i, end=" ")
print()
for s in range(vtoraia, pervaia - 1, - 1):
    print(s, end=" ")
print()
for t in range(pervaia, vtoraia + 1):
    if t % 7 == 0:
        print(t, end=" ")
print()
for w in range(pervaia, vtoraia + 1):
    if w % 5 == 0:
        krt_5 = 0
        krt_5 += 1
        print(krt_5, end=" ")