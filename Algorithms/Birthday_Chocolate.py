# Author: Sinclair Liang
# Github: github.com/sinclairliang
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    times = 0
    for x in range(len(s)):
        if(each_x_sum(s,m,x) == d):
            times += 1
    return times
    
def each_x_sum(s, m, start):
    sum = 0
    try:
        for x in range(m):
            sum += s[start+x]
    except:
        pass
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    # How many squares
    s = list(map(int, input().rstrip().split()))
    # Numbers on each squares
    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
