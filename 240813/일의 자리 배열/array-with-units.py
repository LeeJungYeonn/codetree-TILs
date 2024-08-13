arr = list(map(int, input().split()))

new = 0
for i in range(3, 11):
    new = arr[-1] + arr[-2]
    new %= 10
    arr.append(new)

for i in range(len(arr)):
    print(arr[i], end=' ')