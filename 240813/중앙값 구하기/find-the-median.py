a, b, c = map(int, input().split())

median = 0
if a > b:
    if b > c:
        median = b
    if c > a:
        median = a
if a > c:
    if c > b:
        median = c
    if b > a:
        median = a
if b > c:
    if c > a:
        median = c
    if a > b:
        median = b

print(median)