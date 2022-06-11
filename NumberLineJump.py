'''
In this program we will see wheather two kangaroos will meet at a point at same time or not.
You have to give starting points and speed(m/jump) of both kangaroos as a input.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
If it is possible, return YES, otherwise return NO.
'''

x1,v1,x2,v2 = list(map(int,input('enter values:').split()))

if x1 > x2:     # It means kangaroo2 is started first.
    # If speed of kangaroo2 is greater than speed of kangaroo1 then only kangaroo2 can catch kargaroo1.otherwise it cann't catch.
    if v2 > v1: 
        if (x1-x2)%(v2-v1) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')

elif x2 > x1:       # It menas kangaroo1 is started first.
    if v1 > v2:
        if (x2-x1)%(v1-v2) == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')
else:
    print('No')

#       INPUT               OUTPUT
# 1817 9931 8417 190          NO
# 0 3 4 2                     YES
# 0 2 5 3                     NO

'''
HACKER  RANK SOLUTION:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    if x1 > x2:
        if v2 > v1:
            if (x1-x2)%(v2-v1) == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
        
    elif x2 > x1:
        if v1 > v2:
            if (x2-x1)%(v1-v2) == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

'''