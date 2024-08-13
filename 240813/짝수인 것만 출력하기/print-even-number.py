n = int(input())
arr = list(map(int, input().split()))

even_arr = []

for ele in arr:
    if ele % 2 == 0:
        even_arr.append(ele)

for ele in even_arr:
    print(ele, end=' ')