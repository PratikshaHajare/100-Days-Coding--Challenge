'''
Day 20 coding Statement : Write a program to identify if the number is Prime number or not

Description

Get a number as input from the user and check whether that number is prime or not.

A prime number is a number with factors as 1 and that number itself.

Input

1

Output

1 is not a prime number

Input

5

Output

5 is a prime number  
'''
n=int(input("Enter No: "))
if(n<=1):
    print(f"{n} is invalid input")
else:
    res=True
    for i in range (2,n):
        if(n%i==0):
            res=False
            break
    if(res):
        print(f"{n} is Prime Number")
    else:
        print(f"{n} is Not Prime Number")