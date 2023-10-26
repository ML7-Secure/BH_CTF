from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *

import time

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()

def myECUReset():
    req = ECUReset.make_request(0x01)

    my_connection.send(req.get_payload())

    #payload = my_connection.wait_frame(timeout=1)
    #response = Response.from_payload(payload)

def main():
    myECUReset()

main()