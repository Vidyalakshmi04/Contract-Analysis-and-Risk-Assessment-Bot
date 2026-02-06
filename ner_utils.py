import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = spacy.blank("en")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "PERSON": [],
        "ORG": [],
        "GPE": [],
        "DATE": [],
        "MONEY": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities
