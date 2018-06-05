
vowels = set(['a','e', 'i', 'o', 'u'])

def is_vowel(char):
    if char in vowels:
        return True
    return False


if __name__ == "__main__":
    print(is_vowel("a"))
    print(is_vowel("c"))
    print(is_vowel("e"))
    print(is_vowel("z"))
