"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
"""
s = str(input("Enter a String and we will show that in backward order. \n"))
lst1 = []
lst2 = []

def usr_str(v):
    lst1 = s.split()
    print(lst1)
    i = len(lst1) - 1
    while i >= 0:
        lst2.append(lst1[i])
        i -= 1
    print(lst2)
    output = " ".join(lst2)    #This will convert list into String by using "(Space)".
    print("Below is your Output. Your line in backward order. \n")
    print(output)

usr_str(s)

