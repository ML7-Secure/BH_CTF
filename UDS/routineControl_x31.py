from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *
#from udsoncan.configs import *
#import time

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()


def RoutineControlViaServices(rid=0x1337) -> str:
    # RoutineControl
    
    #rid = 0x1337
    control = 0x03 # 0x01 : Start Routine // 0x02 : Stop Routine // 0x03 : Read Routine Result 
    
    req = RoutineControl.make_request(rid, control)
    
    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    res = response.get_payload()
    #print(res.hex())
    print(res.decode())
    
def main():
    # for rid in reversed(range(0xff00, 0xffff + 1)):
    #     print(hex(rid))
    #     RoutineControlViaServices(rid)
    #     #time.sleep(0.3)
    RoutineControlViaServices()
    
if __name__ == '__main__':
    main()