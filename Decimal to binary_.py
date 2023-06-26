# Write a program to find the binary equivalent of the entered number., i.e. binary
# equivalent of 170 is 10101010

num=int(input("Enter the number: \n"))
l=list()
while num !=0:
    num=num//2
    print("n=", num)
    r=num%2
    print("r =",r)
    l.append(r)
print(l)