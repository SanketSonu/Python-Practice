print("Enter your name: ")
a = str(input())
print("Enter your age: ")
b = int(input())

c = 2020
d = (100 - b)
e = (c + d)
print("Hello {0}!!! In year {1} you will turn 100 Years.".format(a,e))

f = int(input("How many times you want to repeat this message?"))
i = 0
for i in range(f):
	print("Hello {0}!!! In year {1} you will turn 100 Years.".format(a,e))

