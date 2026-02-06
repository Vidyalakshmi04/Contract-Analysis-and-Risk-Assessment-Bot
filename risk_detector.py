RISK_KEYWORDS = {
    "termination": ["terminate", "termination"],
    "penalty": ["penalty", "fine", "liquidated damages"],
    "indemnity": ["indemnify", "indemnification"],
    "non_compete": ["non compete", "not compete"],
    "jurisdiction": ["jurisdiction", "governing law"],
    "auto_renewal": ["auto renew", "renew automatically"],
    "ip": ["intellectual property", "ip rights"]
}

def detect_risks(clause):
    score = 0
    for words in RISK_KEYWORDS.values():
        for w in words:
            if w.lower() in clause.lower():
                score += 1

    level = "Low" if score == 0 else "Medium" if score == 1 else "High"
    return {"score": score, "level": level}
