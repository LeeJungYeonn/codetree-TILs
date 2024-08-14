arr = list(map(int, input().split()))

for _ in range(3, 11):
    e = arr[-1] + 2*arr[-2]
    arr.append(e)

for e in arr:
    print(e, end=' ')