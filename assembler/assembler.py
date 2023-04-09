"""
Assembler class file. Imports to treat all instructions

"""

from dicts import type0_instructions as type0
from dicts import type1_instructions as type1
from dicts import type2_instructions as type2
from dicts import special_instructions as special
from dicts import registers as reg


class Assembler:

    """
    Assembler class. Main purpose is to translate instructions
    to machine code It takes an input file and creates
    (or modifies if exists) the file progfile.dat with the machine code

    """

    def __init__(self, file: str) -> None:

        """
        Save file and create instructions list

        """

        self.filename = file
        self.code = []

    def decode_register(self, register: str) -> str:

        """
        Returns the register binary translation

        """

        if register in reg:
            return reg[register]
        return "?"

    def decode_instruction(self, instr: str) -> str:

        """
        Returns the instruction binary translation
        based on its type

        """

        if instr in type0:
            return type0[instr]
        if instr in type1:
            return type1[instr]
        if instr in type2:
            return type2[instr]
        if instr in special:
            return special[instr]
        return "?"

    def read_file(self) -> None:

        """
        Reads all instructions from the input file
        and saves it on code[] list

        """

        with open(self.filename, "r", encoding='UTF-8') as file:
            line = file.readline()
            while line != "":
                line = line.strip().replace(",", "")
                if len(line) > 0 :
                    self.code += [line]
                line = file.readline()

    def parse(self, instruction: tuple) -> str:

        """
        Parses all instructions based on their types
        and returns the translation to binary form
        _op: opcode
        _rd: target register
        _r1: first operand register
        _r2: second operand register
        imm: immediate
        line: string with the instruction in binary form

        """

        # instruction[0] contains the instruction to be executed and translated
        if instruction[0] in type0:
            _op = self.decode_instruction(instruction[0])
            _rd = self.decode_register(instruction[1])
            _r1 = self.decode_register(instruction[2])

            # MOV, NOT, NEGA and NEGB instructions doesn't use three registers
            if len(instruction) == 4:
                _r2 = self.decode_register(instruction[3])
                # 6b opcode + 4b target register + 4b op1 + 4b op2 + 14b not used
                line = _op + _rd + _r1 + _r2 + "{:014b}".format(0)
            else :
                # Instruction is MOV, NOT, NEGA OR NEGB
                line = _op + _rd + _r1 + "{:018b}".format(0)

        elif instruction[0] in type1:
            _op = self.decode_instruction(instruction[0])
            _rd = self.decode_register(instruction[1])
            
            # LI instruction just needs a target register for the immediate
            if len(instruction) == 3:
                imm = int(instruction[2].replace("#",""))
                # 6b opcode + 4b target register + 4b not used + 18b immediate
                line = _op + _rd + "{:04b}".format(0) + "{:018b}".format(imm)
            else:
                _r1 = self.decode_register(instruction[2])
                imm = int(instruction[3].replace("#",""))
                # 6b opcode + 4b target register + 4b not used + 18b immediate
                line = _op + _rd + _r1 + "{:018b}".format(imm)

        elif instruction[0] in type2:
            _op = self.decode_instruction(instruction[0])
            imm = int(instruction[1].replace("#",""))
            # 6b opcode + 8b not used + 18b immediate
            line = _op + "{:08b}".format(0) + "{:018b}".format(imm)

        elif instruction[0] in special:
            _op = self.decode_instruction(instruction[0])
            # 6b opcode + 26b not used
            line = _op + "{:026b}".format(0)

        line += "\n"
        return line

    def write(self) -> None:

        """
        Writes the parsed instruction to the file

        """

        lines_written = 0
        with open("progfile.dat", "w", encoding='UTF-8') as output_file:
            for i in self.code:
                line = self.parse(i.split())
                output_file.write(line)
                lines_written += 1

        with open("progfile.dat", "a", encoding='UTF-8') as output_file:
            # We fill the rest of the memory with 0's. (Current memory: 64k)
            for i in range(65536 - lines_written):
                output_file.write("{:032b}\n".format(0))
