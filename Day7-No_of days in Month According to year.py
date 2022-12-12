'''
Day 7 coding Statement:  Write a program to find Number of days in a given month of a given year

Description

Get the number of month and year as input from the user and check the number of days present in that month.

Input

Enter month : 2

Enter year : 2000

Output

29

'''
m=int(input("Enter Month : "))
y=int(input("Enter Year : "))
ms=[1,3,5,7,8,10,12]
if(m==2) and ((y%400==0) or (y%100!=0 and y%4==0)):
  print(29)
elif m==2 :
  print(28)
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
  print(31)
else:
  print(30)