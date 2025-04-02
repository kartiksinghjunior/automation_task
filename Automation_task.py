import os
import shutil

# Function to organize files based on extensions
def organize_files(directory):
    if not os.path.exists(directory):  # Check if the directory exists
        print("Invalid directory path.")
        return
    
    # File categories and their extensions
    categories = {  # Define categories and their associated file extensions
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi"],
        "Music": [".mp3", ".wav"]
    }
    
    # Create category folders if they don’t exist
    for folder in categories:  # Loop through each category
        os.makedirs(os.path.join(directory, folder), exist_ok=True)  # Create folders if not already present
    
    # Move files into respective folders
    for file in os.listdir(directory):  # Iterate through all files in the directory
        file_path = os.path.join(directory, file)  # Get the full path of the file
        if os.path.isfile(file_path):  # Check if it's a file (not a folder)
            for folder, extensions in categories.items():  # Match file extensions to categories
                if file.lower().endswith(tuple(extensions)):  # Check if the file matches any extension
                    shutil.move(file_path, os.path.join(directory, folder, file))  # Move the file to the category folder
                    print(f"Moved: {file} → {folder}")  # Log the move operation
                    break  # Stop checking other categories once a match is found
    
    print("File organization complete!")  # Indicate the process is complete

# Run script
if __name__ == "__main__":
    folder_path = input("C:\\Users\\theha\\Music): ").strip())  # Prompt user for the folder path
    organize_files(folder_path)  # Call the function to organize files
    print("script completed successfully !")  # Indicate the script has finished