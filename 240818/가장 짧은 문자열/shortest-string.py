old = len(input())

shortest = old
longest = old

for _ in range(2):
    new = len(input())
    if new > longest:
        longest = new
    elif new < shortest:
        shortest = new
    old = new

print(longest - shortest)