input_str = input()
trg_str = input()

N = len(input_str)
start = 0

M = len(trg_str)

for i in range(N - M + 1):
    all_same = True
    for j in range(M):
        if input_str[i + j] != trg_str[j]:
            all_same = False
    
    if all_same == True:
        start = i
        break
    else:
        start = -1

print(start)