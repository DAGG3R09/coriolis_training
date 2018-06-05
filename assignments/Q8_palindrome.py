from Q7_reverse_string import reverse_string


def is_palindrome(string):

    if string == "":
        return True

    if reverse_string(string) == string:
        return True
    return False


if __name__ == "__main__":
    l = "string"
    l2 = "ma'am"

    print(is_palindrome(l))
    print(is_palindrome(l2))