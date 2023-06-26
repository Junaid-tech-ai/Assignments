# Write a program that asks the user to enter two numbers, obtains them from the user and
# prints their sum, product, difference, quotient and remainder.

num1=int(input("Enter the first number: \n"))
num2=int(input("Enter the 2nd number: \n"))
while num2==0:
    print("enter the number other than zero:")
    num2=int(input("Enter the 2nd number: \n"))

sum=num1+num2
product=num1*num2
difference=num1-num2
if num2>num1:
    difference=num2-num1

quotient=num1/num2
remainder=num1%num2
print("sum =",sum, "product =", product, "difference =", difference,"quotient =", quotient, "remainder =", remainder)
# ------------------------
# 2-
