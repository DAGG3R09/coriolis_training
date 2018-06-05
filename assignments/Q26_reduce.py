from functools import reduce
from Q1_max import max2


def max_of_list(list):
    return reduce(max2, list)


if __name__ == "__main__":
    print(max_of_list([1, 2, 3, 4, 5, 6]))
    print(max_of_list([6, 23, 4, 1, 5, 10]))
    print(max_of_list([23, 4, 1, 5, 10]))
