#  Write a program that reads in the radius of a circle and prints the circle‟s diameter,
# circumference and area. Use the constant value 3.14159 for pi. Perform each of these
# calculations inside the print statement(s) and use the conversion format specifier %f.

radius=int(input("Enter the value of radius in cm: \n"))

import math
pi=math.pi

circle_diameter=2*radius
circle_circumference=2*pi*radius
circle_area=pi*radius**2


print("The Diameter Of Circle =",circle_diameter, "cm", "\nThe Circumference of Circle =", circle_circumference, "cm" "\nThe Area of Circle =", circle_area, "cm")