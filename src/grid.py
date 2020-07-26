import sys
import os
import threading
import numpy as np
from PIL import Image

from renditions import default_rendition

class AsciiGrid:
    def __init__(self, impath, step=5, size=(350, 600), rendition=None, concurrent=False):
        if len(size) != 2:
            raise ValueError("provided size got invalid format, expected length "
                             f"= 2, but received: {len(size)}")
        if not os.path.exists(impath):
            raise FileNotFoundError(f"File by provided path '{impath}' "
                                     "wasn't found")
        if rendition is None:
            self.rendition = default_rendition
        else: self.rendition = rendition

        if concurrent:
            self.n_threads = os.cpu_count() if os.cpu_count() is not None else 4
            self.threads      = []
            self.shared_grids = ["" for _ in range(self.n_threads)]
            for i in range(self.n_threads):
                th = threading.Thread(target=self.th_ascify, args=(i,))
                self.threads.append(th)
        else: self.n_threads = 1

        self.concurrent   = concurrent
        self.step         = step
        self.y            = size[0] // step // self.n_threads
        self.x            = size[1] // step
        self.img          = Image.open(impath).resize(size[::-1], resample=Image.BILINEAR)
        self.img          = np.array(self.img)
        self.ascii_grid   = ""

    def start(self):
        if self.concurrent:
            self.y += 1
            for th in self.threads:
                th.start()
                th.join()
            self.ascii_grid = self.ascii_grid.join(self.shared_grids)
        else:
            self.ascify();

    def ascify(self):
        for i in range(self.y):
            for j in range(self.x):
                img_slice = self.img[i*self.step:(i+1)*self.step,
                                     j*self.step:(j+1)*self.step]
                self.ascii_grid += self.rendition(img_slice)
            self.ascii_grid += "\n"

    def th_ascify(self, tid):
        for i in range(self.y*tid, self.y*(tid+1)):
            for j in range(self.x):
                img_slice = self.img[i*self.step:(i+1)*self.step,
                                     j*self.step:(j+1)*self.step]
                self.shared_grids[tid] += self.rendition(img_slice)
            self.shared_grids[tid] += "\n"
