import isotp
import time

tp = isotp.socket(3) # 3=timeout
tp.set_fc_opts(stmin=5, bs=10) # https://can-isotp.readthedocs.io/en/latest/isotp/socket.html
tp.bind('can0', isotp.Address(rxid=0x694, txid=0x6b4, addressing_mode=0))

def reset():
    tp.send(bytearray([0x11, 0x01]))
    print(tp.recv().hex())

def main():
    reset()

main()
