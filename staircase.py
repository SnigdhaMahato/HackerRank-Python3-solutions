import math
import os
import random
import re
import sys

n = int(input())
def staircase(n):
    for stairs in range(1, n+1):
         print(("#" * stairs).rjust(n))

staircase(n)
