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
if b > a:
    if a > c:
        median = a
    if c > b:
        median = b
if b > c:
    if c > a:
        median = c
    if a > b:
        median = b
if c > a:
    if a > b:
        median = a
    if b > c:
        median = c
if c > b:
    if b > a:
        median = b
    if a > c:
        median = c

print(median)