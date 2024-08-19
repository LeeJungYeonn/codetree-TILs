A = input()
A += '0'

s = A[0]
cnt = 1
run_length = ''

for i in range(1, len(A)):
    if A[i] == s:
        cnt += 1
    else:
        run_length += (s + str(cnt))
        s = A[i]
        cnt = 1

print(len(run_length))
print(run_length)