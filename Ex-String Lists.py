s = input("Please enter a word or number to check if its palindrome or not: \n")


if(s==s[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
