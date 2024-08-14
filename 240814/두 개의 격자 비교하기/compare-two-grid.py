n, m = map(int, input().split())

arr1 = []
for _ in range(m):
    row = list(map(int, input().split()))
    arr1. append(row)

arr2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    arr2.append(row)

result = []
for _ in range(m):
    row = [0]*n
    result.append(row)

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        if j != (m-1):
            print(result[i][j], end=' ')
        else:
            print(result[i][j])