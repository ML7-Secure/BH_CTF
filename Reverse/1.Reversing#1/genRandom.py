
a = 1103515245
c = 12345
m = 2147483647
seed = 1337

def gen_random():
    global seed
    tmp = (a * seed + c) & 0xFFFFFFFF # OVERFLOW to handle to get the same behavior than C ! Or use ctypes (see below...)
    seed = tmp % m
    print("seed :", seed)
    return seed

if __name__ == "__main__":
    for i in range(8):
        gen_random()

""" ALTERNATIVE WITH 'ctypes'
import ctypes

a = 1103515245
c = 12345
m = 2147483647
seed = 1337

STATE = [0x1e48add6, 0xaaa7550c, 0x18df53bf, 0xe6af1116]

# Load the C library
lib = ctypes.CDLL('./lcg.so') # $ gcc -shared -fPIC -o lcg.so genRandom.c

# Define the C function signature
lib.gen_random.restype = ctypes.c_uint32

def gen_random():
    global seed
    seed = lib.gen_random()
    #print("seed :", seed)
    return seed

if __name__ == "__main__":
    for i in range(8):
        gen_random()
"""