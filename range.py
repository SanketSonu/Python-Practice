for i in range(5):
	print(i)

fruits = ["Apple", "Banana", "Mango", "Grapes", "Pineapple"]

print("\n")

for i in range(len(fruits)):
	print(i, fruits[i])

print(range(10)) 						#Strange thing happens when you print this range..!!!

print(sum(range(4)))       				#Sum of range(4) => 6 (0+1+2+3)

print(list(range(5)))