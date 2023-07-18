# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second. [Hint: Use the remainder operator.
num1=int(input("Enter The First Number: \n"))
num2=int(input("Enter The 2nd Number: \n"))


if num1 % num2==0:
    print(num1,"is the multiple of",num2)
else:
    print(num1,"is not the multiple of",num2)