import sys
import numpy as np
from PIL import Image


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 spaceimage.py <width> <height>")
        exit(1)

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    image = [int(a) for a in list(input())]

    layerlen = int(width*height)
    nlayers = int(len(image)/layerlen)
    print("LAYERS:", nlayers)

    image = np.array_split(image, nlayers)
    final_image = np.zeros(layerlen)
    for i in range(layerlen):
        for j in range(nlayers):
            if image[j][i] == 0 or image[j][i] == 1:
                final_image[i] = image[j][i]
                break
    print(image)

    final_image = 255 * (1.0 - final_image) # 0 -> 255
    final_image = final_image.reshape((height, width)).astype(np.uint8)
    print(final_image)
    img = Image.fromarray(final_image, mode='L')
    img.save("passwd.png")
