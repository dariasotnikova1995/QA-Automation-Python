num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
print("Maximum number is: ", max_num)