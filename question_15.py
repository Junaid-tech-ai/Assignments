# (Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
# The formulas for calculating BMI are
# BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
# Create a BMI calculator application that reads the user‟s weight in kilograms and height
# in meters, then calculates and displays the user‟s body mass index. Also, the applicationshould display the following information from the Department of Health and Human
# Services/National Institutes of Health so the user can evaluate his/her BMI:
# BMI VALUES
# Underweight: less than 18.5
# Normal: between 18.5 and 24.9
# Overweight: between 25 and 29.9
# Obese: 30 or greater
weight=int(input('Enter the weight In kilograms: \n'))
height=float(input('Enter the height In meters: \n'))
BMI=weight/(height*height)
print("Body Mass Index Is= ",BMI, "Kg/m2")
if BMI<18.5:
    print('Underweight')
elif 18.5<BMI<24.9:
    print('Normal')
elif 25<BMI<29.9:
    print("Overweight")
elif BMI>=30:
    print('Obesity')