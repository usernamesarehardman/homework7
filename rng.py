import random

# Task 1: Five random numbers between 0 and 99
random_numbers_1 = [random.randint(0, 99) for _ in range(5)]
print("Task 1: Five random numbers between 0 and 99:", random_numbers_1)

# Task 2: Five random numbers with seed 3323 between 0 and 99
random.seed(3323)
random_numbers_2 = [random.randint(0, 99) for _ in range(5)]
print("Task 2: Five random numbers with seed 3323 between 0 and 99:", random_numbers_2)

# Task 3: Seven random numbers with seed 80 between 0 and 255
random.seed(80)
random_numbers_3 = [random.randint(0, 255) for _ in range(7)]
print("Task 3: Seven random numbers with seed 80 between 0 and 255:", random_numbers_3)

# Task 4: Ten random numbers with seed 443 between 0 and 255
random.seed(443)
random_numbers_4 = [random.randint(0, 255) for _ in range(10)]
print("Task 4: Ten random numbers with seed 443 between 0 and 255:", random_numbers_4)
