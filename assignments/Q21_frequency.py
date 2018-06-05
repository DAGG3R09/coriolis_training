

def char_freq(string):
    chars = dict()
    for char in string:
        if chars.get(char, None) == None:
            chars[char] = 1
        else:
            chars[char] += 1

    return chars


if __name__ == "__main__":
    print(char_freq("aabbsscasdsddd"))
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))
