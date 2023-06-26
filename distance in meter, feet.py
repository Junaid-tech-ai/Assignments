# The distance between two cities (in km.) is input through the keyboard. Write a program
# to convert and print this distance in meters, feet, inches and centimeters.

distance=int(input("Enter the distance between two cities In KM: \n"))
distance_meter=distance*1000                   #1 Km =1000m
distance_feet=distance_meter*3.28              #1 m=3.28feet
distance_inches=distance_feet* 12              # 1 feet=12 inches
distance_cm=distance_inches * 2.54             # 1 inch=2.54 cm

print("Distance in meters = ", distance_meter, "Distance in feet = ", distance_feet, "Distance in inches = ", distance_inches, "Distace in Cm = ", distance_cm)