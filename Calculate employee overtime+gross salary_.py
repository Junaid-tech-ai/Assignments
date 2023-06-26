# Develop a program that will determine the gross pay for each of several employees. The
# company pays “straight time” for the first 40 hours worked by each employee and pays
# “time-and-a-half” for all hours worked more than 40 hours. You‟re given a list of the
# employees of the company, the number of hours each employee worked last week and the
# hourly rate of each employee. Your program should input this information for each
# employee and should determine and display the employee's gross pay. Here is a sample
# input/output dialog:
# Enter # of hours worked (-1 to end): 39
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $390.00
# Enter # of hours worked (-1 to end): 40
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $400.00
# Enter # of hours worked (-1 to end): 41Enter hourly rate of the worker ($00.00): 10.00
# Salary is $415.00
# Enter # of hours worked (-1 to end): -1

num_of_employees=int(input("Enter the number of employees: \n"))
for i in range(num_of_employees):
    working_hours=float(input("Enter the working hours:\n"))
    hourly_rate=float(input("Enter the hourly rates:\n"))
    gross_pay=0
    regular_pay=0
    if working_hours<=40:
        gross_pay=working_hours*hourly_rate
    elif working_hours>40:
        regular_pay=hourly_rate*40
        overtime=(working_hours-40)*(hourly_rate*1.5)
        gross_pay=overtime+regular_pay
    print(gross_pay)