
from transformers import AutoTokenizer
from collections import Counter

def count_and_display_top_tokens(file_path, model_name, max_sequence_length=512, top_n=30):
    # Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using the AutoTokenizer
    tokens = tokenizer.encode(text, max_length=max_sequence_length, truncation=True)

    # Convert the tokens back to words
    words = tokenizer.convert_ids_to_tokens(tokens)

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Display the top N words
    print(f"Top {top_n} unique words in the text:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

# Example usage
file_path = r'C:\files\Class\softwarenoAssign\Soft_assignment\output1.txt'  # Replace with the path to your text file

model_name = 'bert-base-uncased'  # Replace with the desired transformer model
count_and_display_top_tokens(file_path, model_name)
