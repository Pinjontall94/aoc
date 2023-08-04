import pathlib, os
from .day01 import solve01


# Globals
inputs = pathlib.Path("inputs")


def input_file(filename):
    """Joins path labeled 'inputs' with a filename. Globals, shmobals."""
    return os.path.join(inputs, filename)


def main():
    print(solve01(input_file("example_day01.txt")))
    return 0

if __name__ == "__main__":
    main()
