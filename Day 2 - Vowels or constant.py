'''
Day 1 coding Statement: Write a program to identify if the character is a vowel or consonant.

Description of the program: 


Take an input character from the user and check whether the given input is a vowel or consonant.

Input
A

Output
Vowel

Input
m

Output
Consonant

Input
3

Output
Invalid Input

'''
#Program-1
ch=input("Enter Letter:")
l1=['A','E','O','I','U','a','e','i','o','u']
if (ch=='A' or ch=='E' or ch=='O' or ch=='I' or ch=='U') or (ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u') :
  print("Vowels")
elif not ch.isalpha():
  print("invalid input")
else:
  print("constant")

#Program-2
ch=input("Enter Letter:")
l1=['A','E','O','I','U','a','e','i','o','u']
i=0
if(ch[i] in l1) :
    print("Vowels")
elif not ch.isalpha():
    print("invalid input")
else:
    print("constant")