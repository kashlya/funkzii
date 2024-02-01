pervaia = int(input("первая цифра: "))
vtoraia = int(input("вторая цифра: "))
for i in range(pervaia, vtoraia + 1):
    if i % 7 == 0:
        print(i)