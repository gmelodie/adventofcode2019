import sys

def dist(orbits, start, end):
    d = 0
    while start != end:
        start = orbits[start]
        d += 1

    if start != end:
        print("Error: could't find path")

    return d

def find_fork(orbits, planet):
    fork = []
    while planet in orbits:
        fork.append(planet)
        planet = orbits[planet]

    fork.append(planet) # get last planet
    return fork

def find_common_ancestor(orbits, fork1, fork2):
    for ancestor in fork1:
        if ancestor in fork2:
            return ancestor
    print("Error: couldn't find common ancestor")

if __name__ == "__main__":
    orbits = {}
    for line in sys.stdin:
        planet1, planet2 = line.strip().split(")")
        orbits[planet2] = planet1 # planet2 orbits planet1
    print(orbits)

    san_fork = find_fork(orbits, "SAN")
    print("SAN Fork", san_fork)
    you_fork = find_fork(orbits, "YOU")
    print("YOU Fork", you_fork)

    common_ancestor = find_common_ancestor(orbits, san_fork, you_fork)

    san_to_ancestor = dist(orbits, "SAN", common_ancestor)
    you_to_ancestor = dist(orbits, "YOU", common_ancestor)

    print(san_to_ancestor + you_to_ancestor - 2)
