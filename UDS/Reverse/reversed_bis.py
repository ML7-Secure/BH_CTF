param1 = [0]*0x270

def genState(void, param2): # void FUN_00401b5c(ulong *param_1,ulong param_2)
    seed = param2 & 0xFFFFFFFF
    param1[0] = seed
    for i in range(1,0x270): # seed already in
        seed = (seed * 0x17B5) & 0xFFFFFFFF
        param1[i] = seed
    param1.append(0x270)


def genKey(): # ulong FUN_00401c74(undefined8 *param_1,int param_2)
    if param1[-1] > 0x26f:
        if param1[-1] > 0x270:
            genState(0, 0x1105)
        
        for i in range(0xe3):
            if param1[i + 1] & 1 == 0:
                constant_value = 0x7fffffff
            else:
                constant_value = 0x3

            #param1[i] = param1[i + 0x18d] ^ param1[i + 1] & 0x7fffffff | param1[i + 1] & 0x80000000 >> 1 ^ constant_value
            #param1[i] = (param1[i + 0x18d] ^ ((param1[i + 1] & 0x7fffffff) | ((param1[i + 1] & 0x80000000) >> 1))) ^ constant_value
            param1[i] = param1[i + 0x18d] ^ (((param1[i + 1] & 0x7fffffff) | (param1[i + 1] & 0x80000000)) >> 1) ^ constant_value

        for i in range(0xe3, 0x26f):
            if param1[i + 1] & 1 == 0:
                constant_value = 0x7fffffff
            else:
                constant_value = 0x3

            #param1[i] = param1[i - 0xe3] ^ param1[i + 1] & 0x7fffffff | param1[i + 1] & 0x80000000 >> 1 ^ constant_value
            #param1[i] = (param1[i - 0xe3] ^ ((param1[i + 1] & 0x7fffffff) | ((param1[i + 1] & 0x80000000) >> 1))) ^ constant_value
            param1[i] = param1[i - 0xe3] ^ (((param1[i + 1] & 0x7fffffff) | (param1[i + 1] & 0x80000000)) >> 1) ^ constant_value

        if param1[0] & 1 == 0:
            constant_value = 0x7fffffff
        else:
            constant_value = 0x3

        #param1[0x26f] = param1[0x18c] ^ param1[0] & 0x7fffffff | param1[0x26f] & 0x80000000 >> 1 ^ constant_value
        #param1[0x26f] = (param1[0x18c] ^ ((param1[0] & 0x7fffffff) | ((param1[0x26f] & 0x80000000) >> 1))) ^ constant_value
        param1[i] = param1[0x18c] ^ (((param1[0] & 0x7fffffff) | (param1[0x26f] & 0x80000000)) >> 1) ^ constant_value

    """
    for e in param1:
        assert e < 2**32
    """

    #print(param1)

    futureKey = param1[0]
    #assert futureKey < 2**32

    futureKey = futureKey ^ futureKey >> 0xb
    #assert futureKey < 2**32
    futureKey = futureKey ^ (futureKey << 7) & 0x9d2c5680
    #assert futureKey < 2**32
    futureKey = futureKey ^ (futureKey << 0xf) & 0xefc60000
    #assert futureKey < 2**32
    #assert (futureKey ^ futureKey >> 0x12) < 2**32
    
    return futureKey ^ futureKey >> 0x12

def uds():
    param1[-1] = 0x271
    for _ in range(2**20):
        seed = genKey()
        key = genKey()
        
        #print(seed.to_bytes(4).hex())
        if (seed == 0xC91DFF42):
            print('n : ', hex(seed))
            print('n+1:', hex(key))
            print('n+2:', hex(genKey()))
            break

        #print(key.to_bytes(4).hex())
        if (key == 0xC91DFF42):
            print('n : ', hex(key))
            print('n+1:', hex(genKey()))
            print('n+2:', hex(genKey()))
            break

def main():
    uds()

if __name__ == "__main__":
    main()
