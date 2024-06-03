import os
import shutil

def organize_files_by_type(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Dictionary to map file extensions to folder names
    file_types = {
        'TextFiles': ['.txt', '.doc', '.docx', '.pdf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Scripts': ['.py', '.js', '.sh'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        # Add more file types and corresponding folders as needed
    }

    # Create directories for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files into the corresponding directories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move files with unlisted extensions to an "Others" folder
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

    print("Files have been organized by type.")

# Example usage
directory_to_organize = "/path/to/your/directory"
organize_files_by_type(directory_to_organize)
    