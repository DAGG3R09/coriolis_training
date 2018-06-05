from assignments.Q1_max import max2


def max3(n1, n2, n3):
    return max2(max2(n1, n2), n3)


if __name__ == "__main__":
    print (max3(10, 12, 6))
    print (max3(12, 10, 21))
    print (max3(10, 10, 10))