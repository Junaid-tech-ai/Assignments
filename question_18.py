# A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
# for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
# after 30days your membership will be cancelled. Write a program to accept the number
# of days the member is late to return the book and display the fine or the appropriate
# message

days=int(input("Enter the number of days: \n"))
if days<=5:
    print('The fine of first five days is 50 paise')
elif 6<=days<=10:
    print("The fine of 6-10 days is 1 rupee")
elif days>10:
    print('The fine of above 10 days is 5 rupees')
elif days>=30:
    print('Your membership will be cancelled ')