n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(n):
        arr[j][i] = num
        num += 1

for row in arr:
    for ele in row:
        print(ele, end=' ')
    print()