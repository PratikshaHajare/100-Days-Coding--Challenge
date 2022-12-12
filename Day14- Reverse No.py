'''
Day 14 coding Statement : Write a program to reverse a given number

Description

Get an input from the user and the print the reverse of the given number as the output

E.g. let the number be 324 then the reverse of the number is 423

Input

675

Output

576
'''
#Program 1
n=int(input("Enter Value : "))
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)


#Program 2
n=int(input("Enter Value : "))
m=str(n)
n=int(m[::-1])
print(n,type(n))