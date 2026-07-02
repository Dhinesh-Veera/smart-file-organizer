# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""   if ".txt" in fileName:
        try:
            Text_Folder = r'C:\Users\Dhinesh Sangeetha\Pictures\Text_Folder'
            if Path(Text_Folder).is_dir():
                pass
            else:
                os.mkdir(Text_Folder)
            try:
                shutil.move(File_Path, Text_Folder)
                print((f"{fileName} moved Sucessfully to the folder {Text_Folder}"))
            except BaseException as e:
                print(f"Error While Moving {e}")

        except Exception as e:
            print(f"Error while checking the folder {e}")

    #Image Files
    if ".jpg" in fileName:
        try:
            Image_Folder = r'C:\Users\Dhinesh Sangeetha\Pictures\Image_Folder'
            if Path(Image_Folder).is_dir():
                pass
            else:
                os.mkdir(Image_Folder)
            try:
                shutil.move(File_Path, Image_Folder)
                print((f"{fileName} moved Sucessfully to the folder {Image_Folder}"))
            except BaseException as e:
                print(f"Error While Moving {e}")

        except Exception as e:
            print(f"Error while checking the folder {e}")
"""

Extension =[".txt", ".jpg", "pdf"]