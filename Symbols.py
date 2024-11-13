class Sentence():
    def eval(self, model):
        raise NotImplementedError

    def symbols(self):
        return set()

class Symbol(Sentence):
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return self.name

class Not:
    def __init__(self, operand):
        self.operand = operand

class And:
    def __init__(self, *conjuncts):
        self.operands = conjuncts
