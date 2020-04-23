"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in a:
	for j in b:
		if i == j:
			c.append(i)

c = list(dict.fromkeys(c))
print(c)

n = int(input("Enter size for list 1 and we will give random list 1:"))
m = int(input("Enter size for list 2 and we will give random list 2:"))

lst1 = []
lst2 = []
lst3 = []
for i in range(n):
	lst1.append(random.randint(1,50))
for j in range(m):
	lst2.append(random.randint(1,50))

print("List 1: ", lst1)
print("List 2: ", lst2)

for i in lst1:
	for j in lst2:
		if i == j:
			lst3.append(i)
			print(lst3)

if len(lst3) == 0:
	print("Sorry no matches. Try again.")

lst3 = list(dict.fromkeys(lst3))
