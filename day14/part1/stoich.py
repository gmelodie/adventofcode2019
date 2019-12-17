import sys
import re


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
# required to produce <quantity> of <material>
def cost(quantity, material, reactions, leftover):
    if material == 'ORE': # base case
        return quantity

    # Get from leftover
    while quantity > 0 and leftover[material] > 0:
        quantity -= 1
        leftover[material] -= 1

    # Careful: 10000 is just a big number
    # (might not be big enough)
    for i in range(10000):
        if reactions[material]['quantity'] * i >= quantity:
            break

    leftover[material] += reactions[material]['quantity']*i - quantity

    total_ore = 0
    for amount, ingredient in reactions[material]['ingredients']:
        total_ore += cost(i*amount, ingredient, reactions, leftover)


    # TODO: calculate leftover
    print("Will need", total_ore, "to produce", quantity, \
          "of", material)
    return total_ore


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 stoich.py <input_file>")
        exit(0)

    # read input
    reactions = read_reactions(sys.argv[1])
    print(reactions)

    leftover = {}
    for material in reactions.keys():
        leftover[material] = 0

    # calculate best reaction list
    print(cost(1, 'FUEL', reactions, leftover))
