# -*- coding: utf-8 -*-

key = {"merry":"god", "christmas":"jul", "and":"och",
        "happy":"gott", "new":"nytt", "year":"år"}


def translate(words):
    return [key.get(w, w) for w in words]


if __name__ == "__main__":
    english_words = "merry christmas".split()
    l2 = "happy new year".split()
    print(translate(english_words))
    print(translate(l2))