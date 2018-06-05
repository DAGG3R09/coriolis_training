

def length(item):
    i = 0
    for _ in item:
        i += 1
    return i


if __name__ == "__main__":
    print (length([1, 2, 3, 4, 5, 6]))
    print (length([]))
    print (length("1234567789"))