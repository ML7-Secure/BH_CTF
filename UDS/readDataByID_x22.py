from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *
from udsoncan.configs import *
import time

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()


def ReadDatabyIdViaServices(i) -> str:
    # ReadDatabyIdViaServices (w/ didlist)

    didlist = [i]
    #didlist = [i for i in reversed(range(0xFFFF + 1))]
    
    didconfig = dict(default_client_config)
    didconfig['data_identifiers'] = {i : AsciiCodec(15)}
    
    try:
        req = ReadDataByIdentifier.make_request(didlist, didconfig)
    except ValueError as e:
        print(e)

    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    res = response.get_payload()
    #print(res.hex())
    print(res.decode())
    
def main():
    for i in range(0xFFFF + 1):
        time.sleep(0.2)
        print(hex(i)[2:].zfill(4))
        ReadDatabyIdViaServices(i)
    
if __name__ == '__main__':
    main()