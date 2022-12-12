'''
Day 8 coding Statement:  Write a program to find roots of a quadratic equation

Description

Get the values of a, b and c (coefficients of quadratic equation) as input from the user and calculate the roots and print as the output.

Input

Enter the value of a, b and c : 1 -6 9

Output

Roots are equal

Root 1= root 2 = 3.00
'''

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

d=(b**2)-(4*a*c)
sqrt=0.5

if d>0:
  print("Roots are real and different")
  print("Root 1 = ",(-b +(d**sqrt)/(2*a)))
  print("Root 2 = ",(-b -(d**sqrt)/(2*a)))
elif d==0:
  print("Roots are real")
  print(-b / (2*a))
else:
  print("Roots are complex")
  print(- b / (2*a), " + i", sqrt / (2 * a))
  print(- b / (2*a), " - i", sqrt / (2 * a))