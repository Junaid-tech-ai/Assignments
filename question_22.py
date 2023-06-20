# Write a program that calculates and prints the sum of the even integers from 2 to 30.
sum=0
for even_integers in range(2,32,2):
    sum=sum+even_integers
    print(even_integers)
print("The sum of all even integers 2 to 30 is =", sum)


