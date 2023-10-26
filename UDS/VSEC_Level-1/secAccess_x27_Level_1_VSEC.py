from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()
LEVEL = 0x1 # 0x3
SEED_LENGTH = 4

def getSeed():

    # Warp up
    my_connection.send(b'\x27\x01')

    # Request Seed (LEVEL)
    req = Request(SecurityAccess, subfunction=LEVEL)

    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    #response.service_data
    print(response.data)


def getSeedViaServices() -> str:
    # Request Seed (LEVEL)
    req = SecurityAccess.make_request(LEVEL, SecurityAccess.Mode.RequestSeed)

    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    seed = response.get_payload()
    seed = seed[-SEED_LENGTH:].hex()
    return seed


def keyCalculation(seed, X=0):
    #for i in range(SEED_LENGTH):
    # b1 = int(seed[0:2],16)
    # b2 = int(seed[2:4],16)
    # b3 = int(seed[4:6],16)
    # b4 = int(seed[6:8],16)
    
    seed = int(seed, 16)

    # 1) XOR
    # key = b1 ^ b2 # NO...

    # 2) Bitwise Inverse (~) OK FOR LEVEL 3 (VSEC HarborBay)
    # b1 = hex(~b1 & 0xFF)[2:]
    # b2 = hex(~b2 & 0xFF)[2:]
    # key = int(b1+b2, 16)
    # key = key.to_bytes(2, 'big')

    # 3) Single byte XOR (^ X) OK FOR LEVEL 1 (UserSpaceDiag)
    # key_1 = hex(b1 ^ X)[2:] 
    # key_2 = hex(b2 ^ X)[2:]
    # key_3 = hex(b3 ^ X)[2:]
    # key_4 = hex(b4 ^ X)[2:]

    # key_1 = hex(b1)[2:] 
    # key_2 = hex(b2)[2:]
    # key_3 = hex(b3)[2:]
    # key_4 = hex(b4)[2:]
    # key = int(key_1 + key_2 + key_3 + key_4, 16)
    # key = key.to_bytes(4, 'big')

    # 3) RDU_222 : https://github.com/jglim/UnlockECU/blob/main/UnlockECU/UnlockECU/Security/RDU222.cs # NOT THIS....
    # paramA = int("00AFFE00", 16)
    # paramB = int("98765432", 16)
    # paramC = int("00CAFE00", 16)

    # inSeedAsLong = seed

    # inSeedAsLong |= paramA
    # inSeedAsLong ^= paramB
    # inSeedAsLong += paramC

    # key = inSeedAsLong & 0xFFFFFFFF
    
    # return key.to_bytes(4, 'big')

    # 4) DTR222 to SVS204 : https://github.com/jglim/UnlockECU/blob/main/UnlockECU/UnlockECU/Security/RVC222_MPC222_FCW246_LRR3.cs # NOT THIS....
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

    # inSeedAsLong = seed

    # inSeedAsLong |= paramA
    # inSeedAsLong ^= paramB
    # inSeedAsLong += paramC
    # inSeedAsLong ^= 0xFFFFFFFF

    # key = inSeedAsLong & 0xFFFFFFFF
    
    # return key.to_bytes(4, 'big')

    # 5) CR6NFZ : https://github.com/jglim/UnlockECU/blob/main/UnlockECU/UnlockECU/Security/PowertrainSecurityAlgo2.cs
    

    #return key.to_bytes(4, 'big')
    
    # 6) CR4_NFZ : https://github.com/jglim/UnlockECU/blob/main/UnlockECU/UnlockECU/Security/PowertrainSecurityAlgoNFZ.cs

    return key.to_bytes(4, 'big')

    # 7) CRD3 : https://github.com/jglim/UnlockECU/blob/main/UnlockECU/UnlockECU/Security/PowertrainSecurityAlgo3.cs # NOT THIS...
#     remappedValue = 0
#     for i in range(len(SourceBitPositions)):
#         remappedValue |= RemapBit(seed, SourceBitPositions[i], i)

#     key = seed ^ (seed & FinalXorKey) ^ LookupTable[remappedValue]

#     return key.to_bytes(4, 'big')

