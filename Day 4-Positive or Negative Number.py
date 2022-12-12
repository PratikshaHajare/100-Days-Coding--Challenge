"""
    Day 4 coding Statement:  Write a program to identify of the a number is positive or negative

Description


Get an input number from the user and check whether it is a positive or negative number.

Input : -10
Output : Negative number

Input :0
Output : Neither positive nor negative

Input :15
Output : Positive number

"""
  
  
a=int(input("enter No:"))
if(a<0):
  print("Negative")
elif(a==0):
  print("Neither Negative or Positive")
else:
  print("Positive")