def GetBit(value: int, bitPosition: int) -> int:
    return (value >> bitPosition) & 1

def GetByte(value: int, bytePosition: int) -> int:
    return (value >> (bytePosition * 8)) & 0xFF

def SetBit(value: int, bitPosition: int) -> int:
    return value | (1 << bitPosition)

def SetByte(value: int, byteValue: int, bytePosition: int) -> int:
    return (value & ~(0xFF << (bytePosition * 8))) | (byteValue << (bytePosition * 8))

def GenerateKey(inSeed, accessLevel): # INCORRECTTTTT

    matrix = [[0x34, 0xC6, 0x10, 0xA3],
    [0xA3, 0x99, 0xD1, 0x01],
    [0x38, 0x09, 0xF3, 0x84],
    [0x37, 0xCF, 0xA8, 0x49],
    [0x30, 0xC7, 0xE1, 0xB7],
    [0xBE, 0x27, 0xB4, 0xF9],
    [0xDD, 0x45, 0xE6, 0xA1],
    [0x72, 0x85, 0xBA, 0xA2],
    ]
    i = [1,2,1,0,1,0]
    j = [5,2,7,2,7,5]


    #workingSeed = bytearray([inSeed[3], inSeed[2], inSeed[1], inSeed[0]])
    workingSeed = inSeed.to_bytes(4, 'little')

    y = workingSeed[i[0]] ^ workingSeed[i[1]]
    dBit2 = GetBit(workingSeed[i[2]], j[0])
    dBit1 = GetBit(workingSeed[i[3]], j[1])
    dBit0 = GetBit(y, j[2])
    dValue = CreateDValue(dBit2, dBit1, dBit0, matrix)

    #seedAsInt = BytesToInt(workingSeed, Endian.Little)
    seedAsInt = int(workingSeed.hex(), 16)

    dXorIntermediate = seedAsInt ^ dValue
    gBit2 = GetBit(workingSeed[i[4]], j[3])
    gBit1 = GetBit(y, j[4])
    gBit0 = GetBit(GetByte(dXorIntermediate, i[5]), j[5])
    gValue = CreateGValue(gBit2, gBit1, gBit0, matrix)

    seedKey = dXorIntermediate ^ gValue

    #IntToBytes(seedKey, outKey, Endian.Big)
    return seedKey.to_bytes(4, 'big')
    
    
def CreateDValue(bit2Enabled: int, bit1Enabled: int, bit0Enabled: int, matrix) -> int:
    i = 0
    j = 0
    if bit0Enabled != 0:
        j = SetBit(j, 0)
    if bit1Enabled != 0:
        j = SetBit(j, 1)
    if bit2Enabled != 0:
        j = SetBit(j, 2)
    i = SetByte(i, matrix[j][3], 0)
    i = SetByte(i, matrix[j][2], 1)
    i = SetByte(i, matrix[j][1], 2)
    i = SetByte(i, matrix[j][0], 3)
    return i

def CreateGValue(bit2Enabled: int, bit1Enabled: int, bit0Enabled: int, matrix) -> int:
    i = 0
    j = 0
    if bit0Enabled != 0:
        j = SetBit(j, 0)
    if bit1Enabled != 0:
        j = SetBit(j, 1)
    if bit2Enabled != 0:
        j = SetBit(j, 2)
    i = SetByte(i, matrix[j][0], 0)
    i = SetByte(i, matrix[j][3], 1)
    i = SetByte(i, matrix[j][2], 2)
    i = SetByte(i, matrix[j][1], 3)
    return i


# Example usage:
if __name__ == "__main__":
    inSeed = 0x01020304
    accessLevel = 1  # Replace with the desired access level
    key = GenerateKey(inSeed, accessLevel)
    print(key.hex())
    