# Write a python program to calculate the simple interest 
principle = float(input("Enter Your Priciple : "))
rate = float(input("Enter Your Rate : "))
time = float(input("Enter Yout Time "))

amount = (principle * rate * time)/100
print(amount)

totalSI = amount + principle

print("Simple Interest " , totalSI)
