polendrom = input("полендром или нет: ")

shtuka = "".join(s.lower()

for s in polendrom if s.isalnum())

if shtuka == shtuka[::-1]:

    print("это палиндром")

else:

    print("это не палиндром")
