"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

n = int(input("Enter a number to know all the possible divisors:"))

a = list(range(1,n+1))

for i in a:
	if n % i == 0:
		print(i)
