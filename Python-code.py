import os

def create_folder_structure():
    base_folder = 'MyFiles'
    folders = ['Documents', 'Pictures', 'Music']
    files = {
        'Documents': ['file1.docx', 'file2.docx'],
        'Pictures': ['pic1.jpg', 'pic2.jpg'],
        'Music': ['song1.mp3', 'song2.mp3']
    }
    
    # Create base folder
    os.makedirs(base_folder, exist_ok=True)
    
    # Create subfolders and add files
    for folder in folders:
        folder_path = os.path.join(base_folder, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        if folder in files:
            for file in files[folder]:
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'w') as f:
                    f.write('Some content')
    
    # Print folder structure
    print_folder_structure(base_folder)

def print_folder_structure(folder_path, indent=''):
    print(indent + folder_path)
    indent += '   '
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print_folder_structure(item_path, indent)
        else:
            print(indent + item)

# Call the function to create and print the folder structure
create_folder_structure()
