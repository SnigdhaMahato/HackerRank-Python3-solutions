import math
import os
import random
import re
import sys

def aVeryBigSum(ar, n):
    total = 0
    for i in range(n):
        total += int(ar[i])
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(str, input().rstrip().split()))

    result = aVeryBigSum(ar, n)

    fptr.write(str(result) + '\n')

    fptr.close()
