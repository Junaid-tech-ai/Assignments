# Write a program to produce the following output using loop:
# 1
# 2
# 4
# 7
# 3
# 5
# 8
# 6
# 9
# 10

n=4
a=1
for i in range(1,5):
    for space in range(1,n-i+1):
        print(' ',end='')
    for num in range(i):
        print(a,end=" ")
        a+=1
    print()