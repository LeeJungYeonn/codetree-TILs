string = input()

str_len = len(string)
if str_len % 2 == 0:
    for i in range(str_len-1, -1, -2):
        print(string[i], end='')
else:
    for i in range(str_len-2, -1, -2):
        print(string[i], end='')