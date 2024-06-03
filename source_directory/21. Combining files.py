import os
def process_text_file(file_path, combined_file):
    file_name = os.path.basename(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
    if os.path.getsize(file_path) <= 120:
        combined_file.write(f"Filename: {file_name}\n")
        combined_file.write(f"Content: {content}\n\n")
def traverse_directory(directory, combined_file):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item.endswith('.txt'):
            process_text_file(item_path, combined_file)
        elif os.path.isdir(item_path):
            traverse_directory(item_path, combined_file)
source_directory = '/Users/dariasotnikova/Desktop/Python/QA/source_directory'
combined_file_path = os.path.join(source_directory, 'combined_files.txt')
os.makedirs(os.path.dirname(combined_file_path), exist_ok=True)
with open(combined_file_path, 'w') as combined_file:
    traverse_directory(source_directory, combined_file)