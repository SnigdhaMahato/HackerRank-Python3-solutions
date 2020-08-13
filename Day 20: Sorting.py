import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            newVal = a[j]
            a[j] = a[j+1]
            a[j+1] = newVal
            numSwaps += 1

    if (numSwaps == 0):
        break

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a) - 1]))
