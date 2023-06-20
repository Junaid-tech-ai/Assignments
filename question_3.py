# Write a program that takes the marks obtained by a student in five different subjects as
# input through the keyboard, then find out the total marks and percentage marks obtained
# by the student in each subject. Assume that the maximum marks that can be obtained by a
# student in each subject is 100.

sub1=int(input('Enter the first subject number: \n'))
sub2=int(input('Enter the 2nd subject number: \n'))
sub3=int(input('Enter the 3rd subject number: \n'))
sub4=int(input('Enter the 4th subject number: \n'))
sub5=int(input('Enter the fifth subject number: \n'))

total_marks=500
total_marks_each_sub=100


total_obtained_marks=sub1+sub2+sub3+sub4+sub5
percentage_ist_sub=(sub1/total_marks_each_sub)*100
percentage_2nd_sub=(sub2/total_marks_each_sub)*100
percentage_3rd_sub=(sub3/total_marks_each_sub)*100
percentage_4th_sub=(sub4/total_marks_each_sub)*100
percentage_5th_sub=(sub5/total_marks_each_sub)*100
print("total obtained marks =",total_obtained_marks, "\nPercentage of ist subject =",percentage_ist_sub, "Percentage of 2nd subject =", percentage_2nd_sub, "Percentage of 3rd subject =",percentage_3rd_sub, "Percentage of 4th subject =", percentage_4th_sub, "Percentage of fifth subject =", percentage_5th_sub )
percentage=(total_obtained_marks/total_marks)*100
print("Total obtained marks = ",total_obtained_marks, "\nPercentage is = ", percentage, "%")