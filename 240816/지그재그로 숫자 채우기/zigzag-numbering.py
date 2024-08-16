n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0
for i in range(m):
    if i % 2 == 0: # m은 전체 열 개수, i가 각 행!!!
        for j in range(n):
            arr[j][i] = num
            num += 1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num += 1

for row in arr:
    for ele in row:
        print(ele, end=' ')
    print()