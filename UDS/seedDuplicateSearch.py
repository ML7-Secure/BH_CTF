from udsoncan import *
from udsoncan.services import * # SecurityAccess, ECUReset...
from udsoncan.connections import *

import time

my_connection = IsoTPSocketConnection('vcan0', 0x7e8, 0x7e0)
my_connection.open()
assert my_connection.is_open()


LEVEL = 0x5
SEED_LENGTH = 4
NUMBER_OF_REQUESTS = 630
SEEDS = []

def createSeeds() -> str:
    # Request Seed (LEVEL)
    req = SecurityAccess.make_request(LEVEL, SecurityAccess.Mode.RequestSeed)

    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    seed = response.get_payload()
    seed = seed[-SEED_LENGTH:].hex()

    SEEDS.append(seed)


def getSeedViaServices() -> str:
    # Request Seed (LEVEL)
    req = SecurityAccess.make_request(LEVEL, SecurityAccess.Mode.RequestSeed)

    my_connection.send(req.get_payload())

    payload = my_connection.wait_frame(timeout=1)

    response = Response.from_payload(payload)
    seed = response.get_payload()
    seed = seed[-SEED_LENGTH:].hex()

    return seed


def myECUReset():
    req = ECUReset.make_request(0x01)
    my_connection.send(req.get_payload())

def main():
    print("RESET")
    myECUReset()
    time.sleep(1)
    
    for i in range(NUMBER_OF_REQUESTS):
        createSeeds()
        """
        myECUReset()
        time.sleep(1)
        """
    print(len(SEEDS))
    
    print("RESET")
    myECUReset()
    time.sleep(2)

    yes = 0
    for i in range(NUMBER_OF_REQUESTS):
        test = getSeedViaServices()
        if yes == 1 : print(test)
        yes = 0
        if test in SEEDS:
            print(test)
            print(">>>>>>>>>>>>>>>>>>>>>>> in <<<<<<<<<<<<<<<<<<<<<<<")
            yes = 1
        else:
            print("not in")

if __name__ == '__main__':
    main()