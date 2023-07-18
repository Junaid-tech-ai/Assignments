for i in range(1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
n=10
for i in range(1,11):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for star in range(1,i+1):
        print("*",end=" ")
    print()
n=10
for i in range(1,11):
    for j in range(1,n-i+1):
        print(" ",end="")
    for star in range(1,i+1):
        print("* ",end="")
    print()


n=10
for i in range(1,11):
    for j in range(n-i+1):
        print("*",end="")
    print()


n=10
for i in range(1,11):
    for j in range(i):
        print(" ",end=" ")
    for star in range(n-i+1):
        print('*',end=" ")
    print()