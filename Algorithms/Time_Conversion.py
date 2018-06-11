# Author: Sinclair Liang
# Github: github.com/sinclairliang

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    
    if s[-2:] == "AM":
        if(int(s[0:2]) == 12):
            return "00"+s[2:len(s)-2]
        return s[0:len(s)-2]
    else:
        if(int(s[0:2]) == 12):
            return s[0:len(s)-2]
        military_time_hour = str(int(s[0:2])+12)
        military_time_hour += s[2:-2]
        return military_time_hour

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
