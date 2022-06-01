def finalMarks(n,initialMarks):
    roundMarks = []
    j = 0
    for i in range(n):
        for k in range(1,11):
            j = initialMarks[i] + k
            if initialMarks[i] < 38:
                roundMarks.append(initialMarks[i])
                break
            elif j%5 == 0:
                if j-initialMarks[i] < 3:
                    roundMarks.append(j)
                    break
                else:
                    roundMarks.append(initialMarks[i])
                    break
    print(roundMarks)


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
        finalMarks = []
        j = 0
        for i in range(grades_count):
            for k in range(1,11):
                j = grades[i] + k
                if grades[i] < 38:
                    finalMarks.append(grades[i])
                    break
                elif j%5 ==0:
                    if j-grades[i] < 3:
                        finalMarks.append(j)
                        break
                    else:
                        finalMarks.append(grades[i])
                        break
        return finalMarks

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