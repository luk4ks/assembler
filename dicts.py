"""
Dicts file for all instruction types and register translations
Instructions are separated by types, this is because later on
will be easier to handle them and translate its arguments

"""
type0_instructions = {
    "MOV" : "000000"
    ,"NOT" : "000001"
    ,"ADD" : "000010"
    ,"SUB" : "000011"
    ,"AND" : "000100"
    ,"OR" : "000101"
    ,"NEGA" : "000110"
    ,"NEGB" : "000111"
}

type1_instructions = {
    "ADDi" : "001010"
    ,"SUBi" : "001011"
    ,"ANDi" : "001100"
    ,"ORi" : "001101"
    ,"LI" : "100000"
    ,"LD" : "100001"
    ,"ST" : "100010"
}

type2_instructions = {
    "JMP" : "110000"
    ,"JZ" : "110001"
    ,"JNZ" : "110010"
    ,"CALL" : "110011"
}

special_instructions = {
    "UNMASK" : "110101"
    ,"RET" : "110100"
}

registers = {
    "R0" : "0000"
    ,"R1" : "0001"
    ,"R2" : "0010"
    ,"R3" : "0011"
    ,"R4" : "0100"
    ,"R5" : "0101"
    ,"R6" : "0110"
    ,"R7" : "0111"
    ,"R8" : "1000"
    ,"R9" : "1001"
    ,"R10" : "1010"
    ,"R11" : "1011"
    ,"R12" : "1100"
    ,"R13" : "1101"
    ,"R14" : "1110"
    ,"R15" : "1111"
}
