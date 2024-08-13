n = int(input())

arr = []
cnt = 0
i = 1
while True:
    mul = n * i
    arr.append(mul)
    i += 1
    if mul % 5 == 0:
        cnt += 1
    if cnt >= 2:
        break

for e in arr:
    print(e, end=' ')