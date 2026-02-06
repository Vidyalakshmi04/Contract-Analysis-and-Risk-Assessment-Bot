def detect_contract_type(text):
    text = text.lower()
    if "employment" in text:
        return "Employment Contract"
    elif "lease" in text or "rent" in text:
        return "Lease Agreement"
    elif "service" in text:
        return "Service Contract"
    elif "vendor" in text or "supplier" in text:
        return "Vendor Agreement"
    elif "partnership" in text:
        return "Partnership Deed"
    else:
        return "General Agreement"


def classify_clause_type(clause):
    c = clause.lower()
    if "shall not" in c or "must not" in c:
        return "🚫 Prohibition"
    elif "shall" in c or "must" in c:
        return "📌 Obligation"
    elif "may" in c:
        return "✅ Right"
    else:
        return "Neutral"


AMBIGUOUS_WORDS = ["reasonable", "best effort", "as soon as possible", "from time to time", "appropriate"]

def is_ambiguous(clause):
    return any(word in clause.lower() for word in AMBIGUOUS_WORDS)
