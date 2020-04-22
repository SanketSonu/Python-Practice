a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
	if i < 5:
	  print(i)
	  b.append(i)
print(b)
print(a)
n = int(input("Enter a number and we will show you elements of list lesser than that value:"))

for i in a:
	if i < n:
		print(i)
