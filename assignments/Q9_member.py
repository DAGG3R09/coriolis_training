
def is_member(element, list):

    for le in list:
        if le == element:
            return True

    return False


if __name__ == "__main__":
    l = ["aam", "aab", "aac", "aaaaad", "aaavc"]

    print(l)
    print("aac ->", is_member("aac", l))
    print("aad ->", is_member("aad", l))
