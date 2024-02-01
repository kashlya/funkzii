text = input("текст: ")
slova = input("зарезервируйте слова: ")
f = slova.split()
a = []
for i in text.split():
    if i in f:
        a.append(i.upper())
if a:
    print(" ".join(a))
else:
    print("не подходят зарезерованные слова")