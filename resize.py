from PIL import Image
import os

img_ext = ['.jpg', '.png', '.JPG', '.PNG', '.JPEG', 'jpeg']

height = 500

def is_image(file):
    return os.path.splitext(file)[-1] in img_ext

path = input("Enter path:\n")

while path != 'q':
    path = input("Enter path:\n")
    os.chdir(rf"{path}")
    
    for file in os.listdir():
        if not os.path.exists("resized"):
            os.mkdir("resized")

        if is_image(file):
            print(file)
            img = Image.open(file)
            width_img = height / img.height * img.width
            width_img = int(width_img)
            newimg = img.resize((width_img, height))
            newimg.save(f"./resized/{file}")

