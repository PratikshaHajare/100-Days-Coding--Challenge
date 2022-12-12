'''
Day 9 coding Statement : Write a program to find Number of digits in an integer

Description

Take an integer as the input from the user and then calculate the number of digits in the given input and print it as the output.

Input

3241

Output

4 I

nput

6

Output

1
'''
#Program 1
n=int(input())

def countdigit(n):
  n=str(n)
  return len(n)
  
countdigit(n)


#Program 2

n=int(input())
count=0
if(n==0):
  print(1)
else:
  while(n!=0):
    n=n//10
    count+=1
  print(count)
