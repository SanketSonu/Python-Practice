square = []
for x in range(10):
	square.append(x**2)

print(square)

#or we can use list comprehension to short the code

short = [x**2 for x in range(10)]

print(short)

#One more 

a = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			a.append((x,y))

print(a)

#Or we can use list comprehension

aa = [(x,y) for x in[1,2,3] for y in[3,1,4] if x != y]
print(aa)