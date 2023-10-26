import hashlib
import sys
import base64

# https://github.com/iCollin/ncr_aes_js

def keygen():
    if len(sys.argv) < 2:
        print('usage: python program.py <passphrase>')
        sys.exit(1)

    salt = '2d4818490b0c0a95faa5444701d99977'
    passphrase = sys.argv[1].encode('utf-8')
    #print('seed:',passphrase)
    salt_bytes = bytes.fromhex(salt)

    # Perform PBKDF2 key derivation
    dk = hashlib.pbkdf2_hmac('sha1', passphrase, salt_bytes, 65536, dklen=16)

    # Convert the derived key to base64 and print it
    print(dk)
    print(dk.hex())
    return base64.b64encode(dk).decode('utf-8')

def main():
    key = keygen()
    print(key)

if __name__ == '__main__' :
    main()