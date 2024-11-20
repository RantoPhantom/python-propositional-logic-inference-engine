import sys
from forward_chaining import forward_chaining
from backward_chaining import backward_chaining
from truth_table import truth_table
from file_reader import read_input

methods = {
        'tt': truth_table,
        'fc': forward_chaining,
        'bc': backward_chaining
        }

def main():
    if len(sys.argv) != 3:
        raise ValueError(f"Incorrect number of args, need 2 [file_path/name] [method]")
    method_input: str = sys.argv[2].lower()
    file_path: str = sys.argv[1]
    if method_input not in methods:
        print(f"The method provided is unknown/not implemented: {sys.argv[2]}")
        exit(1)
    kb, query = read_input(file_path)
    out = methods[method_input](kb,query)
    msg = "YES" if out[0] == True else "NO"
    msg += ": "
    msg += "" if out[1] == set() or out[1] == 0 else str(out[1])
    print(msg)
main()
