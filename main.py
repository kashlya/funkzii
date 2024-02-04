suma = 0
min_ch = 0
max_ch = 0
while True:
    num = int(input("введи число: "))
    if num == 7:
        print("good bay")
        break
    if num < min_ch:
        min_ch = num
    if max_ch < num:
        max_ch = num
    suma += num
print(min_ch, max_ch, suma)