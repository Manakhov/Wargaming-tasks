from random import randint
from task_one import isEven, is_even
from task_two import FirstCircularBuffer, SecondCircularBuffer
from task_three import sort

# Task one
print(isEven(0), isEven(1), isEven(2))
print(is_even(0), is_even(1), is_even(2))

# Task two
first_buffer = FirstCircularBuffer(randint(3, 10))
for i in range(randint(3, 10)):
    first_buffer.write(randint(-10, 10))
print("First:", first_buffer.read())
first_buffer.delete()
print("Deleted", first_buffer.read())
second_buffer = SecondCircularBuffer(randint(3, 10))
for i in range(randint(3, 10)):
    second_buffer.write(randint(-10, 10))
print("Second", second_buffer.read())
second_buffer.delete()
print("Deleted", second_buffer.read())

# Task three
array = []
length = randint(2, 1000)
for i in range(length):
    array.append(randint(-10, 10))
print("Original array:", array)
print("Sorted array:", sort(array))
