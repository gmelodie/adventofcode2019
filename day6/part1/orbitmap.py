import sys

if __name__ == "__main__":
    orbits = {}
    for line in sys.stdin:
        planet1, planet2 = line.strip().split(")")
        orbits[planet2] = planet1 # planet2 orbits planet1
    print(orbits)

    total_orbits = 0
    for planet in orbits.keys():
        while planet in orbits.keys():
            total_orbits += 1
            planet = orbits[planet]

    print(total_orbits)
