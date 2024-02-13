import random

random_numbers = [random.randint(-20, 20) for i in range(10)]
print(random_numbers)
min_ = random_numbers[0]
max_ = random_numbers[0]
for num in random_numbers:
    if num < min_:
        min_ = num
    elif num > max_:
        max_ = num
print(min_, max_)
minus = 0
plus = 0
nol = 0
for s in random_numbers:
    if s < min_:
        min_ = s
    if s > max_:
        max_ = s
    if s < 0:
        minus += 1
    elif s > 0:
        plus += 1
    else:
        nol += 1
print(f"\nmin{min_}", f"\nmax {max_}", f"\nminus {minus}", f"\nplus {plus}", f"\nnol {nol}")
