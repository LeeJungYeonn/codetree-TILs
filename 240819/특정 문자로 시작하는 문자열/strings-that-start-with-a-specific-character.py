n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

start = input()

cnt = 0
arr2 = []
for ele in arr:
    if ele[0] == start:
        cnt += 1
        arr2.append(ele)

len_arr = 0
for ele in arr2:
    len_arr += len(ele)
mean = len_arr / cnt

print(f"{cnt} {mean:.2f}")