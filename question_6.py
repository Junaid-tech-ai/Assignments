# Two numbers (base and exponent) are entered through the keyboard. Write a program to
# find the value of base raised to the power of exponent.

base_num=int(input('Enter the Base Number: \n'))
exponent_num=int(input("Enter the Exponent: \n"))

value=base_num**exponent_num
print("The result is =", value)