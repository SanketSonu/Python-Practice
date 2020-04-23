"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

s = input("Please enter a word or number to check if its palindrome or not: \n")


if(s==s[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
