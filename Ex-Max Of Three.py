"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
"""

a = int(input("Enter 1st number: \n"))
b = int(input("Enter 2nd number: \n"))
c = int(input("Enter 3rd number: \n"))

if (a > b) and (a > c):
    print('Max value is 1st value:',a)
elif (b > a) and (b > c):
    print('Max value is 2nd value:',b)
elif (c > a) and (c > b):
    print('Max value is 3rd value:',c)



