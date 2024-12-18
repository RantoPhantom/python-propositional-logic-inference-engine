from kb import KnowledgeBase
from itertools import product

def evaluate(clause, values) -> bool:
    premise, conclusion = clause
    if all(values[var] for var in premise):
        return values[conclusion]
    return True 

def truth_table(kb: KnowledgeBase, query: str ) -> tuple[bool, int]:
    # abusing python's set dedupe nature
    num_models: int = 0
    atoms = set(kb.facts)
    for premises, conclusion in kb.rules:
        atoms.update(premises)
        atoms.add(conclusion)

    if query not in atoms:
        return False, 0

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
            num_models += 1
            if not values[query]:
                return False, num_models
    return True, num_models

