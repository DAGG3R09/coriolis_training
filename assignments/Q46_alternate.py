

def load_words():
    s = set()
    for word in open("files/words.txt"):
        s.add(word.strip())

    return s


def create_word(word):
    new_word = ""
    i = 0

    while i < len(word):
        new_word += word[i]
        i += 2
    return new_word


def get_all_new_words(words):
    found_words = []

    for word in words:
        w1 = create_word(word)
        w2 = create_word(word[1:])

        if w1 in words and w2 in words:
            print(word, "makes ", w1, "and", w2)
        elif w1 in words:
            print(word, "makes ", w1)
        elif w2 in words:
            print(word, "makes ", w2)


if __name__ == "__main__":
    all_words = load_words()
    print()
    get_all_new_words(all_words)