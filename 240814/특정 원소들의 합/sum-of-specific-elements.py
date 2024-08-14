arr = []

for _ in range(4):
    row = list(map(int, input().split()))
    arr.append(row)

sum = 0
for i in range(4):
    for j in range(0,i+1):
        sum += arr[i][j]

print(sum)