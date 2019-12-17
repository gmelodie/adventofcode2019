import sys
import math
import re
import copy


def read_reactions(filename):
    reactions = {}
    with open(sys.argv[1]) as fp:
        for line in fp:
            split_line = re.split(', | => | ', line.strip())
            reactions[split_line[-1]] = {
                'quantity': int(split_line[-2]),
                'ingredients': [],
            }
            i = 0
            while i < len(split_line)-2:
                reactions[split_line[-1]]['ingredients']\
                .append((int(split_line[i]), split_line[i+1]))
                i += 2

    return reactions


# Calculate the minimum amount of ORE
# required to produce <fuel_amount> of FUEL
def cost(fuel_amount, reactions):
    if fuel_amount <= 0:
        print("fuel_amount must be positive, got", fuel_amount)
        exit(1)

    required = {}
    required['FUEL'] = fuel_amount

    while any(required[key] > 0 and key != "ORE" for key in required):
        material = [k for k in required if required[k] > 0 and k != "ORE"][0]
        if required[material] < 0 or material == 'ORE':
            continue
        required_quant = required[material]
        minimum_prod_quant = reactions[material]['quantity']
        n_reactions = math.ceil(required_quant/minimum_prod_quant)

        required[material] -= n_reactions*minimum_prod_quant
        for ing in reactions[material]['ingredients']:
            if ing[1] in required:
                required[ing[1]] += ing[0]*n_reactions
            else:
                required[ing[1]] = ing[0]*n_reactions

    return required['ORE']


def bin_search(reactions):
    target = 1000000000000
    low = 0
    high = 200000000

    while low <= high:
        mid = (low+high)//2

        req_ore = cost(mid, reactions)
        print(mid, ":", req_ore)
        if req_ore > target:
            high = mid - 1
        elif req_ore < target:
            low = mid + 1
        else:
            return mid

    return high


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 stoich.py <input_file>")
        exit(0)

    # read input
    reactions = read_reactions(sys.argv[1])

    print(bin_search(reactions))


