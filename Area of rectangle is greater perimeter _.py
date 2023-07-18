# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter.


rectangle_length=int(input('Enter the length of rectangle in meter: \n'))
rectangle_breath=int(input('Enter the breath of rectangle in meter: \n'))
Area=rectangle_length*rectangle_breath
Perimeter=2*(rectangle_length+rectangle_breath)
print("The Area of rectangle = ", Area)
print("The perimeter of rectangle = ", Perimeter)
if Area>Perimeter:
    print('Area of rectangle is greater than its perimeter')
else:
    print('The Perimeter of rectangle is great than its Area')