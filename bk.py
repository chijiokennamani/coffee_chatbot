#!/usr/bin/env python3
# entity_lab.py

"""
Entity Extraction Lab using spaCy with auto-download of the model.
Extracts PERSON, GPE (locations), DATE, TIME, etc. directly in code.
"""

import spacy
import spacy.cli

MODEL = "en_core_web_sm"

# Attempt to load; if missing, download then load
try:
    nlp = spacy.load(MODEL)
except OSError:
    print(f"Model '{MODEL}' not found. Downloading...")
    spacy.cli.download(MODEL)
    nlp = spacy.load(MODEL)

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def main():
    print("spaCy NER Lab – type a sentence (or 'exit' to quit):")
    while True:
        txt = input("You> ").strip()
        if txt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        entities = extract_entities(txt)
        if not entities:
            print("No entities found.")
        else:
            for ent_text, ent_label in entities:
                print(f" • {ent_text:<15} → {ent_label}")

main()
