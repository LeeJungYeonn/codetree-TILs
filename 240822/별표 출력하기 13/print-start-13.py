n = int(input())

num1 = n
num2 = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(num1):
            print('* ', end='')
        print()
        num1 -= 1
    else:
        for j in range(num2):
            print('* ', end='')
        print()
        num2 += 1

for i in range(n, 2*n):
    if i % 2 == 0:
        for j in range(num1):
            print('* ', end='')
        print()
        num1 -= 1
    else:
        for j in range(num2):
            print('* ', end='')
        print()
        num2 += 1