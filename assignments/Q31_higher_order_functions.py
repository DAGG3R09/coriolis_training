from Q1_max import max2

def map_func(func, list):
    return [func(l) for l in list]


def filter_func(func, list):
    return [l for l in list if func(l)]


def reduce_func(func, list):
    if len(list) == 0:
        return
    elif len(list) == 1:
        return list[0]

    res = func(list[0], list[1])

    for element in list[2:]:
        res = func(res, element)

    return res


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = ["hello", "my", "name", "is", "sufiyan"]

    print("length of words Using map: ", map_func(len, l2))
    print("Only Even Using filter: ", filter_func(lambda x: x%2==0, l1))
    print("Max Using reduce: ", reduce_func(max2, l1))