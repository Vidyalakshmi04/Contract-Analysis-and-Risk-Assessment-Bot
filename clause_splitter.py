import re

def split_clauses(text):
    clauses = re.split(r"\n\d+\.|\nClause \d+|\n", text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]