# FinalXorKey = 0x40088C88
# SourceBitPositions = [3, 7, 10, 11, 15, 19, 30]
# LookupTable = [
#     0x45D145D1, 0x406E47C6, 0x5450C446, 0x51EFC651, 0x47CE507A, 0x4271526D, 0x3121A3DA, 0x349EA1CD,
#     0x0CECABBF, 0x0953A9A8, 0x105B10DF, 0x15E412C8, 0x3E1D91A6, 0x3BA293B1, 0xA316122F, 0xA6A91038,
#     0x545044C6, 0x51EF46D1, 0x45D1C551, 0x406EC746, 0x3121235A, 0x349E214D, 0x47CED0FA, 0x4271D2ED,
#     0x105B905F, 0x15E49248, 0x0CEC2B3F, 0x09532928, 0xA31692AF, 0xA6A990B8, 0x3E1D1126, 0x3BA21331,
#     0xC4CE5450, 0xA54D2082, 0xD54FD5C7, 0xD3A2D322, 0xC6D141FB, 0xA7523529, 0xB03EB25B, 0xB6D3B4BE,
#     0xD921E349, 0x884CB829, 0x442A60C0, 0x94FB0349, 0xEBD0D950, 0xBABD8230, 0xF7676230, 0x27B601B9,
#     0xD54F5547, 0xD3A253A2, 0xC4CED4D0, 0xA54DA002, 0xB03E32DB, 0xB6D3343E, 0xC6D1C17B, 0xA752B5A9,
#     0x442AE040, 0x94FB83C9, 0xD92163C9, 0x884C38A9, 0xF767E2B0, 0x27B68139, 0xEBD059D0, 0xBABD02B0,
#     0xE3BF18F8, 0xDDA62A01, 0x9550EB58, 0xAB49D9A1, 0xE1A00D53, 0xDFB93FAA, 0xF0218CC4, 0xCE38BE3D,
#     0xA1CAE9CA, 0x9FD3DB33, 0x3CC16A43, 0x02D858BA, 0x933BD3D3, 0xAD22E12A, 0x8F8C68B3, 0xB1955A4A,
#     0x95506BD8, 0xAB495921, 0xE3BF9878, 0xDDA6AA81, 0xF0210C44, 0xCE383EBD, 0xE1A08DD3, 0xDFB9BF2A,
#     0x3CC1EAC3, 0x02D8D83A, 0xA1CA694A, 0x9FD35BB3, 0x8F8CE833, 0xB195DACA, 0x933B5353, 0xAD2261AA,
#     0x5A4815E4, 0x5CB8A6A1, 0x4BC99473, 0x4D392736, 0x5857004F, 0x5EA7B30A, 0x2EB8F3EF, 0x284840AA,
#     0x103A4AD8, 0x16CAF99D, 0x0C8DF1B8, 0x0A7D42FD, 0x22CB70C1, 0x243BC384, 0xBFC0F348, 0xB930400D,
#     0x4BC914F3, 0x4D39A7B6, 0x5A489564, 0x5CB82621, 0x2EB8736F, 0x2848C02A, 0x585780CF, 0x5EA7338A,
#     0x0C8D7138, 0x0A7DC27D, 0x103ACA58, 0x16CA791D, 0xBFC073C8, 0xB930C08D, 0x22CBF041, 0x243B4304,
# ]

# def RemapBit(inValue: int, sourceBitPosition: int, destinationBitPosition: int) -> int:
#     return 1 << destinationBitPosition if (inValue & (1 << sourceBitPosition)) else 0


def SendKeyViaServices(seed):

    if SEED_LENGTH == 4:
        #for X in range(256):
        key = keyCalculation(seed) #####
        time.sleep(0.5) # !! IMPORTANT !! #
        
        #Send Key (LEVEL)
        req = SecurityAccess.make_request(LEVEL, SecurityAccess.Mode.SendKey, data=key)

        my_connection.send(req.get_payload())
        payload = my_connection.wait_frame(timeout=1)
        response = Response.from_payload(payload)
        rep = response.get_payload()
        print(rep.hex())
        #print(rep.decode())
            
    elif SEED_LENGTH == 2:
        key = keyCalculation(seed) #####
        #Send Key (LEVEL)
        req = SecurityAccess.make_request(LEVEL, SecurityAccess.Mode.SendKey, data=key)

        my_connection.send(req.get_payload())
        payload = my_connection.wait_frame(timeout=1)
        response = Response.from_payload(payload)
        rep = response.get_payload()
        print(rep.hex())
        a ={
        #'response.service' : response.service,
        #'response.data' : response.data,
        'response.code' : response.code,
        }
        print(a)

    else:
        exit('SEED LENGTH NOT COVERED')


    
def main():
    seed = getSeedViaServices()
    SendKeyViaServices(seed)

if __name__ == '__main__':
    main()

""" Seed Evolution
E4 EC 3C 08
30 B4 0E 07 
2F 36 1B 3A 
BA 80 83 9A 
96 D6 C9 BF 
F6 AF 1E 8D 
9B CD 75 EA 
61 4E 5D 4E 
BD 65 AA 48 
69 60 93 90 
A8 EA 99 5D 
6D F8 2A EF 
41 56 2C FA 
3C 7B 1F 3C 
67 C8 6E 03 
2A 3E BD 7F  
B1 2C 4F DD 
DB FE DC C7 
8F FC 08 08 
28 84 1D 91 
AF AE 0B E2 
C7 00 25 17 
A8 AD B2 03 
92 21 46 50 
8E 48 D3 C8 
E9 28 A4 AA 
8D DF 34 76 
3C 5A 59 E1 
50 A6 CD BC 
2B 7D F2 6F 
E3 2D BC 4C 
B6 4C 49 2A 
D5 2F B4 21 
52 39 D5 72 
4E 5D 95 92 
57 70 2C D1 
8C F3 4D 33 
08 4E D8 E0 
90 CC 45 E0 
6C C5 B7 AB 
22 7A 10 7A 
29 FE 00 FD 
AC E8 D8 9E 
D5 C3 2B 60 
12 4D BA AF 
8D F2 D7 F4 
55 46 7F EE 
EE 1E F6 09 
"""



