"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


a = int(input("Enter a number and we will tell you whether it is EVEN or ODD:"))

if a % 2 == 0:
		print("Your number is an EVEN number.")
else:
		print("Your number is an ODD number.")

if a % 4 ==0:
	print("Hurray!! Your number is also a multiple of 4. You are genius.")

num = int(input("Please enter a number:"))
check = int(input("please enter another number:"))

if num % check == 0:
	print("You are Noob.")
else:
	print("You are Ultra Noob.")
