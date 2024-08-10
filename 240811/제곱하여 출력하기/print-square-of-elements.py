n = int(input())

arr = list(map(int, input().split()))

new_arr = [e**2 for e in arr]
for e in new_arr:
    print(e, end=' ')