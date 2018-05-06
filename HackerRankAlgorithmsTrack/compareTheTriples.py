#!/bin/python3

import os
import sys

def compare(a, b):
    if a > b : return (1,0)
    elif a < b : return (0, 1)
    else : return (0,0)
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    return map(sum, zip(*[compare(a0, b0), compare(a1, b1), compare(a2, b2)]))

    
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


