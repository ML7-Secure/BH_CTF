from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *

# my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
# my_connection.open()
# assert my_connection.is_open()
# LEVEL = 0x1 # 0x3

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
    seed = seed[-2:].hex()
    return seed 

    # USELESS ?
    #interpretedResponse = SecurityAccess.interpret_response(response,SecurityAccess.Mode.RequestSeed)
    #print(interpretedResponse)

    # USELESS ?
    #res = SecurityAccess.ResponseData(0x03, int("D77D", 16).to_bytes(2,'big'))
    #print(res.seed)

    #print(response.service_data)
    #print("\n")
    #print(response.data)

def keyCalculation(seed):
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    seed = int(seed, 16)

    # 1) XOR
    # key = b1 ^ b2 # NOT THIS

    # 2) Bitwise Inverse (~) OK FOR LEVEL 3
    b1 = hex(~b1 & 0xFF)[2:]
    b2 = hex(~b2 & 0xFF)[2:]
    key = int(b1+b2, 16)
    key = key.to_bytes(2, 'big')

    return key

def keyCalculation_4byteSeed(seed): # NOK FOR LEVEL 1
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    b3 = int(seed[4:6],16)
    b4 = int(seed[6:8],16)
    seed = int(seed, 16)

    # 2) Bitwise Inverse (~) OK FOR LEVEL 3
    b1 = hex(~b1 & 0xFF)[2:]
    b2 = hex(~b2 & 0xFF)[2:]
    b3 = hex(~b3 & 0xFF)[2:]
    b4 = hex(~b4 & 0xFF)[2:]
    key = int(b1+b2+b3+b4, 16)
    key = key.to_bytes(4, 'big')

    print(key.hex())


def SendKeyViaServices(seed):
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
    
def main():
    seed = getSeedViaServices()
    SendKeyViaServices(seed)


if __name__ == '__main__':
    main()
    #seed = "7D0E1A5C"
    #keyCalculation_4byteSeed(seed)