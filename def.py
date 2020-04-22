x = int(input("Enter any positive number:"))

def fib(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	print(result)
	
fib(x)                                          # Calling function def fib(n) with value 'x' provided by the user.