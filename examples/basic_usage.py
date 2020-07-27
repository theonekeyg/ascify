#!/usr/bin/env python3
from ascify.grid import AsciiGrid

def main():
    grid = AsciiGrid("leader.jpg", step=3, size=(250, 400))
    grid.start()
    print(grid)

if __name__ == "__main__":
    main()
