import os
from pathlib import Path
import shutil

#File Organiser Function
def File_Organiser(base_folder, File_Path):
    # initiate Dictionary to store Folder names with respect to Extension
    file_name = (Path(File_Path)).name  # without Extension (Path(File_Path).stem)
    # Get extension Only
    extension = File_Path.suffix

    ext_dict = {
        ".txt": "Text",
        ".jpg": "Image",
        ".pdf": "PDF",
        ".mp3": "Music",
        ".mp4": "Movies",
        ".zip": "Archives",
        ".xlsx": "Excel",
        ".png": "Screenshot"
    }
    try:
        #Check Extension is present in pre-defined list or not
        if extension not in ext_dict.keys():
            if File_Path.is_dir():
                return False, file_name, "Folder"
            else:
                return False, file_name, "Unknown File"
        else:
            base_dir = base_folder
            sub_dir = ext_dict[extension] + "_Folder"
            #Join Base Folder and Sub Folder
            new_folder = base_dir / sub_dir
            #Checks Folder is already present or not
            #We can use this also ->  new_folder.mkdir(exist_ok=True)
            if Path(new_folder).is_dir():
                pass
            else:
                # Create New Folder
                os.mkdir(new_folder)
            try:
                #Move the File from base to destination
                shutil.move(File_Path, new_folder)

                #print(f"{file_name} moved Successfully to the folder {new_folder}")
                return True, file_name, sub_dir
            except Exception as e:
                print(f"Error While Moving {e}")
                return False, file_name, extension

    except Exception as e:
        print(f"Error while checking the folder {e}")
        return False, file_name, extension

# Ask user to enter the folder path
folder_input = input("Enter the folder path: ")

# Go to input Folder
base_folder = Path(folder_input) #Eg: C:\Users\Pictures

#Get all the files
Files = [f for f in base_folder.iterdir() if f.is_file()]
Total_Files = len(Files)

#Create Empty Counts and List to store upcoming output
moved = 0
skipped = 0
skipped_files = []
moved_files = []

#Loop the file one by one
for File_Path in Files:
    #Call File Organiser Function
    status, file_name, folder = File_Organiser(base_folder, File_Path)
    if status:
        moved += 1
        moved_files.append(f"{file_name} -> {folder}")

    else:
        skipped += 1
        skipped_files.append(file_name)

#Print Summary details
print("\n" + "=" * 40)
print("          SUMMARY")
print("=" * 40)

print(f"\nTotal Files : {Total_Files}")

print("\nMoved Files")
print("-" * 20)
if moved_files:
    for file in moved_files:
        print(file)
else:
    print("None")

print("\nSkipped Files")
print("-" * 20)
if skipped_files:
    for file in skipped_files:
        print(file)
else:
    print("None")

print("\n" + "-" * 20)
print(f"Moved   : {moved}")
print(f"Skipped : {skipped}")
print("-" * 20)






