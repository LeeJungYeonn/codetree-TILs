n = int(input())

num = 1
cnt = 0
while True:
    n //= num
    num += 1
    cnt += 1
    if n <= 1:
        break

print(cnt)