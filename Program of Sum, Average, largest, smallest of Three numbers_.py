# Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these
# numbers. The screen dialogue should appear as follows:
# Enter three different integers: 13 27 14
# Sum is 54
# Average is 18
# Product is 4914
# Smallest is 13
# Largest is 27

num1=int(input('Enter the first number: \n'))
num2=int(input('Enter the 2nd number: \n'))
num3=int(input('Enter the 3rd number: \n'))
sum=num1+num2+num3
average=sum/3
product=num1*num2*num3
print("Sum is",sum, '\nAverage is', average, "\nProduct is",product)
if num1>num2 and num1>num3:
    print("largest is",num1 )
elif num2>num1 and num2>num3:
    print('Largest is', num2)
else:
    print("largest is ", num3)

if num1<num2 and num1<num3:
    print("Smallest is",num1 )
elif num2<num1 and num2<num3:
    print('Smallest is', num2)
else:
    print("Smallest is ", num3)

