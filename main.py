pervaia = int(input("первая цифра: "))
vtoraia = int(input("вторая цифра: "))
for i in range(pervaia, vtoraia + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)