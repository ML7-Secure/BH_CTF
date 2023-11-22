from udsoncan import *
from udsoncan.services import * # SecurityAccess...
from udsoncan.connections import *
#from udsoncan.configs
import time
a=input("rx : ")
b=input("tx : ")
rx = int(a, 16)
tx = int(b, 16)
my_connection = IsoTPSocketConnection('can0', rx, tx)
my_connection.open()
assert my_connection.is_open()

req = ClearDiagnosticInformation.make_request(group=0xFFFFFF)
my_connection.send(req.get_payload())
payload = my_connection.wait_frame(timeout=3)
response = Response.from_payload(payload)
res = response.get_payload()
print(res.hex())
