rows, cols = (5, 5) 
arr = [[0]*cols]*rows 

arr[0][0] = 1
arr[1][1] = "gg"
arr[2][2] = 50
arr[3][3] = 7
arr[4][4] = 9
for i in arr: 
    print(i)

a = [[1,2,3,4,5], [22, 33, 44, 55, 66], [34,65,56,57,64], [45,33,67,88,97],[65, 77,89, 90, 10]]
for i in a:
    print(i)
a[1][3] = 69

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()