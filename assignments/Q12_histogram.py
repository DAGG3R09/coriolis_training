from Q11_generate_chars import generate_n_characters

character = "*"


def histogram(list):
    for l in list:
        print(generate_n_characters(l, character))


if __name__ == "__main__":
    histogram([1, 2, 3, 4, 5])