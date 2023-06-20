# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle.

side1=float(input("Enter the first side of triangle: \n"))
side2=float(input("Enter the 2nd side of triangle: \n"))
side3=float(input("Enter the third side of triangle: \n"))

if side1==side2==side3:
    print('This is equilateral triangle')
elif side1==side2 or side2==side3 or side1==side3:
    print('This is isosceles triangle')
elif side1==side2+side3 or side2==side1+side3 or side3==side1+side2:
    print('This is right angle triangle')
else:
    print('This is scalene triangle')