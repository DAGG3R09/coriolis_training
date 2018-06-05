
def generate_n_characters(n, char):

    l = [char for i in range(n)]

    return ''.join(l)


if __name__ == "__main__":
    print(generate_n_characters(5, "*"))
    print(generate_n_characters(6, "1"))
    print(generate_n_characters(6, "12"))