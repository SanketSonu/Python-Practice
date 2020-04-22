from collections import deque

a = deque([3, 4, 5])
a.append("apple")
a.append("orange")
print(a)

a.popleft()
print(a)

a.popleft()
print(a)