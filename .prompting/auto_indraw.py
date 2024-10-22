import os

# Define the header and file name
h1 = "Business Process and Continuous Improvement"
file_name = "index.md"

# Define the list of topics
topics = [
    'Enabling Business Process Improvement',
    'Exploring Business Process Automation',
    'Using Lean to Perfect Organizational Processes',
    'Using Lean to Improve Flow and Pull',
    'Using Lean to Reduce Waste and Streamline Value Flow',
    'Applying Value Stream Mapping in Lean Business',
    'Six Sigma Techniques for Improvement',
    'Basics of Process Mapping, 2nd Edition',
    'Lean Thinking: Banish Waste and Create Wealth in Your Corporation',
    'Creating a Lean Culture: Tools to Sustain Lean Conversions, Third Edition',
    'The Lean Strategy'
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
