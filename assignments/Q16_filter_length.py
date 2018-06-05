
def filter_by_length(n, list1):

    return list(filter(lambda x: len(x) <= n, list1))

if __name__ == "__main__":
    l1 = ["hello", "my", "name", "is", "sufiyan"]
    l2 = ["hello....", "my", "name", "is", "sufiyan"]

    print(filter_by_length(5, l1))
    print(filter_by_length(3, l2))
