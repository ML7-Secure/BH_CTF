from Crypto.Cipher import AES
import random

class MC256:
    _mc_256 = "⅛⅜⅝⅞⅓⅔✉☂☔☄⛄☃⚐✎❣♤♧♡♢⛈ªº¬«»░▒▓∅∈≡±≥≤⌠⌡÷≈°∙√ⁿ²¡‰­·₴≠×ΦΨικλοπτυφЯабвгдежзиклмнопрстуфхцчшщъыьэюяєѕіј„…⁊←↑→↓⇄＋ƏəɛɪҮүӨөʻˌ;ĸ⁰¹³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁱ™⧈⚔☠ᴀʙᴄᴅᴇꜰɢʜᴊᴋʟᴍɴᴏᴘꞯʀꜱᴛᴜᴠᴡʏᴢ¢¤¥©®µ¶¼½¾·‐‚†‡•‱′″‴‵‶‷‹›※‼⁂⁉⁎⁑⁒⁗℗−∓∞☀☁☈Є☲☵☽♀♂⚥♠♣♥♦♩♪♫♬♭♮♯⚀⚁⚂⚃⚄⚅ʬ⚡⛏✔❄❌❤⭐△▷▽◁◆◇○◎☆★✘⸸▲▶▼◀●◦◘⚓ᛩᛪ☺☻"

    @staticmethod
    def encode(a):
        return ''.join(MC256._mc_256[ord(c)] for c in a)

    @staticmethod
    def decode(a):
        return [MC256._mc_256.index(c) for c in a]

def gen_iv(nonce):
    c0 = 0xe66d
    c1 = 0xdeec
    c2 = 0x0005
    on_16 = 0xffff

    seed = int('0x' + ''.join(f'{b:02x}' for b in nonce), 16)
    s0 = (seed & on_16) ^ c0
    s1 = ((seed // 0x10000) & on_16) ^ c1
    s2 = ((seed // 0x100000000) & on_16) ^ c2

    def next():
        nonlocal s0, s1, s2
        carry = 0xb
        r0 = (s0 * c0) + carry
        carry = r0 >> 16
        r0 &= on_16

        r1 = (s1 * c0 + s0 * c1) + carry
        carry = r1 >> 16
        r1 &= on_16

        r2 = (s2 * c0 + s1 * c1 + s0 * c2) + carry
        r2 &= on_16
        s0, s1, s2 = r0, r1, r2
        return s2 * 0x10000 + s1

    iv = []
    i = 0
    while i < 16:
        for r in (next() for _ in range(min(16 - i, 4))):
            iv.append((r << 24) >> 24)
            i += 1

    iv = bytearray([b & 0xFF for b in iv])
    return bytes(iv) 

def encrypt(key, a, nonce=None):
    if not a.startswith('#%'):
        a = '#%' + a
    if nonce is None:
        nonce = [random.randint(0, 255) for _ in range(8)]
    iv = gen_iv(nonce)
    plain_bytes = a.encode('utf-8')
    aes = AES.new(key, AES.MODE_CFB, iv, segment_size=8)
    encr = aes.encrypt(plain_bytes)
    print('encrypteddd : ', encr.hex())

    nonce += list(encr)
    
    a = MC256.encode(bytes(nonce).decode('latin-1'))
    b = MC256.decode(a)
    
    print(b)
    return a

# Example usage:
key = b'\xe8\xb4\xf1\x16K@\xfe\xc6\xf70\x05\x8e\xbc\x13\xba\x97'
plaintext = '7D0E1A5C'
nonce = [0x7D, 0x0E, 0x1A, 0x5C]

encrypted_data = encrypt(key, plaintext, nonce)
print("Encrypted:", encrypted_data)
