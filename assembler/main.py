import sys
from assembler import *

def main():
    filename = sys.argv[1]
    assembler = Assembler(filename)
    assembler.read_file()
    assembler.parse_out()


if __name__ == "__main__":
    sys.exit(main())