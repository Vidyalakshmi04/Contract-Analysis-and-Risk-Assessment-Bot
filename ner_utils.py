import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "Parties (ORG / PERSON)": [],
        "Dates": [],
        "Amounts (MONEY)": [],
        "Locations / Jurisdiction (GPE)": []
    }

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON"]:
            entities["Parties (ORG / PERSON)"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["Dates"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["Amounts (MONEY)"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["Locations / Jurisdiction (GPE)"].append(ent.text)

    # Remove duplicates
    for k in entities:
        entities[k] = list(set(entities[k]))

    return entities
