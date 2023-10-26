from z3 import *

MAX_SIZE = 32
a = 1103515245
c = 12345
m = 2147483647
seed = 1337

STATE = [0x1e48add6, 0xaaa7550c, 0x18df53bf, 0xe6af1116]

def main(): 
    s = Solver()

    start0 = BitVec('start0', 32) # All calculations are mod 2**32
    start0 = (start0 * 0xcafebeef) #& 0xFFFFFFFF
    start0 += 78628735 # Value From C gen_random function (Python code produces the same now...)
    start0 = (start0 * 0xfacefeed) #& 0xFFFFFFFF    
    s.add(start0 == STATE[0] ^ 416994124) # Value From C gen_random function
    
    start1 = BitVec('start1', 32)
    start1 = (start1 * 0xcafebeef) #& 0xFFFFFFFF
    start1 += 2052411286 # Value From C gen_random function
    start1 = (start1 * 0xfacefeed) #& 0xFFFFFFFF    
    s.add(start1 == STATE[1] ^ 949405464) # Value From C gen_random function

    start2 = BitVec('start2', 32)
    start2 = (start2 * 0xcafebeef) #& 0xFFFFFFFF
    start2 += 493634929 # Value From C gen_random function
    start2 = (start2 * 0xfacefeed) #& 0xFFFFFFFF    
    s.add(start2 == STATE[2] ^ 1789407063) # Value From C gen_random function

    start3 = BitVec('start3', 32)
    start3 = (start3 * 0xcafebeef) #& 0xFFFFFFFF
    start3 += 1548933700 # Value From C gen_random function
    start3 = (start3 * 0xfacefeed) #& 0xFFFFFFFF    
    s.add(start3 == STATE[3] ^ 576706350) # Value From C gen_random function

    #exit()
    if s.check() == sat:
        model = s.model()
        print(model) # int to convert into hex and concatenate !

    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
