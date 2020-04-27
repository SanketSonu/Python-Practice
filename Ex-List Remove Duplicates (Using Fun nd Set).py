"""
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

a = [1,1,1,2,3,3,4,66,57,57,66,88,99]

def lst_dup1(num):
    
    lst = set(a)
    lst1 = list(lst)
    print("This output is generated using Set data type. \n")
    print(lst1,"\n")

lst_dup1(a)

lst2 = []
def lst_dup2(num):
    for i in num:
        if i not in lst2:
            lst2.append(i)
    print("This output is generated using Loops. \n")
    print(lst2)
lst_dup2(a)


