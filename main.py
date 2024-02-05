primer = input("пример: ")
chast = primer.split()
num_1, num, num_2 = int(chast[0]), chast[1], int(chast[2])
if num == "+":
    otvet = num_1 + num_2
elif num == "-":
    otvet = num_1 - num_2
elif num == "*":
    otvet = num_1 * num_2
elif num == "/":
    otvet = num_1 / num_2
print(f"ответ: {otvet}")