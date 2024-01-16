import spacy
from spacy import displacy
from spacy.tokens import DocBin
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

def ner_spacy(text, model_name):
    nlp = spacy.load(model_name)
    doc = nlp(text)
    return doc

def ner_biobert(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)
    
    # Convert predictions to tokens
    tokens = tokenizer.convert_ids_to_tokens(predictions[0].tolist())
    
    return tokens

def compare_ner_results(text, spacy_model_name, biobert_model_name):
    # Load spaCy model
    spacy_doc = ner_spacy(text, spacy_model_name)

    # Load BioBERT model
    tokenizer_biobert = AutoTokenizer.from_pretrained(biobert_model_name)
    model_biobert = AutoModelForTokenClassification.from_pretrained(biobert_model_name)

    # Perform NER with BioBERT
    tokens_biobert = ner_biobert(text, tokenizer_biobert, model_biobert)

    # Extract entities from spaCy
    entities_spacy = [ent.text for ent in spacy_doc.ents]

    # Extract entities from BioBERT
    entities_biobert = [token for token in tokens_biobert if token.startswith("B-")]

    # Compare entities
    common_entities = set(entities_spacy) & set(entities_biobert)
    unique_entities_spacy = set(entities_spacy) - set(entities_biobert)
    unique_entities_biobert = set(entities_biobert) - set(entities_spacy)

    # Display results
    print(f"Total entities detected by spaCy: {len(entities_spacy)}")
    print(f"Total entities detected by BioBERT: {len(entities_biobert)}")
    print(f"Common entities: {len(common_entities)}")
    print(f"Entities unique to spaCy: {len(unique_entities_spacy)}")
    print(f"Entities unique to BioBERT: {len(unique_entities_biobert)}")

    # Display most common words for spaCy
    print("\nMost common words for spaCy:")
    counter_spacy = Counter(entities_spacy)
    for word, count in counter_spacy.most_common(10):
        print(f"{word}: {count}")

    # Display most common words for BioBERT
    print("\nMost common words for BioBERT:")
    counter_biobert = Counter(entities_biobert)
    for word, count in counter_biobert.most_common(10):
        print(f"{word}: {count}")

    # Visualization of spaCy NER
    displacy.serve(spacy_doc, style="ent")

# Example usage
# file_path = 'your_text_file.txt'  # Replace with the path to your text file
file_path = r'C:\files\Class\softwarenoAssign\Soft_assignment\output1.txt'  # Replace with the path to your text file

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

spacy_model_name = 'en_core_sci_sm'  # Replace with the desired spaCy model
biobert_model_name = 'dmis-lab/biobert-base-cased-v1.1'  # Replace with the desired BioBERT model
compare_ner_results(text, spacy_model_name, biobert_model_name)
