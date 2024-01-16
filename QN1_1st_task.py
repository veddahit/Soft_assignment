# print("hello s")
# # Open a file in write mode ('w')
# with open('example.txt', 'w') as file:
#     # Write content to the file
#     file.write('Hello, this is a text file created with Python!\n')
#     file.write('You can add more lines as needed.\n')

# print('Text file created successfully!')

# import csv

# # Specify the path to your CSV file
# csv_file_path = 'C:\files\Class\softwarenowfiles\csv1.csv'

# # Open the CSV file
# with open(csv_file_path, 'r') as file:
#     # Create a CSV reader object
#     csv_reader = csv.reader(file)

#     # Read and print each row in the CSV file
#     for row in csv_reader:
#         print(row)

# #######################################################################
import csv


csv_file_path = r'C:\files\Class\softwarenowfiles\csv1.csv'

column_name = 'SHORT-TEXT'


with open(csv_file_path, 'r') as file:
    
    csv_reader = csv.DictReader(file)

    
    column_values = [row[column_name] for row in csv_reader]
    print(f"{column_name} column values: {column_values}")
    
#######################################################################

import csv
import os


csv_directory = r'C:\files\Class\softwarenowfiles'
column_name = 'SHORT-TEXT'
# print(csv_directory)
# Output text file
output_txt_file = 'output1.txt'


def extract_text_from_csv(csv_file_path):
    texts = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
      
        column_values = [row[column_name] for row in csv_reader]
        print(f"{column_name} column values: {column_values}")      
    print(column_values)
    return column_values


def write_text_to_file(texts, output_file):
    # print(texts)
    with open(output_file, 'a') as file:
        for text in texts:
            # print(texts)
            file.write(text + '\n')


for filename in os.listdir(csv_directory):
    # print(filename)
    if filename.endswith('.csv'):
        csv_file_path = os.path.join(csv_directory, filename)
        print("file path is",csv_file_path)
        texts = extract_text_from_csv(csv_file_path)
        # print(texts)
        write_text_to_file(texts, output_txt_file)

print(f'Texts extracted from CSV files and stored in {output_txt_file}.')

