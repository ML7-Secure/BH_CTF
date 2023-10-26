def FUN_00401b5c(param_1, param_2):
    # Store the lower 32 bits of param_2 in the first element of the list.
    param_1[0] = param_2 & 0xFFFFFFFF

    # Store the value 1 at the index 0x270 in the list.
    param_1.append(1)

    # Loop while the value at index 0x270 is less than 0x270 (624).
    while param_1[0x270] < 0x270:
        # Calculate the new value and store it at the appropriate index in the list.
        index = param_1[0x270]
        previous_value = param_1[index - 1]
        new_value = previous_value * 0x17B5
        param_1.append(new_value)

        # Increment the value at index 0x270 by 1.
        param_1[0x270] += 1

def easy(param1,param2):
    seed = param2 & 0xFFFFFFFF
    param1.append(seed)
    for i in range(0x270 - 1): # seed already appened
        seed = (seed * 0x17B5) & 0xFFFFFFFF
        param1.append(seed)
    param1.append(0x270)
    return param1

param1 = []
param2 = 0x1105
easy(param1, param2)
print(param1)
print(len(param1))
#exit()

def xor_operation(param_1, i, mask):
    return param_1[i] ^ ((param_1[i + 1] & 0x7fffffff | param_1[i] & 0x80000000) >> 1) ^ mask

def apply_xor_operations(param_1):
    # Assuming param_1 is a list or array of integers

    # Loop 1 (i < 0xe3)
    for i in range(0xe3):
        mask = 0x7FFFFFFF if param_1[i + 1] & 1 == 0 else 0x3
        param_1[i] = param_1[i + 0x18d] ^ xor_operation(param_1, i, mask)

    # Loop 2 (i >= 0xe3 and i < 0x26f)
    for i in range(0xe3, 0x26f):
        mask = 0x7FFFFFFF if param_1[i + 1] & 1 == 0 else 0x3
        param_1[i] = param_1[i - 0xe3] ^ xor_operation(param_1, i, mask)

    mask = 0x7FFFFFFF if param_1[0] & 1 == 0 else 0x3
    param_1[0x26f] = param_1[0x18c] ^ ((param_1[0] & 0x7fffffff | param_1[0x26f] & 0x80000000) >> 1) ^ mask
"""
apply_xor_operations(param1)
print(param1)
print(param1[0])

test0 = ((param1[0x18d] ^ param1[1] & 0x7FFFFFFF | param1[0] & 0x80000000) >> 1) ^ 0x7FFFFFFF
test1 = ((param1[0x18d] ^ param1[1] & 0x7FFFFFFF | param1[0] & 0x80000000) >> 1) ^ 0x3

print(test0)
print(test1)
"""

"""

preKey = param1[0]

preKey = preKey ^ preKey >> 0xb
preKey = preKey ^ (preKey << 7) & 0x9d2c5680
preKey = preKey ^ (preKey << 0xf) & 0xefc60000
uVar4 = preKey ^ preKey >> 0x12

generatedKeyKey=[0,0,0,0]

generatedKeyKey[1] = uVar4 >> 0x10
generatedKeyKey[0] = uVar4 >> 0x18
generatedKeyKey[2] = uVar4 >> 8
generatedKeyKey[3] = uVar4


generatedKeyKey[1] = int(hex(uVar4)[2:][-2:],16) >> 0x10
generatedKeyKey[0] = int(hex(uVar4)[2:][-2:],16) >> 0x18
generatedKeyKey[2] = int(hex(uVar4)[2:][-2:],16) >> 8
generatedKeyKey[3] = int(hex(uVar4)[2:][-2:],16)

print(generatedKeyKey)
for e in generatedKeyKey:
    print(hex(e))


"""