from kb import KnowledgeBase

def backward_chaining(kb: KnowledgeBase, query: str) -> bool:
    if query in kb.facts:
        return True

    for premises, conclusion in kb.rules:
        if conclusion == query:
            if all(backward_chaining(kb, premise) for premise in premises):
                return True
    return False
