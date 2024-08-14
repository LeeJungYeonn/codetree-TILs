N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

for e in arr:
    if e % 2 == 1 and e % 3 == 0:
        print(e)