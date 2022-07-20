# Plus Minus Problem
'''
In this problem we have to count total number of positve integers, negative intergers and
zeros. Then we have to find out the ratio of total numbers and length of array.
'''
#!/bin/python3
import math
import os
import random
import re
import sys


def plusMinus(arr):
    # Write your code here
    NoOfPositiveInteger = NoOfNegativeInteger = NoOfZeros  = 0
    
    for i in arr:
        if i > 0:
            NoOfPositiveInteger += 1
        elif i < 0:
            NoOfNegativeInteger += 1
        else:
            NoOfZeros += 1
            
    print('%.6f'%(NoOfPositiveInteger/len(arr)))
    print('%.6f'%(NoOfNegativeInteger/len(arr)))
    print('%.6f'%(NoOfZeros/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
