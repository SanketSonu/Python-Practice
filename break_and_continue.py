for i in range(2,10):
	if i % 2 == 0:
		print("Found an even number:", i)
	else:                                                 			#Here else belongs to FOR loop not IF loop
		print("Found a number:", i)

print("\n")
print("Above is using ELSE and below is using CONTINUE.")
print("\n")

for i in range(2,10):
	if i % 2 == 0:
		print("Found an even number:", i)
		continue                                         			
	print("Found a number:", i)


print("\n")
print("Now we will see Break statement.")
print("\n")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
       # loop fell through without finding a factor
        print(n, 'is a prime number')