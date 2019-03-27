#!/bin/python3

import os
import random
from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for l, r, k in queries:
        arr[l - 1] += k 
        arr[r] -=k
    return max(accumulate(arr))

def calcPrefixSumArray(arr, n):
    for i in range(1, n):
        arr[i] += arr[i - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
