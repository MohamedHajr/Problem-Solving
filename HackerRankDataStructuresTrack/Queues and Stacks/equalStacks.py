#!/bin/python3

import os

#
# Complete the equalStacks function below.
#
#This one TimesOut
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)

    minimum = min(s1, s2, s3)
    while s1 != minimum or s2 != minimum or s3 != minimum:
        while s1 >  minimum :
            del h1[0]
            s1 = sum(h1)
            if s1 < minimum:
                minimum = s1
        while s2 > minimum :
            del h2[0]
            s2 = sum(h2)
            if s2 < minimum:
                minimum = s2
        while s3 > minimum:
            del h3[0]
            s3 = sum(h1)
            if s3 < minimum:
                minimum = s3
    return minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
