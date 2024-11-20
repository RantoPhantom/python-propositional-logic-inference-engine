class KnowledgeBase:
    def __init__(self, rules: list[tuple | str], facts: list[str]):
        self.facts = facts
        self.rules = rules

