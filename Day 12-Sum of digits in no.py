'''
Day 12 coding Statement:  Write a program to find Sum of digits of a number

Description

Get a number from user and then find the sum of the digits in the given number.

E.g. let the number = 341

Sum of digits is 3+4+1= 8

Input

4521

Output

12
'''
#Using for loop
n=int(input())
sum=0
for i in range(1,n+1):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)

#Using While Loop
n=int(input())
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)