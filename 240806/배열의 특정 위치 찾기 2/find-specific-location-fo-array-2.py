arr = list(map(int, input().split()))

arr1 = arr[::2]
arr2 = arr[1::2]

sum1 = sum(arr1)
sum2 = sum(arr2)

if sum1 > sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)