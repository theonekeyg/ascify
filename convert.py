#!/usr/bin/env python3
import argparse

from ascify.grid import AsciiGrid

def main():
    parser = argparse.ArgumentParser(description="utility to ascify image files")
    parser.add_argument("-i", "--input", required=True, help="Input image file", dest="input")
    parser.add_argument("-o", "--output", help="If this option is provided, the output \
        file will be  used to store the result, stdout otherwise", dest="output")
    args = parser.parse_args()

    grid = AsciiGrid(args.input, size=(60, 120))
    grid.start()

    if args.output is None:
        print(grid)
    else:
        with open(args.output, "w") as f:
            f.write(grid)

if __name__ == "__main__":
    main()
