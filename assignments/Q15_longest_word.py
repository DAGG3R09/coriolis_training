from Q14_list_to_lengths import list_lengths
from Q13_max_list import max_list

def longest_word(words):
    lengths = list_lengths(words)
    max = max_list(lengths)
    index = lengths.index(max)
    return words[index]


if __name__ == "__main__":
    l1 = ["hello", "my", "name", "is", "sufiyan"]
    l2 = ["hello....", "my", "name", "is", "sufiyan"]

    print(longest_word(l1))
    print(longest_word(l2))