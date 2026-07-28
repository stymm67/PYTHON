# Write a python program to swap two number 
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print("=== Before Swap === \na = ", a , "\nb = ", b)

temp = a 
a = b 
b = temp

print("=== After Swap === \na = ", a , "\nb = ", b)