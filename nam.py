import os

path = input("Path: ")
os.chdir(rf'{path}')
while(path!="q"):
    path = input("Path: ")
    os.chdir(rf'{path}')
    for file in os.listdir():
        new_name = file[:-5]+"©Marudhar Arts, India.tiff"
        print(new_name)
        os.rename(file, new_name)
