import sys
import os
import numpy as np
from PIL import Image

from grid import AsciiGrid
from renditions import *

# import warnings
# warnings.filterwarnings("error")

ascii_tokens = {
    "@": 200,
    "#": 155,
    "&": 100,
    "*": 50,
    ".": 0
}



def main():
    grid = AsciiGrid("./leader.jpg")
    grid.ascify()
    print(grid.ascii_grid)

if __name__ == "__main__":
    main()
