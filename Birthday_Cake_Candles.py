import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    count = 0
    tallest = max(ar)
    for i in range(len(ar)):
        if(ar[i] == tallest):
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()