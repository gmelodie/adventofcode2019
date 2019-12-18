import numpy as np


if __name__ == "__main__":
    raw_signal = input().strip()
    signal = [int(a) for a in list(raw_signal)]

    offset = int(raw_signal[:7], 10)

    signal = signal * 10000

    nphases = 100
    for phase in range(nphases):
        print("PHASE", phase+1)

        partial_sum = sum(signal[j] for j in \
                          range(offset, len(signal)))

        for i in range(offset, len(signal)):
            t = partial_sum
            partial_sum -= signal[i]
            signal[i] = int(abs(t)) % 10

        print(signal[offset:offset+8])

