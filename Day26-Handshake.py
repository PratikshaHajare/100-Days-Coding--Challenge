'''
Day 26 coding Statement : Write a program to calculate Maximum number of handshakes

Description

Get the number of people in the room as input from the user. Then calculate the maximum number of handshakes possible among that people.

For e.g. If there are N people in the room then the first person has to shake hand with N-1 people and second person has to shake hand with N-1-1 people i.e., N-2 handshakes are possible. Thus, it goes on.

So total hand shakes = N-1 + N-2 + N-3 +………+1 + 0

Input

10

Output

45
'''
#Programme 1
n=int(input("Enter no of people : "))
print(n)
i=1
max_Handshake=0
while(i<=n):
    total=n-i
    max_Handshake=max_Handshake+total
    i=i+1
print(max_Handshake)


#Programme 2-
m=int(input("Enter Person :"))
print("No of Person : ",m)
total_h=m*(m-1)/2
print("Total : ",total_h)
