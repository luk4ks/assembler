"""Imports to treat all instructions"""
from dicts import type0_instructions as type0
from dicts import type1_instructions as type1
from dicts import type2_instructions as type2
from dicts import special_instructions as special
from dicts import registers as reg


class Assembler:
    """Assembler class. Main purpose is to translate instructions to machine code
       It takes an input file and creates (or modifies if exists) 
       the file progfile.dat with the machine code
    """

    def __init__(self, file: str) -> None:
        """Save file and create instructions list"""

        self.filename = file
        self.code = []

    def decode_register(self, register: str) -> str:
        """Returns the register binary translation"""

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

        print(self.code)

    def parse_out(self) -> None:
        """
        Parses all instructions based on their types and then
        writes on the output file translated to binary

        """

        with open("progfile.dat", "w", encoding='UTF-8') as output_file:
            for i in self.code:
                line = ""
                inst = i.split()
                # We save the instruction to treat
                _op = inst[0]

                if _op in type0:
                    _rd = inst[1]
                    _r1 = inst[2]
                    _r2 = inst[3]
                    #6 bits opcode + 4 bits target register + 4 bits op1 + 4 bits op2 + 14 bits not used
                    line = self.decode_instruction(_op) + self.decode_register(_rd) + self.decode_register(_r1) + self.decode_register(_r2) + "{:014b}".format(0)

                elif _op in type1:
                    reg = inst[1]
                    inm = int(inst[2].replace("#",""))
                    #6 bits opcode + 4 bits target regisrter + 4 bits not used?? + 18 bits immediate??
                    line = self.decode_instruction(_op) + self.decode_register(reg) + "{:04b}".format(0) + "{:018b}".format(inm)

                elif _op in type2:
                    _rd = inst[1]
                    _r1 = inst[2]
                    inm = inst[3].replace("#","")
                    line = self.decode_instruction(_op) + self.decode_register(_rd) + self.decode_register(_r1) + "{:018b}".format(inm)

                elif _op in special:
                    line = self.decode_instruction(_op) + "{:026b}".format(0)

                line += "\n"
                output_file.write(line)
