import os


while True or not 'q':
    path = input('Enter any path please: ')
    os.chdir(rf'{path}')
    num_input = int(input('Enter text u want to rename: '))
    file_format = input('Enter format or enter for default jpg: ')
    #rename_text = input('Enter text u want to rename')
    for file in os.listdir(path):
        if file_format == "":
            file_format = ".jpg"
        new_name = file[:-4] + "-" + str(num_input) + file_format
        print(new_name)
        os.rename(file, new_name)
        num_input += 1
