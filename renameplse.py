import os


while True or not 'q':
    path = input('Enter any path please')
    os.chdir(rf'{path}')
    rename_text = input('Enter text u want to rename')
    for file in os.listdir(path):
        new_name = file[:-5] + rename_text + ".tiff"
        os.rename(file, new_name)
