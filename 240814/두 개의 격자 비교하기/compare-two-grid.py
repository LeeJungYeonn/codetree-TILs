def make_arr(arr, n, m):
    for _ in range(m):
        row = list(map(int, input().split()))
        arr. append(row)
    return arr

n, m = map(int, input().split())

arr1 = []
make_arr(arr1, n, m)

arr2 = []
make_arr(arr2, n, m)

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