"""
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

Randomly generate two lists to test this
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in a if i in b]
c = list(dict.fromkeys(c))
print(c)

print("Lets generate 2 random lists and we will use list comprehension to find the common elements.\n")

a1 = int(input("What length of 1st list you want from no. 1 to 100: \n"))
b1 = int(input("What length of 2nd list you want from no. 1 to 100: \n"))

lst1 = []
lst2 = []

for i in range(a1):
	lst1.append(random.randint(1,100))
for j in range(b1):
	lst2.append(random.randint(1,100))

print("List 1:", lst1)
print("List 2: ", lst2)

lst3 = [i for i in lst1 if i in b]
lst3 = list(dict.fromkeys(lst3))

if len(lst3) == 0:
	print("Sorry no matches. Try again.")
print(lst3)