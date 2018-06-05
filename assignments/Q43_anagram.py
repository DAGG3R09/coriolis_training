from collections import Counter

def load_words():
    s = []
    for word in open("files/words.txt"):
        s.append(word.strip())

    return s


def create_hashmap(all_words):
    words = dict()
    for word in all_words:
        words[word] = Counter(word)

    return words


def get_largest_set(hash, all_words):
    all_sets = []

    length = len(all_words)
    while length != 0:
        anagram_set = [all_words[0]]
        count = hash[all_words[0]]

        all_words.remove(all_words[0])
        length -= 1

        j = 0
        while j < length:
            if count == hash[all_words[j]]:
                anagram_set.append(all_words[j])
                all_words.remove(all_words[j])
                length -= 1
            else:
                j +=1

        # print(anagram_set)
        all_sets.append(anagram_set)

    print(max(all_sets, key = len))

if __name__ == "__main__":
    all_words = load_words()
    hash = create_hashmap(all_words)
    get_largest_set(hash, all_words)
