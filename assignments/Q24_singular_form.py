

def check_endings(verb):
    ending = ["o", "ch", "s", "sh", "x", "z"]

    for e in ending:
        if verb.endswith(e):
            return True
    return False


def get_singular_form(verb):

    if verb.endswith("y"):
        verb = verb.replace("y", "ies")
    elif check_endings(verb):
        verb += "es"
    else:
        verb += "s"

    return verb


if __name__ == "__main__":
    print(get_singular_form("try"))
    print(get_singular_form("brush"))
    print(get_singular_form("run"))
    print(get_singular_form("fix"))