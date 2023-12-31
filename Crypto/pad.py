from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from binascii import hexlify
from os import urandom

def r_pad(payload, block_size=16):
    length = block_size - (len(payload) % block_size)
    return payload + (length.to_bytes(1)) * length

_key = urandom(16)
_flag = open('flag.txt','rb').read()
_flag = r_pad(_flag)

cipher = AES.new(_key, AES.MODE_ECB)
msg = cipher.encrypt(_flag)

f = open('mykey.pem','r')
key = RSA.importKey(f.read())

pub = (key.publickey().exportKey('PEM'))

_key_enc = pow(int.from_bytes(_key),key.e,key.n)
_key_dec = pow(_key_enc,key.d,key.n).to_bytes(16)

assert(_key == _key_dec)
cipher = AES.new(_key_dec, AES.MODE_ECB)
dec_msg = cipher.decrypt(msg)
assert(_flag in dec_msg)

with open(__file__,'r') as fd:
    print(fd.read())
"I encrypted my flag with AES_ECB, and encrypted my secret key so only someone who has the private key can recovery my message. Good luck."
print("public key:")
print(pub.decode())
print("encrypted key:")
print(hexlify(_key_enc.to_bytes(16)).decode())
print("encrypted msg:")
print(hexlify(msg).decode())
