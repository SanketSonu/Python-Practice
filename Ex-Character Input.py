"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

print("Enter your name: ")
a = str(input())
print("Enter your age: ")
b = int(input())

c = 2020
d = (100 - b)
e = (c + d)
print("Hello {0}!!! In year {1} you will turn 100 Years.".format(a,e))

f = int(input("How many times you want to repeat this message?"))
i = 0
for i in range(f):
	print("Hello {0}!!! In year {1} you will turn 100 Years.".format(a,e))

