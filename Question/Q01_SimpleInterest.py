# Write a python program to calculate the simple interest 
principal = float(input("Enter Your Pricipal : "))
rate = float(input("Enter Your Rate : "))
time = float(input("Enter Yout Time "))

SimpleInterst = (principle * rate * time)/100
print(SimpleInterst)

totalAmount = SimpleInterst + principal

print("Simple Interest " , totalAmount)
