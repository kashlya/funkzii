a = int(input("число a: "))
b = int(input("число b: "))
suma = 0
dilniki = a
if a < b:
    for i in range(a, b + 1):
        ch = 0
        for s in range(1, i + 1 // 2 + 1):
            if i % s == 0:
                ch += s
        if ch > suma:
            dilniki = i
            suma = ch
    print(dilniki, suma)
else:
    print("false")
