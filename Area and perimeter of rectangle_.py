# The length & breadth of a rectangle are input through the keyboard. Write a program to
# calculate the area & perimeter of the rectangle.


length=int(input('Enter the length of rectangular: \n '))
breath=int(input('Enter the breath of rectangular: \n '))

rectangle_area=length*breath
rectangle_perimeter=2*(length+breath)
print("The Area of Rectangle is =",rectangle_area, "\nThe Perimeter of Rectangle is =", rectangle_perimeter )