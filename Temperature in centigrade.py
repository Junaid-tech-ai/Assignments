# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.

temp_f=int(input("Enter the temperature in Fahrenheit: \n"))
temp_Cel=(5/9)*(temp_f-32)
print("The Temperature in Centigrade is: ", int(temp_Cel))