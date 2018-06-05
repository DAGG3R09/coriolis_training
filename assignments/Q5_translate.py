from Q4_vowel import is_vowel


def translate(string):
    result = ""
    for s in string:
        if is_vowel(s) or s == ' ':
            result += s
        else:
            result += s + "o" + s

    return result


if __name__ == "__main__":
    print(translate("this is fun"))
    print("tothohisos isos fofunon")


