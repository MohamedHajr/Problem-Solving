#!/bin/python3

import math
import os
import random
import re
import sys

def get_msb(n):
    index = -1 
    while n != 0:
        index += 1
        n >>= 1
    return index

def counter_game(num):
    counter = 0
    while num != 1:
        print(bin(num))
        if num & (num - 1) == 0:
            num //= 2
        else:
            msb = get_msb(num)

            num -= 1 << msb
        counter += 1
    return "Richard" if counter % 2 == 0 else "Louise"


print(counter_game(132))

