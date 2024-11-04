import os
knowledge: list[str] = []
query : str = ''

def read_input(filename: str):
    all_lines: list[str] = []

    file = open(filename, "r")
    for line in file:
        all_lines.append(line.strip())

    if len(all_lines) != 4:
        raise ValueError("the file does not have the minimum amount of lines (4)")
    if 'TELL' not in all_lines:
        raise ValueError("the current file does not have any KB")
    if 'ASK' not in all_lines:
        raise ValueError("the current file does not have a query")

    knowledge = all_lines[all_lines.index('TELL') + 1].split(";")
    knowledge = [string.strip() for string in knowledge]
    if '' in knowledge:
        knowledge.remove('')
    for l in knowledge:
        print(l)

    return

def main():
    read_input("KB")
main()
