#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def map_path_to_num(path):
    if path == 'D':
        return -1
    return 1


def countingValleys(steps, path):
    from itertools import accumulate

    # Write your code here
    path_nums = map(map_path_to_num, path)
    cum = list(accumulate(path_nums))
    valley = 0
    for i in range(steps):
        if cum[i] == 0 and cum[i - 1] == -1:
            valley += 1
    return valley


if __name__ == '__main__':
    fptr = sys.stdout

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
