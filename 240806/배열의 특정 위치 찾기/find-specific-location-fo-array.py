arr = list(map(int, input().split()))

arr1 = arr[1::2]

n_arr = len(arr)
n_arr2 = 0
sum_arr2 = 0
for i in range(0, n_arr):
    if (i+1) % 3 == 0:
        n_arr2 += 1
        sum_arr2 += arr[i]
mean = sum_arr2 / n_arr2

print(sum(arr1), end=' ')
print(f"{mean:.1f}")