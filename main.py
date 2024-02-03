pervoe = int(input("начало: "))
vtoroe = int(input("конец: "))
summa = 0
summa_2 = 0
summa_3 = 0
for i in range(pervoe, vtoroe + 1):
    if i % 2 == 0:
        summa += i
print(f"сумма парных: {summa}")
for s in range(pervoe, vtoroe + 1):
    if not s % 2 == 0:
        summa_2 += s
print(f"сумма не парных: {summa_2}")
for r in range(pervoe, vtoroe + 1):
    if r % 9 == 0:
        summa_3 += r
print(f"сумма крат. 9: {summa_3}")
print(f"среднеарифметическое {summa + summa_2 + summa_3}")