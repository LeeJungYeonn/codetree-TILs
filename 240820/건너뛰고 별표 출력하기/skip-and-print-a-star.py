n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print('\n')

for i in range(n, 0, -1):
    for j in range(i-1, 0, -1):
        print('*', end='')
    print('\n')