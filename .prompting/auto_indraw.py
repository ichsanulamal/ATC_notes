import os

# Define the header and file name
h1 = "Independence and Relationships"
file_name = "index.md"

# Define the list of topics
topics = [
    'Developing Personal Accountability',
    'Becoming Your Own Best Coach',
    'Creating a Solid Support Base through Peer Relationships',
    'Building a Circle of Connections for Networking Success',
    'Building a Win-win Relationship with Your Manager',
    'Being an Effective Team Member',
    'No More Excuses: The Five Accountabilities for Personal and Organizational Growth',
    'Five Keys to Powerful Business Relationships'
    
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
