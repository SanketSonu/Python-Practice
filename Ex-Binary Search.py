"""
Write a function that takes an list and sort that list in order (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""

size = int(input("Please provide the size of the list: \n"))
print("Please enter the elements of the list 1 by 1: \n")

lst = []
for i in range(0,size):
    ele = int(input())
    lst.append(ele)
num = int(input("Please provide a number that you want to search: \n"))
print("This is unorder list: \n", lst)
lst.sort()
print("This is ordered list: \n", lst)

def search_without_bs(a):
    if num in lst:
        print("Yes number is found in the list. We have used normal function to find this number. \n")
    else:
        print("Number not found in the list.\n")

search_without_bs(lst)

def binary_sort(lst, start, end, num):
    while start <= end:
        mid = start + (end-start)//2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1
result = binary_sort(lst, 0, len(lst)-1, num)
 
if result != -1:
    print("Yes..!! We have used Binary Search for this and element found at {0} index: \n".format(result))
else:
    print("Element is not present in the list. Bbye..!!!")
