from itertools import product
class KnowledgeBase:
    def __init__(self, rules: list[tuple | str], facts: list[str]):
        self.rules = rules
        self.facts = facts

def evaluate(clause, values) -> bool:
    premise, conclusion = clause
    if all(values[var] for var in premise):
        return values[conclusion]
    return True 

def truth_table(kb: KnowledgeBase, query: str ) -> bool:
    # abusing python's set dedupe nature
    atoms = set(kb.facts)
    for premises, conclusion in kb.rules:
        atoms.update(premises)
        atoms.add(conclusion)

    if query not in atoms:
        raise ValueError("query not in atoms, cannot eval")
    # make all possible combinations of 1s and 0s of the atoms
    
    atoms = list(atoms)
    all_combinations = product([True, False], repeat=len(atoms))
    for combination in all_combinations:
        # a dict of all values of those atoms
        values = dict(zip(atoms, combination))

        if not all(values[fact] for fact in kb.facts):
            # if not all facts are true then continue til it is 
            continue
        if all(evaluate(rule, values) for rule in kb.rules):
            if not values[query]:
                return False
    return True

def parse(knowledge: list[str]) -> KnowledgeBase:
    facts: list[str] = []
    rules: list[tuple | str]= []
    for s in knowledge:
        if len(s) <= 2:
            facts.append(s)
            continue
        substring = tuple(s.split("=>"))
        lol =substring[0].strip().split("&")
        rules.append((lol,substring[1].strip()))
    return KnowledgeBase(rules, facts)

def read_input(filename: str) -> tuple[KnowledgeBase, str]:
    all_lines: list[str] = []
    knowledge: list[str] = []

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
    query: str = all_lines[all_lines.index('ASK') + 1].strip()
    if '' in knowledge:
        knowledge.remove('')
    return parse(knowledge), query

def main():
    kb, query = read_input('./tests/test_10')
    print(truth_table(kb,query))
main()
