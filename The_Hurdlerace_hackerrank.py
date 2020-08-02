n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
height = list(map(int, input().rstrip().split()))
b = max(height)
if (b<k):
    print(0)
else:
    print(b-k)
