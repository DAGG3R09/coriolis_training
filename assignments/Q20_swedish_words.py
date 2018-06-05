# -*- coding: utf-8 -*-

key = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}


def translate(words):
    return ' '.join([key.get(w, w) for w in words])


if __name__ == "__main__":
    l1 = ["merry", "christmas"]
    print(translate(l1))