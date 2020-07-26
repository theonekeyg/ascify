import sys
import os
import argparse

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
    parser = argparse.ArgumentParser(description="utility to ascify image files")
    parser.add_argument("-i", "--input", required=True, help="Input image file", dest="input")
    parser.add_argument("-o", "--output", help="If this option is provided, the output file will be \
                        used to store the result, stdout otherwise", dest="output")
    parser.add_argument("-c", action="store_const", const=True, default=False,
                        help="Whether do calculations in multiple threads or not", dest="concurrent")
    args = parser.parse_args()

    concurrent = args.concurrent
    grid = AsciiGrid(args.input, concurrent=concurrent)
    grid.start()
    if args.output is None:
        print(grid.ascii_grid)
    else:
        with open(args.output, "w") as f:
            f.write(grid.ascii_grad)

if __name__ == "__main__":
    main()
