from forward_chaining import forward_chaining
from backward_chaining import backward_chaining
from truth_table import truth_table
from kb import KnowledgeBase
import os

dir = os.fsencode("./tests")
kbs = []
queries = []
values = []
filenames = []

def parse(knowledge: list[str]) -> KnowledgeBase:
    facts: list[str] = []
    rules: list[tuple | str]= []
    for s in knowledge:
        if len(s) <= 2:
            facts.append(s)
            continue
        substring = tuple(s.split("=>"))
        lol = substring[0].strip().split("&")
        lol = [s.strip() for s in lol]
        rules.append((lol,substring[1].strip()))
    return KnowledgeBase(rules, facts)

def read_input_tests(filename: str) -> tuple[KnowledgeBase, str, str, bool]:
    all_lines: list[str] = []
    knowledge: list[str] = []

    file = open(filename, "r")
    for line in file:
        all_lines.append(line.strip())

    if len(all_lines) != 5:
        raise ValueError(f"the file does not have the minimum amount of lines (5) {filename}")
    if 'TELL' not in all_lines:
        raise ValueError("the current file does not have any KB")
    if 'ASK' not in all_lines:
        raise ValueError("the current file does not have a query")

    knowledge = all_lines[all_lines.index('TELL') + 1].split(";")
    knowledge = [string.strip() for string in knowledge]
    query: str = all_lines[all_lines.index('ASK') + 1].strip()
    if '' in knowledge:
        knowledge.remove('')
    return parse(knowledge), query, filename, all_lines[4].lower() == 'true'

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    if filename.endswith(".py") or filename.endswith(".readme"):
        continue

    input = read_input_tests("./tests/" + filename)
    kbs.append(input[0])
    queries.append(input[1])
    values.append(input[3])
    filenames.append(input[2])

methods = [forward_chaining,backward_chaining,truth_table]

for method in methods:
    for i in range(len(kbs)):
        assert method(kbs[i],queries[i]) == values[i], f'''
        shit gon wrong: the {method.__name__} for {filenames[i]}
        was asserted: {values[i]}, but got: {method(kbs[i],queries[i])}
        '''
print(f"all {len(kbs)} tests are tested and nothing errored :D")
