#import os
#from openai import OpenAI

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_clause(clause):
    # Simple fallback explanation (no API key needed)
    clause_lower = clause.lower()

    if "terminate" in clause_lower:
        return "This clause allows one party to end the contract. Check if the termination is fair to both sides."

    if "penalty" in clause_lower or "fine" in clause_lower:
        return "This clause mentions penalties. You may have to pay money if you break this agreement."

    if "indemnify" in clause_lower:
        return "This clause makes you responsible for losses or damages. This can be risky for small businesses."

    if "jurisdiction" in clause_lower:
        return "This clause decides which court or city will handle legal disputes. This may be inconvenient for you."

    if "auto" in clause_lower and "renew" in clause_lower:
        return "This clause renews the contract automatically. You may get locked in without noticing."

    if "intellectual property" in clause_lower or "ip" in clause_lower:
        return "This clause transfers ownership of work or ideas. Make sure you are not losing your rights."

    return "This clause contains legal terms. It is recommended to review if this condition is fair for your business."

