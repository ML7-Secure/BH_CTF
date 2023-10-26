def GenerateKey(inSeed, accessLevel):
    paramA = int("00AFFE00", 16)
    paramB = int("98765432", 16)
    paramC = int("00CAFE00", 16)

    inSeedAsLong = inSeed

    inSeedAsLong |= paramA
    inSeedAsLong ^= paramB
    inSeedAsLong += paramC

    outKey = inSeedAsLong & 0xFFFFFFFF
    return outKey # int


# Example usage:
if __name__ == "__main__":
    inSeed = 0x01020304  # Replace with your input seed
    accessLevel = 1  # Replace with the desired access level
    
    outKey = GenerateKey(inSeed, accessLevel)
    
    print(hex(outKey))