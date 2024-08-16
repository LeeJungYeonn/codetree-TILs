n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
for j in range(n-1, -1, -1):
    if (n-1) % 2 != 0:
        if j % 2 != 0:
            for i in range(n-1, -1, -1):
                arr[i][j] = num
                num += 1
        else:
            for i in range(n):
                arr[i][j] = num
                num += 1
    else:
        if j % 2 == 0:
            for i in range(n-1, -1, -1):
                arr[i][j] = num
                num += 1
        else:
            for i in range(n):
                arr[i][j] = num
                num += 1

for row in arr:
    for ele in row:
        print(ele, end=' ')
    print()