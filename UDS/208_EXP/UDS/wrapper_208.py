from udsoncan import *
from udsoncan.services import * # SecurityAccess...
from udsoncan.connections import *
#from udsoncan.configs
import time
import subprocess

SESSION_NUM = 3

client_server = [(0x49b, 0x49a), (0x58b, 0x58a), (0x590, 0x58f), (0x5d0, 0x5cf), (0x6a2, 0x682), (0x6a6, 0x686), (0x6a8, 0x688), (0x6a9, 0x689), (0x6ad, 0x68d), (0x6b4, 0x694), (0x6ba, 0x69a), (0x74a, 0x64a), (0x7ff, 0x64a), (0x7ff, 0x694)]

"""
(0x49b, 0x49a), 
(0x58b, 0x58a), 
(0x590, 0x58f), 
(0x5d0, 0x5cf), 

(0x6a2, 0x682), 

(0x6a6, 0x686), 
(0x6a8, 0x688),

(0x6a9, 0x689), 

(0x6ad, 0x68d), 
(0x6b4, 0x694), 
(0x6ba, 0x69a), 
(0x74a, 0x64a), 
(0x7ff, 0x64a), 
(0x7ff, 0x694)]
"""

def session(my_connection):
    req = DiagnosticSessionControl.make_request(SESSION_NUM)
    my_connection.send(req.get_payload())
    payload = my_connection.wait_frame(timeout=3)
    response = Response.from_payload(payload)
    res = response.get_payload()
    print(res.hex())

def session_cc(i):
    out = subprocess.run(['./cc.py', '-i', 'can0', 'uds', 'security_seed', '3', '3', '-n', '1', str(client_server[i][0]), str(client_server[i][1])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = out.stdout
    print(res.decode())

#def reset(i):
def reset():
    #out = subprocess.run(['./cc.py', '-i', 'can0', 'uds', 'ecu_reset', '1', str(client_server[i][0]), str(client_server[i][1])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = subprocess.run(['./cc.py', 'uds', 'ecu_reset', '1', '0x6f0', '0x611'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = out.stdout
    print(res.decode())

def dtc_clear(my_connection):
    req = ClearDiagnosticInformation.make_request(group=0xFFFFFF)
    my_connection.send(req.get_payload())
    payload = my_connection.wait_frame(timeout=3)
    print("debug")
    response = Response.from_payload(payload)
    res = response.get_payload()
    print(res.hex())
    print("debug")


def main():
    #for i in range(len(client_server)):
    #i = 10 # 4, 7, 11, 12, 13 - not completed correctly //// 10 : all good
    #my_connection = IsoTPSocketConnection('can0', client_server[i][1], client_server[i][0])
    #my_connection = IsoTPSocketConnection('can0', 0x611, 0x6f0)
    #my_connection.open()
    #assert my_connection.is_open()

    #session(my_connection)
    #session_cc(i)
    #print("********************************* SESSION OPENED *********************************")
    for _ in range(1):
	    reset()
    print("********************************* RESET SENT *********************************")
    #dtc_clear(my_connection)
    #print("********************************* DTC CLEAR SENT *********************************")

main()

