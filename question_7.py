# If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits. (Hint: Use the modulus operator „%‟ to split the digits).

num1=int(input("Enter the Ist Number :\n"))
num2=int(input("Enter the 2nd Number :\n"))
num3=int(input("Enter the 3rd Number :\n"))
num4=int(input("Enter the 4th Number :\n"))
num5=int(input("Enter the 5th Number :\n"))

digit1=num1%10
digit2=num2%10
digit3=num3%10
digit4=num4%10
digit5=num5%10

digits_sum=digit1+digit2+digit3+digit4+digit5
print("Digit 1 =", digit1, "\nDigit 2 =", digit2, "\nDigit 3 =",digit3, '\nDigit 4 =', digit4, "\nDigit 5 =", digit5)
print('The sum of digits is =',digits_sum)