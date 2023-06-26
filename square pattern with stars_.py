# Write a program that takes the side of a square from user and then prints that square out
# of asterisks. Your program should work for squares of all side sizes between 1 and 20.
# For example, if your program reads a size of 4, it should print
# ****
# ****
# ****
# ****

n=int(input("Enter the number: "))
for i in range(n):
    for j in range(1,n+1):
        print("*",end='')
    print()