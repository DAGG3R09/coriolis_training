from re import sub


def corrector(string):
    string = sub('\.', '. ', string)
    string = sub(' +', ' ', string)

    return string


if __name__ == "__main__":
    s = "This   is  very funny  and    cool.Indeed!"

    print(corrector(s))