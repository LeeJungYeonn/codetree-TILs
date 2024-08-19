numbers = [
    int(input()) for _ in range(5)
]

true = True
for n in numbers:
    if n % 3 != 0:
        true = False

if true:
    print(1)
else:
    print(0)