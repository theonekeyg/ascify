from sys import argv
import os
import numpy as np
from PIL import Image

ascii_tokens = {
    "@": 200,
    "#": 155,
    "&": 100,
    "*": 50,
    ".": 0
}


class Grid:
    def __init__(self, impath, step=5, size=(500, 500)):
        if len(size) != 2:
            raise ValueError("provided size got invalid format, expected length "
                            f"of 2, but received {len(size)}")
        if not os.path.exists(impath):
            raise FileNotFoundError(f"File by provided path '{impath}' "
                                     "wasn't found")
        self.step       = step
        self.y          = size[0] // step
        self.x          = size[1] // step
        self.img        = Image.open(impath)
        self.img        = self.img.resize(size, resample=Image.BILINEAR)
        self.img        = np.array(self.img)
        self.ascii_grid = ""

    def ascify(self):
        for i in range(self.y):
            for j in range(self.x):
                for char, threshold in ascii_tokens.items():
                    # print(self.img[i*self.step:(i+1)*self.step,
                    #                j*self.step:(j+1)*self.step])

                    if (self.img[i*self.step:(i+1)*self.step,
                                 j*self.step:(j+1)*self.step].mean() >= threshold):
                        self.ascii_grid += char
                        break

            self.ascii_grid += "\n"

def main():
    grid = Grid("./leader.jpg")
    grid.ascify()
    print(grid.ascii_grid)

if __name__ == "__main__":
    main()
