arr = list(map(int, input().split()))
n = len(arr)

k = 0
for i in range(n):
    if arr[i] == 0:
        k = i
        break

print(arr[k-1] + arr[k-2] + arr[k-3])