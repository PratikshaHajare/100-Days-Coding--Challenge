'''
Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie

Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

Input

10 20

Output

This point lies in first quadrant.

Input

-10 20

Output

This point lies in second quadrant.
'''

x=int(input("enter Value :"))
y=int(input("enter Value :"))
if(x>=0 and y>=0):
    print("First Quadrant")
elif(x<=0 and y>=0):
    print("Second Quadrant")
elif(x>=0 and y<=0):
    print("Third Quadrant")
else:
    print("Fourth Quadrant")