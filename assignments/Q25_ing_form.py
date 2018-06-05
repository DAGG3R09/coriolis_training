from Q4_vowel import is_vowel

special_words = ['see', 'be', 'flee', 'knee']


def make_ing_form(verb):
    if verb.endswith("ie"):
        verb = verb.replace("ie", "y")
        verb += "ing"
    elif verb.endswith("e"):
        if verb not in special_words:
            verb = verb.replace("e", "ing")
        else:
            verb += "ing"

    elif (
            len(verb) > 3
            and
            not is_vowel(verb[-3])
            and
            is_vowel(verb[-2])
            and
            not is_vowel(verb[-1])
        ):

            verb += verb[0:-1] + "ing"
    else:
        verb += "ing"

    return verb

if __name__ == "__main__":
    print(make_ing_form("go"))
    print(make_ing_form("brush"))
    print(make_ing_form("run"))
    print(make_ing_form("be"))
    print(make_ing_form("see"))
    print(make_ing_form("flee"))
    print(make_ing_form("knee"))
    print(make_ing_form("lie"))
    print(make_ing_form("move"))
    print(make_ing_form("hug"))