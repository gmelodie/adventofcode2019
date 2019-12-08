import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 spaceimage.py <width> <height>")
        exit(1)

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    image = [int(a) for a in list(input())]

    layerlen = int(width*height)
    layers = int(len(image)/layerlen)
    print("LAYERS:", layers)

    info = []
    for i in range(layers):
        meta = {0:0, 1:0, 2:0}
        for j in range(layerlen):
            if image[i*layerlen + j] >= 0 and image[i*layerlen + j] <= 2:

                meta[image[i*layerlen + j]] += 1
        info.append(meta)

    minmeta = info[0]
    for meta in info:
        if meta[0] < minmeta[0]:
            minmeta = meta

    print(minmeta)
    print(minmeta[1]*minmeta[2])

    #print(image)
