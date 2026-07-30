# write a program in python to check if he/she is eligible for vote or not.
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
gender = input("Enter M or F : ")

if(gender == "M"):
  if(age>=18):
    print("YES!! Mr. " , name, " is eligible for vote.")

if(gender == "F"):
  if(age>=18):
    print("YES!! Mrs. " , name, " is eligible for vote.")