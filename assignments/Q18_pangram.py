
from string import ascii_lowercase

lowercase = set(ascii_lowercase)


def pangram_recognizer(string):
    string = string.lower()
    string = list(filter(lambda x: x in lowercase, string))

    # alphas = dict()
    # for s in string:
    #     alphas[s] = True

    s = set(string)
    if len(s) == 26:
        return True
    return False


if __name__ == "__main__":
    s1 = "Go hang a salami I'm a lasagna hog."
    s2 = "Lisa Bonet ate no basil"
    s3 = "The quick brown fox jumps over the lazy dog."

    print(pangram_recognizer(s1))
    print(pangram_recognizer(s2))
    print(pangram_recognizer(s3))
