def make_arr(n):
    arr = [
    list(map(int, input().split()))
    for _ in range(n)
    ]
    return arr

n, m = map(int, input().split())

arr1 = make_arr(n)

arr2 = make_arr(n)

result = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(0,n):
    for j in range(0,m):
        if arr1[i][j] != arr2[i][j]:
            result[i][j] = 1

for i in range(0,n):
    for j in range(0,m):
        print(result[i][j], end=' ')
    print()