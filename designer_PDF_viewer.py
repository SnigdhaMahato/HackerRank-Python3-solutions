import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    highest = 0
    for i in range(len(word)):
        if(highest < h[ord(word[i])-97]):
            highest = h[ord(word[i])-97]
    return highest*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()
