from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *
#from udsoncan.configs import *
#import time

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()


def ReadMemByAddrViaServices(addr=0xC0FFE000, memSize=0xFF, address_format=32, memorysize_format=32) -> str:
    #memSize = 0xFF
    memLoc = MemoryLocation(addr, memSize, address_format=address_format, memorysize_format=memorysize_format)
    req = ReadMemoryByAddress.make_request(memLoc)
    
    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)
    
    response = Response.from_payload(payload)
    res = response.get_payload() # error : "Cannot make payload from response object. Service is not set" ???
    #print(res.hex())
    """
    if "7f" in res.hex():
        return
    else:
        print(res.hex())
        try:
            print(res.decode())
        except UnicodeDecodeError as e:
            print(e)
    """

def main():
    #for address in range(0xC0FFE000, 0xC3F80000, 0xFF):
        #echo "23 44 C0 FF E0 00 00 00 0A FF" | isotpsend -p 00 -s 7e0 -d 7e8 vcan0 # Solution for ReadMemByAddr Challenge
        #ReadMemByAddrViaServices(address)

    address = 0xC0FFE000
    #address = 0x00400000
    memSize = 0xAFF
    ReadMemByAddrViaServices(address, memSize)
    
if __name__ == '__main__':
    main()