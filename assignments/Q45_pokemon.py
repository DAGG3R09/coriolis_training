from copy import deepcopy

all_pokemons = """
            audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
            cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
            girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
            kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
            nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
            porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
            sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
            tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
        """


def generate_dictionary(pokemons):
    poke_dict = dict()

    for pokemon in pokemons:
        if poke_dict.get(pokemon[0], None) == None:
            poke_dict[pokemon[0]] = [pokemon]
        else:
            poke_dict[pokemon[0]].append(pokemon)

    return poke_dict


def get_new_dict(poke_dict, pokemon, key):
    d = deepcopy(poke_dict)
    d[key].remove(pokemon)
    return d


def get_max_chain(chain, poke_dict):
    last_pokemon = chain[-1]
    last_char = last_pokemon[-1]

    possible_choices = poke_dict.get(last_char, [])

    if possible_choices == []:
        return chain

    chains = []
    for choice in possible_choices:
         chains.append(get_max_chain(chain+[choice], get_new_dict(poke_dict, choice, last_char)))

    return max(chains, key= len)


def create_chain(poke_dict, all_pokemon):
    max_chain = []
    for pokemon in all_pokemon:
        chain = get_max_chain([pokemon], get_new_dict(poke_dict, pokemon, pokemon[0]))

        print(pokemon, ":", chain)
        if len(max_chain) < len(chain):
            max_chain = chain

    return max_chain


if __name__ == "__main__":
    pokes = all_pokemons.strip().split()
    poke_dict = generate_dictionary(pokes)

    for key, item in poke_dict.items():
        print(key, ": ", item)

    print(create_chain(poke_dict, pokes))


    # output:
    #['machamp', 'petilil', 'landorus', 'scrafty', 'yamask', 'kricketune', 'emboar', 'registeel', 'loudred',
    # 'darmanitan', 'nosepass', 'simisear', 'relicanth', 'heatmor', 'rufflet', 'trapinch', 'haxorus', 'seaking',
    # 'girafarig', 'gabite', 'exeggcute', 'emolga', 'audino']


