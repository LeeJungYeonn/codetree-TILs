n, m = map(int, input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x,y = tuple(map(int, input().split()))
    arr[x-1][y-1] = x*y

for row in arr:
    for ele in row:
        print(ele, end=' ')
    print()