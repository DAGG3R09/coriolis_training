from Q1_max import max2

def longest_word(words):
    lengths = map(len, words)
    maximum = reduce(max2, lengths)
    index = lengths.index(maximum)
    return words[index]

if __name__ == "__main__":
    l1 = ["hello", "my", "name", "is", "sufiyan"]
    l2 = ["hello....", "my", "name", "is", "sufiyan"]

    print(longest_word(l1))
    print(longest_word(l2))