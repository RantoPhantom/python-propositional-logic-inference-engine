from kb import KnowledgeBase

def backward_chaining(kb: KnowledgeBase, query: str, inferred: set = set()) -> tuple[bool, set]:
    if query in kb.facts:
        inferred.add(query)
        return True, inferred

    for premises, conclusion in kb.rules:
        if conclusion == query:
            inferred.add(conclusion)
            return all(backward_chaining(kb, premise, inferred) for premise in premises),inferred
    return False, inferred
