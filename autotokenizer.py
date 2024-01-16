# from transformers import AutoTokenizer
# from collections import Counter
# import string

# def count_and_display_top_tokens(text_file_path, model_name, top_n=30):
#     # Read the content of the text file
#     with open(text_file_path, 'r', encoding='utf-8') as file:
#         text = file.read()

#     # Remove punctuation and convert to lowercase
#     translator = str.maketrans('', '', string.punctuation)
#     text = text.translate(translator).lower()

#     # Initialize the Auto Tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(model_name)

#     # Tokenize the text
#     tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))

#     # Count occurrences of each token
#     token_counts = Counter(tokens)

#     # Display the top N tokens
#     top_tokens = token_counts.most_common(top_n)
#     for token, count in top_tokens:
#         print(f'{token}: {count} times')

# # Specify the path to your text file
# # text_file_path = 'your_text_file.txt'
# text_file_path = r'C:\files\Class\Software now\Assignment sof\assignments\output1.txt'


# # Specify the pre-trained model name (e.g., 'bert-base-uncased')
# model_name = 'bert-base-uncased'

# # Count and display top tokens
# count_and_display_top_tokens(text_file_path, model_name, top_n=30)

import spacy
import torch 
from transformers  import AutoTokenizer, AutoModel

#loading spacy model

nlp_sci_sm = spacy.load('en_core_web_sm')

#load the BioBert model

model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

#reading text file

file_path = ""
with open(file_path, 'r',encoding='utf-8') as file:
    text = file.read()

    #extracting disase entities using en_core_sci_sm

doc_sci_sm = nlp_sci_sm(text)
diseases_sci_sm = [ent.text for ent in doc_sci_sm.ents if ent.label_ == "DISEASE"]

#EXTRACTING DISEASE AND DRUG ENTITIES USING BIOBERT

inputs = tokenizer.encode_plus(text, return_tensors='pt')
input_ids = inputs['input_ids']
attention_mask = input['attention_mask']
outputs = model(input_ids, attention_mask= attention_mask)
predicted_labels=torch.argmax(outputs.logits, dim=1)[0]
predicted_entities = [tokenizer.decode(input_ids[0][1] )for i, label in enumerate(predicted_labels) if label.item() ==1 ]



#filtering out diseases and drugs entities from BioBERT prediction
diseases_biobert =[entity for entity in predicted_entities if entity in diseases_sci_sm]
drugs_biobert = [entity for entity in predicted_entities if entity not in diseases_sci_sm]

#compare the results
total_entities_sci_sm = len(diseases_sci_sm)
total_entities_biobert = len(predicted_entities)
common_entities = set (diseases_sci_sm) & set(predicted_entities)

print("total disease entities detected by en_core_sci_sm", total_entities_sci_sm)
print("total disease and drug entities detected by Biobert:", total_entities_biobert)
print("Number of common entities detected by both models:", len(common_entities))
print("Most common disease and srug entities:", common_entities)
