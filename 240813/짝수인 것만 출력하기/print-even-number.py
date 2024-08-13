n = int(input())
arr = list(map(int, input().split()))

even_arr = []

for e in arr:
    if e % 2 == 0:
        even_arr.append(e)

for e in even_arr:
    print(e, end=' ')