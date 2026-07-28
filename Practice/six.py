# Write a program in python to print compound interest
pricipal = float(input("Enter Principle amount : "))
rate = float(input("Enter rate percentage : "))
time = float(input("Enter total time : "))

amount = pricipal * (1 + rate / 100) ** time

print("Compound Interest is " , amount)