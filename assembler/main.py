"""Main program"""
import sys

from assembler import Assembler


def main():
    """Main instanciates an Assembler object"""
    filename = sys.argv[1]
    assembler = Assembler(filename)
    assembler.read_file()
    assembler.write()


if __name__ == "__main__":
    sys.exit(main())
