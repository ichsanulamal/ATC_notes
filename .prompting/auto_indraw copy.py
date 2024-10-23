import os

# Define the header and file name
h1 = "AIfDS Activate"
file_name = "index.md"

# Define the list of topics
topics = [
    'An Introduction to Generative AI Concepts',
    'Generative Modeling Foundations',
    'Getting Started with Large Language Models (LLMs)',
    'Exploring the Depths of Large Language Models in Generative AI',
    'Leveraging Generative AI for Business',
    'Artificial Intelligence and Machine Learning',
    'Deep Learning and Neural Networks',
    'An Introduction to GPT Models',
    'Considerations for Using AI Responsibly'
]

# Create the markdown content
markdown_content = f"# {h1}\n\n"
for item in topics:
    item_cleaned = item.replace(":", "")  # Remove colon
    markdown_content += f"- [[{item_cleaned}/index]]\n"  # Add the link format

# Write the markdown content to a file
with open(file_name, 'w') as md_file:
    md_file.write(markdown_content)

# Create folders for each topic
for item in topics:
    item_cleaned = item.replace(":", "")  # Remove colon for folder name
    os.makedirs(item_cleaned, exist_ok=True)  # Create folder

print(f"Markdown file '{file_name}' created and folders generated.")


import os

# Get the current working directory
current_directory = os.getcwd()

# Loop through all items in the current directory
for folder_name in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder_name)
    
    # Check if it is a directory
    if os.path.isdir(folder_path):
        # Create the two files
        raw_file_path = os.path.join(folder_path, 'raw.txt')
        index_file_path = os.path.join(folder_path, 'index.md')
        
        with open(raw_file_path, 'w') as raw_file:
            pass  # Create an empty raw.txt
        
        with open(index_file_path, 'w') as index_file:
            # Write the header to index.md
            index_file.write(f"# {folder_name}\n")
