age_sum = 0
num = 0
while True:
    age = int(input())
    if 20 <= age <= 29:
        age_sum += age
        num += 1
    else:
        break

age_mean = age_sum / num
print(f"{age_mean:.2f}")