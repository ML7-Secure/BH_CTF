#!/usr/local/bin/python3
import ast, sys

"Here is a python sandbox for you! Your goal is to read the flag at ./flag.txt"
"To help you out, heres the source!"

print(sys.version)
with open(__file__,'r') as fd:
    print(fd.read())

_filter = [list, tuple, int, object, str, dict, float, bytes, None]

def chk(string):
    try:
        val = ast.literal_eval(string)
        return type(val) not in _filter
    except ValueError:
        return False
    except SyntaxError:
        return False

while True:
    inp = input("> ")
    if chk(inp.split('.')[0]):
        eval(inp,{'__builtins__':None})
    else:
        print("go away")