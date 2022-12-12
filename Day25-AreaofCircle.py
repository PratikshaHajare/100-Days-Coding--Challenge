'''
Day 25 coding Statement : Write a program to find Area of a circle

Description

Get the value for radius from the user and calculate the area of the circle for the given radius.

Area of circle = 3.14*radius*radius

Input

3

Output

28.26

'''

r=float(input("Enter Radius :"))
if(r<=0):
    print("Invalid Input")
else:
    Area=3.14*r*r
    print("Area of Circle",Area)