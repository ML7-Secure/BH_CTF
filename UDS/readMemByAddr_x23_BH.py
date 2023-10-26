import can
import isotp

tp = isotp.socket(3) # 3=timeout
tp.set_fc_opts(stmin=5, bs=10) # https://can-isotp.readthedocs.io/en/latest/isotp/socket.html
tp.bind('vcan0', isotp.Address(rxid=0x7e8, txid=0x7e0, addressing_mode=0))

def ReadMemByAddr():
    a = 0x00400000
    out_f = open('dumpMem', 'wb')
    while True:
        print("reading", hex(a))
        #tp.send(bytearray([0x23, 0x44, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00])) # == echo "23 44 00 40 00 00 00 00 08 00"
        tp.send(bytearray([0x23, 0x44, (a>>24) & 0xFF, (a>>16) & 0xFF, (a>>8) & 0xFF, a & 0xFF, 0x00, 0x00, 0x08, 0x00])) # == echo "23 44 00 40 00 00 00 00 08 00"
        #                  ^^^   ^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^
        #               service sizes                MEMORY ADDRESS                             SIZE TO READ
        resp = tp.recv()
        out_f.write(resp)
        a+=0x0800

    out_f.close()

def main():
    ReadMemByAddr()

main()
