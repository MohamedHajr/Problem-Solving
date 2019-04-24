#!/bin/python3

import os
#
# Complete the twoStacks function below.
#


def twoStacks(limit, s1, s2):
    total = 0
    moves = []
    for _ in range(len(s1)):
        if total + s1[-1] > limit:
            break
        elem = s1.pop()
        total += elem
        moves.append(elem)

    max_moves = len(moves)
    curr_moves = max_moves
    while len(s2):
        if total + s2[-1] <= limit:
            total += s2.pop()
            curr_moves += 1
            if curr_moves > max_moves:
                max_moves = curr_moves
            continue
        if not len(moves):
            break
        elem = moves.pop()
        total -= elem
        curr_moves -= 1
    return max_moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, reversed(input().rstrip().split())))

        b = list(map(int, reversed(input().rstrip().split())))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
