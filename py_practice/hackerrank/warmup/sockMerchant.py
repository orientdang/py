#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    word_freq = [ar.count(n) for n in ar]
    freq = set(list(zip(ar, word_freq)))
    return sum([i[1] // 2 for i in freq])


if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
