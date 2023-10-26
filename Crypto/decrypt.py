import subprocess
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD, isPrime
from Crypto.Cipher import AES


def factorDB(N):
    out = subprocess.run(['factordb', str(N)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return out.stdout.decode()

def eulerTotient(p,q):
    N = p*q
    return ( (p-1) * (q-1) ) #% N

def getAESkey():
    #N = input("Modulus : ")
    #print(factorDB(N))
    N = 286394205929583764004283889883101908799
    p = 1021971265088706973 
    q = 280237043557897671563
    e = 65537
    d = inverse(e, eulerTotient(p, q))
    ct = 0xd6bfd5ae31761a41982f6c7a4d2b9902
    plainAESkey = pow(ct, d, N)
    return plainAESkey
    

def main():
    AESkey = getAESkey()
    key = long_to_bytes(AESkey)
    cipher = AES.new(key, AES.MODE_ECB)
    #enc_msg = "57caf12fc0aa2f5e5151f7b06d73c2a04cd6c212e0ba5240351beac058134ff638cd4ca17a60da63067bb1be70a3d907"
    #enc_msg = bytes.fromhex(enc_msg)
    enc_msg = 0x57caf12fc0aa2f5e5151f7b06d73c2a04cd6c212e0ba5240351beac058134ff638cd4ca17a60da63067bb1be70a3d907
    enc_msg = long_to_bytes(enc_msg)
    
    flag = cipher.decrypt(enc_msg)
    print(flag.decode())

main()