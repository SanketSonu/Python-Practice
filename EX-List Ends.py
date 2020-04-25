"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""


a = [5, 10, 15, 20, 25]
b = []

def lst(zz):
    for i in a:
        b.append(a[0])
        b.append(a[4])
lst(a)

b = list(dict.fromkeys(b))
print(b)

###Take random list from user and find the first and last elements of list.

n = int(input("Enter size of list u want to enter: \n"))
lst1 = []
lst2 = []
print("Please enter list elements 1 by 1: \n")

for i in range(0,n):
    ele = int(input())
    lst1.append(ele)
print(lst1)

def lst_usr(zzz):
    for i in lst1:
        lst2.append(lst1[0])
        lst2.append(lst1[len(lst1)-1])
lst_usr(lst1)

lst2 = list(dict.fromkeys(lst2))
print(lst2)