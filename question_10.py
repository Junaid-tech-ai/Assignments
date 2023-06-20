# Write a program that take year as an input from user. Determine whether year is leap year
# or not.

year=int(input("Enter the year: \n"))

if year%4==0 and year%100!=0:
    print(year, "Is leap year")
elif year%4==0 and year%100==0 and year%400!=0:
    print(year, "This year is not leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print(year, "This is year is leap year")
else:
    print(year,'Is not leap year')