n = int(input("Enter a number to know all the possible divisors:"))

a = list(range(1,n+1))

for i in a:
	if n % i == 0:
		print(i)
