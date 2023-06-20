# Write a program to enter the numbers till the user wants and at the end it should display
# the count of positive, negative and zeros entered
ch=""
num=0
positive_count=0
negative_count=0
zero_count=0
while True:
    num=int(input('Enter the number till the user:\n'))
    if num>0:
        positive_count=positive_count+1
    elif num<0:
        negative_count=negative_count+1
    else:
        zero_count=zero_count+1
    print('Do you want to continue')
    ch=input('Enter yes to continue ')
    if ch=="yes":
        continue
    else:
        break

print("count of positive ",positive_count, "count of negative ",negative_count, "count of zeros",zero_count)



