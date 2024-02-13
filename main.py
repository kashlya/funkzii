import random

random_numbers_1 = [random.randint(0, 40) for i in range(3)]  # первый список
print(random_numbers_1)
random_numbers_2 = [random.randint(0, 40) for s in range(3)]  # вророй список
print(random_numbers_2)

random_numbers_3 = random_numbers_1 + random_numbers_2, set(random_numbers_1 + random_numbers_2), list(set(random_numbers_1).intersection(random_numbers_2)), min(random_numbers_1 + random_numbers_2), max(random_numbers_1 + random_numbers_2)
print(random_numbers_3)