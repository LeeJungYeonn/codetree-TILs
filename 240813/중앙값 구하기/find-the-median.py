a, b, c = map(int, input().split())

if a > b:
    if c > a: # c > a > b
        print(a)
    elif b > c: # a > b > c
        print(b)
    else: # a > c > b
        print(c)
else:
    if c > b: # c > b > a
        print(b)
    elif a > c: # b > a > c
        print(a)
    else: # b > c > a
        print(c)