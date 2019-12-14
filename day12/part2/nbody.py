import sys


def update_velocity(i, moons, velocities):
    for j in range(len(moons)):
        if j == i:
            continue
        for coords in range(3):
            if moons[i][coords] < moons[j][coords]:
                velocities[i][coords] += 1
            elif moons[i][coords] > moons[j][coords]:
                velocities[i][coords] -= 1


def update_position(i, moons, velocities):
    moons[i][0] += velocities[i][0]
    moons[i][1] += velocities[i][1]
    moons[i][2] += velocities[i][2]


def potential_energy(moon):
    return abs(moon[0]) + abs(moon[1]) + abs(moon[2])


def kinetic_energy(velocity):
    return abs(velocity[0]) + abs(velocity[1]) + abs(velocity[2])


if __name__ == "__main__":
    nsteps = 1000

    moons = []
    velocities = []
    for line in sys.stdin:
        moons.append([int(a) for a in line.strip().split()])
        velocities.append([0,0,0])

    for step in range(nsteps):
        print("STEP", step)
        for i in range(len(moons)):
            update_velocity(i, moons, velocities)
        for i in range(len(moons)):
            update_position(i, moons, velocities)
            print(moons[i], velocities[i])

    total_energy = 0
    for i in range(len(moons)):
        pot = potential_energy(moons[i])
        kin = kinetic_energy(velocities[i])
        print(pot, kin)
        total_energy += (pot * kin)

    print(total_energy)

