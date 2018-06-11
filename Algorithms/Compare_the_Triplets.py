# Author: Sinclair Liang
# Github: github.com/sinclairliang
#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    a = [a0, a1, a2]
    b = [b0, b1, b2]
    # print ("compare:" + compare)
    result_a = result_b = 0
    for i in range(3):
        if a [i] > b [i]:
            # print (str(compare [i]))
            #print (str(compare [i]) + "is comparing with" + str(compare [i+2]))
            result_a += 1    
        elif a [i] < b [i]:
            # print (str(compare [i]) + "is comparing with" + str(compare [i+2]))
            result_b += 1
        else:
            pass
            
    return (result_a, result_b)
        
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
