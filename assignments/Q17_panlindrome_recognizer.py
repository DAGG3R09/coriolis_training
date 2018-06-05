from string import ascii_lowercase

lowercase = set(ascii_lowercase)


def palindrome_recognizer(string):
    string = string.lower()
    string = list(filter(lambda x: x in lowercase, string))

    if(string == string[::-1]):
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = "Go hang a salami I'm a lasagna hog."
    s2 = "Lisa Bonet ate no basil"
    s3 = "Sufiyan Parkar"

    print(palindrome_recognizer(s1))
    print(palindrome_recognizer(s2))
    print(palindrome_recognizer(s3))
