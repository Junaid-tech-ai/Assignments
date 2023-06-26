# Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter.


num1=int(input("Enter The First Number: \n"))
num2=int(input("Enter The 2nd Number: \n"))

if num1>num2:
    print(num1,"Is largest Number")
elif num1==num2:
    print("These Numbers are Equal")
else:
    print(num2,"Is largest Number")
