from math import sqrt

T = int(input())

def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n) + 1)):
            if (n % i is 0) and (i != n):
               return False
        return True

for _ in range(T):
    n = int(input())
    if n >= 2 and prime(n):
        print('Prime')
    else:
        print('Not prime')
