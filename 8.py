# Write a python program to find maximum between middle numbers.
num1=int(input("enter the numer"))
num2=int(input("enter the numer"))
num3=int(input("enter the numer"))
if num1>num2>num3:
    print(num3)
elif num2>num1>num3:
    print(num3)
elif num3>num2>num1:
    print(num2)
else:
    print("no")