# Author: Sinclair Liang
# Github: github.com/sinclairliang
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    number_of_pairs = 0
    length = n
    for i in range(len(ar)):
        for j in range(length):
            if(ar[i]+ar[j] == k):
                number_of_pairs += 1
        length -= 1
    return number_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
