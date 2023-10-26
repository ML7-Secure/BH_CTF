def GenerateKey(inSeed, accessLevel):
    # not the same params for all !!!!!!!!!!!!!
    # DTR222, FCW222,  (NOT THIS):
    #paramA = int("00AFFE00", 16)
    #paramB = int("87654321", 16)
    #paramC = int("0000CAFE", 16)

    # LRR205 (NOT THIS) :
    # paramA = int("00AFFE01", 16)
    # paramB = int("05051969", 16)
    # paramC = int("CAFFEE00", 16)

    # RVC204, RVC213, SVS204 (NOT THIS) :
    # paramA = int("00AFFE88", 16)
    # paramB = int("87612345", 16)
    # paramC = int("0055CAFE", 16)

    inSeedAsLong = inSeed

    inSeedAsLong |= paramA
    inSeedAsLong ^= paramB
    inSeedAsLong += paramC
    inSeedAsLong ^= 0xFFFFFFFF

    outKey = inSeedAsLong & 0xFFFFFFFF
    return outKey # int


# Example usage:
if __name__ == "__main__":
    inSeed = 0x01020304  # Replace with your input seed
    accessLevel = 1  # Replace with the desired access level
    
    outKey = GenerateKey(inSeed, accessLevel)
    
    print(hex(outKey))