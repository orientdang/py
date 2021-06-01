from pprint import pprint

import numpy as np


def all_none_zero():
    x = np.array([1, 2, 3, 4])
    print(np.all(x))
    print('-' * 60)
    x = np.array([0, 1, 2, 3])
    print(np.all(x))


def any_none_zeros():
    x = np.array([1, 0, 0, 0])
    print(np.any(x))

    print("=" * 60)

    x = np.array([0, 0, 0, 0])
    print(np.any(x))


def check_finiteness():
    a = np.array([1, 0, np.nan, np.inf])
    result = np.isfinite(a)
    print(np.isfinite(a))


def check_infineness():
    a = np.array([1, 0, np.nan, np.inf, -np.inf])
    print(np.isinf(a))


def check_nan():
    a = np.array([1, 0, np.nan, np.inf])
    print(np.isnan(a))


def comparision():
    x = np.array([3, 5])
    y = np.array([2, 5])
    greater = np.greater(x, y)
    greater_equal = np.greater_equal(x, y)
    less = np.less(x, y)
    less_equal = np.less_equal(x, y)

    print(greater)
    print(greater_equal)
    print(less)
    print(less_equal)


def determine_size():
    x = np.array([1, 7, 13, 105, 7, 8])
    print("Size of the memory occupied by the said array:")
    size = x.size
    itemsize = x.itemsize
    total_size = size * itemsize
    print(size, itemsize, total_size)


def create_arbitrary_array():
    zeros = np.zeros(10)
    ones = np.ones(10)
    fives = np.ones(10) * 5

    from_to = np.arange(30, 100)

    print(zeros)
    print(ones)
    print(fives)
    print(from_to)


def create_matrix():
    array = np.identity(3)
    print(array)


def gen_random():
    ran = np.random.normal(0, 1, 1)
    print(ran)


def three_by_four():
    arr = np.arange(10, 22).reshape((3, 4))
    for x in np.nditer(arr):
        print(x)


three_by_four()
