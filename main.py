text = input("текст: ")
k = list(text)
count = 0
for i in k:
    if i == ",":
        count += 1
for q in k:
    if q == ".":
        count += 1
for e in k:
    if e == "?":
        count += 1
for w in k:
    if w == "!":
         count += 1
print(count)