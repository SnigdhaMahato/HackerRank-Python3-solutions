n = int(input())
count = 0
maxCount = 0
while (n>0):
    rem = n % 2
    if (rem == 1):
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 0
    n = n // 2

print(maxCount)
