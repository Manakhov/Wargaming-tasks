from random import randint
from task_one import isEven, is_even
from task_three import sort

# Task one
print(isEven(0), isEven(1), isEven(2))
print(is_even(0), is_even(1), is_even(2))

# Task three
array = []
length = randint(2, 1000)
for i in range(length):
    array.append(randint(-10, 10))
print("Изначальный массив:\n", array)
print("Отсортированный массив:\n", sort(array))
