import sys
import copy
import numpy as np


def update_velocities(moons, velocities):
    for i in range(len(moons)):
        for j in range(len(moons)):
            if j == i:
                continue
            if moons[i] < moons[j]:
                velocities[i] += 1
            elif moons[i] > moons[j]:
                velocities[i] -= 1


def update_positions(moons, velocities):
    for i in range(len(moons)):
        moons[i] += velocities[i]


def back_to_beginning(orig_moons, orig_velocities, velocities, moons):
    for i in range(len(moons)):
        if orig_moons[i] != moons[i] or orig_velocities[i] != velocities[i]:
            return False
    return True


def simulate_axis(moons, axis):
    new_moons = []
    new_velocities = []
    for moon in moons:
        new_moons.append(moon[axis])
        new_velocities.append(0)

    orig_moons = copy.deepcopy(new_moons)
    orig_velocities = copy.deepcopy(new_velocities)

    nsteps = 0
    while True:
        nsteps += 1

        update_velocities(new_moons, new_velocities)
        update_positions(new_moons, new_velocities)

        if back_to_beginning(orig_moons, orig_velocities, \
                             new_velocities, new_moons):
            break

    return nsteps


if __name__ == "__main__":
    moons = []
    for line in sys.stdin:
        moons.append([int(a) for a in line.strip().split()])

    least_x = simulate_axis(moons, 0)
    least_y = simulate_axis(moons, 1)
    least_z = simulate_axis(moons, 2)


    print(least_x)
    print(least_y)
    print(least_z)
    repeat = np.lcm.reduce([least_x, least_y, least_z])
    print("Took", repeat, "steps to get back at the beginning")

