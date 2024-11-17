from kb import KnowledgeBase

def parse(knowledge: list[str]) -> KnowledgeBase:
    facts: list[str] = []
    rules: list[tuple | str]= []
    for s in knowledge:
        if len(s) <= 2:
            facts.append(s)
            continue
        substring = tuple(s.split("=>"))
        lol = substring[0].strip().split("&")
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
