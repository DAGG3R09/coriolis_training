from string import ascii_lowercase

lowercase = set(ascii_lowercase)

def normalize_text(text):
    text = text.lower()
    string = list(filter(lambda x: x in lowercase or x == ' ', text))
    return string


def hapax(filename):

    for line in open(filename, "r"):
        # text = normalize_text(line)
        line = line.lower()
        words = line.strip().split()

        chars = dict()
        for word in words:
            if chars.get(word, None) == None:
                chars[word] = 1
            else:
                chars[word] += 1

    hapaxes = []
    for word, count in chars.items():
        if count == 1:
            hapaxes.append(word)
    return hapaxes


if __name__ == "__main__":
    fname = "files/hapax.txt"
    print(hapax(fname))