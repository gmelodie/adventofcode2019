import numpy as np

def calculate_pattern(n, length):
    base_pattern = np.array([0, 1, 0, -1])

    # repeat
    pattern = np.repeat(base_pattern, n)
    # concatenate until same size as length
    pattern = np.tile(pattern, (length//len(pattern))+1)
    # remove excess elements from the end (minus one)
    pattern = pattern[:length+1]
    # remove first element
    return pattern[1:]


if __name__ == "__main__":
    signal = np.array([int(a) for a in list(input().strip())])
    signal = np.tile(signal, 10000)
    offset = 0
    for i in range(7):
        offset += signal[i] * 10**(6-i)

    nphases = 100
    for phase in range(nphases):
        # print("PHASE", phase+1)
        new_signal = np.zeros(len(signal))
        for i, digit in enumerate(signal):
            print(i, end=' ')
            pattern = calculate_pattern(i+1, len(signal))
            # print(pattern)
            new_signal[i] = int(abs(np.sum(signal*pattern))) % 10
            # print(new_signal[i])
        # print()
        signal = new_signal

    print(signal[offset:offset+8])

