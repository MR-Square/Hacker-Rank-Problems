from tkinter.font import ROMAN


def finalMarks(n,initialMarks):
    roundMarks = []
    for i in range(n):
        if initialMarks[i] < 38:
            roundMarks.append(initialMarks[i])
        elif ((initialMarks[i]//5+1)*5)-initialMarks[i] < 3:
            roundMarks.append(((initialMarks[i]//5+1)*5))
        else:
            roundMarks.append(initialMarks[i])
    
    print(roundMarks)




if __name__ == "__main__":

    n = int(input('enter number of students::'))
    marks = []
    for _ in range(n):
        marks.append(int(input('enter marks:')))

    finalMarks(n,marks)




'''
HACKER RANK SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades_count,grades):
        roundMarks = []
    for i in range(n):
        if initialMarks[i] < 38:
            roundMarks.append(initialMarks[i])
        elif ((initialMarks[i]//5+1)*5)-initialMarks[i] < 3:
            roundMarks.append(((initialMarks[i]//5+1)*5))
        else:
            roundMarks.append(initialMarks[i])

    print(roundMarks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades_count,grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

'''