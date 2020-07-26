import sys
import os
import numpy as np
from PIL import Image

from renditions import default_rendition

class AsciiGrid:
    def __init__(self, impath, step=5, size=(350, 600), rendition=None):
        if len(size) != 2:
            raise ValueError("provided size got invalid format, expected length "
                             f"= 2, but received: {len(size)}")
        if not os.path.exists(impath):
            raise FileNotFoundError(f"File by provided path '{impath}' "
                                     "wasn't found")
        if rendition is None:
            self.rendition = default_rendition
        else: self.rendition = rendition

        self.step       = step
        self.y          = size[0] // step
        self.x          = size[1] // step
        self.img        = Image.open(impath)
        self.img        = self.img.resize(size[::-1], resample=Image.BILINEAR)
        self.img        = np.array(self.img)
        self.ascii_grid = ""

    def ascify(self):
        for i in range(self.y):
            for j in range(self.x):
                img_slice = self.img[i*self.step:(i+1)*self.step,
                                     j*self.step:(j+1)*self.step]
                sys.stdout.write(self.rendition(img_slice))

            # self.ascii_grid += "\n"
            sys.stdout.write("\n")
