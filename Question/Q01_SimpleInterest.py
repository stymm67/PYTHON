# Write a python program to calculate the simple interest 
principle = float(input("Enter Your Priciple : "))
rate = float(input("Enter Your Rate : "))
time = float(input("Enter Yout Time "))

SimpleInterst = (principle * rate * time)/100
print(SimpleInterst)

totalAmount = SimpleInterst + principle

print("Simple Interest " , totalAmount)
