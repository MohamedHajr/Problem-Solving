#!/bin/python3

import math
import os

# Complete the isBalanced function below.


def isBalanced(s):
    if len(s) % 2 != 0:
        return 'NO'
    midPoint = int(len(s) / 2)
    stack = []
    for index in range(midPoint):
        stack.append(s[index])
    for rightBracket in s[midPoint:]:
        leftBracket = stack.pop()
        if rightBracket == '}':
            if not leftBracket == '{':
                return 'NO'
        elif rightBracket == ')':
            if not leftBracket == '(':
                return 'NO'
        elif rightBracket == ']':
            if not leftBracket == '[':
                return 'NO'
        else:
            return 'NO'
    return 'YES'


def isBalanced(s):
    if len(s) % 2 != 0:
        return 'NO'
    stack = []
    for bracket in s:
        if bracket == '}':
            if not stack.pop() == '{':
                return 'NO'
        elif bracket == ')':
            if not stack.pop() == '(':
                return 'NO'
        elif bracket == ']':
            if not stack.pop() == '[':
                return 'NO'
        else:
            stack.append(bracket)
    
    if len(stack) != 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
