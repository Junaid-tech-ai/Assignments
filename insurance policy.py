# A company insures its drivers in the following cases:
# − If the driver is married.
# − If the driver is unmarried, male & above 30 years of age.
# − If the driver is unmarried, female & above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex and age of the driver
# are the inputs, write a program to determine whether the driver is to be insured or not.

marital_status=str(input("Enter the marital status: \n "))


if marital_status=="married":
    print("This driver is insured")

if marital_status=="unmarried":
    sex_status=str(input("Enter the sex : \n "))
    age=int(input("Enter the age: \n"))
    if marital_status=="unmarried" and sex_status=="male" and age>30:
        print("This driver is insured")

    elif marital_status=="unmarried" and sex_status=="female" and age>25:
        print("This driver is insured")

    else:
        print("This driver is not Insured")
