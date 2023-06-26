# Write a program to generate all combinations of 1, 2 and 3 using for loop.
#
num1=int(input('Enter the ist number:'))
num2=int(input('Enter the 2nd number:'))
num3=int(input('Enter the 3rd number:'))
combination=[]
combination.append(num1)
combination.append(num2)
combination.append(num3)

for i in range(0,3):
    print("i",i)
    for j in range(0,3):
        print('j',j)
        for z in range(0,3):
            print("z",z)
            print(combination[i],combination[j],combination[z])

