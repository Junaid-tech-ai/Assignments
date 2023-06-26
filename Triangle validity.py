# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

angle_1=int(input("Enter the first angle: \n"))
angle_2=int(input("Enter the 2nd angle: \n"))
angle_3=int(input("Enter the 3rd angle: \n"))

sum=angle_1+angle_2+angle_3
print("Sum of angles is:", sum)
if sum==180:
    print("This Triangle is Valid")
else:
    print("This Triangle is not Valid :>")
