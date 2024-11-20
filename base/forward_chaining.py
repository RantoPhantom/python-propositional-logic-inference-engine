from kb import KnowledgeBase

def forward_chaining(kb: KnowledgeBase, query: str) -> tuple[bool, set]:
    inferred = set(kb.facts)
    new_inference = True
    if query in inferred:
        return True, inferred
    while new_inference:
        new_inference = False
        for premises, conclusion in kb.rules:
            if all(p in inferred for p in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                new_inference = True

    if query in inferred:
        return True, inferred
    return False, inferred
