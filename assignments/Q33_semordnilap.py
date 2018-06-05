
def get_words(filename):
    words = []
    for l in open(filename):
        words += l.strip().split(' ')
    return words

def check_semordnilap(filename):
    words = get_words(filename)
    words_set = set(words)

    pairs = []
    for w in words:
        if w[::-1] in words_set:
            pairs.append((w, w[::-1]))
            words_set.remove(w)
            words_set.remove(w[::-1])

    return pairs


if __name__ == "__main__":
    print(check_semordnilap("files/semordnilap.txt"))