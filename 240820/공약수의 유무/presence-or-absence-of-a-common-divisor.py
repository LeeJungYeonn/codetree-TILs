a, b = tuple(map(int, input().split()))

exist = False
for n in range(a, b+1):
    if 1920 % n == 0 and 2880 % n == 0:
        exist = True
        break

if exist:
    print(1)
else:
    print(0)