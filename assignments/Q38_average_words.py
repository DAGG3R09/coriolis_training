

def average_words(filename):

    word_count = 0
    word_length_count = 0
    for line in open(filename, "r"):
        words = line.strip().split()
        word_length_count += sum(map(len, words))
        word_count += len(words)

    return word_length_count/word_count


if __name__ == "__main__":
    print(average_words("files/hapax.txt"))