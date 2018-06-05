

def using_loops(words):

    result = []
    for w in words:
        result.append(len(w))

    return result


def using_list_comprehension(words):
    return [len(w) for w in words]


def using_map(words):
    return list(map(len, words))


if __name__ == "__main__":
    l = ["Hello!", "this", "is", "Sufiyan", "Parkar"]
    print(l)
    print("Loops: ", using_loops(l))
    print("Map: ", using_map(l))
    print("List Comprehension: ", using_list_comprehension(l))