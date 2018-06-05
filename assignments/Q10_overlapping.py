
def is_overlapping (l1, l2):

    for le1 in l1:
        for le2 in l2:
            if le1 == le2:
                return True
    return False


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 6, 7, 8, 9]
    l3 = [6, 7, 8, 9, 10]

    print(is_overlapping(l1, l2))
    print(is_overlapping(l1, l3))