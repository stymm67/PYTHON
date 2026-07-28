"""
user input = list[11-12]
target element = input

search 1 by 1 element

found
not found
"""

numbers = []

for i in range(3):
    element = (input("Enter an element: "))
    numbers.append(element)

target = (input("Enter target element: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(i)
