from rembg import remove
from PIL import Image
import os


path_i = input('Enter a path')
os.chdir(rf'{path_i}')



def check_image(a):
    img_ext = ['.jpg', '.png', '.JPG', '.PNG', '.JPEG', 'jpeg']
    return os.path.splitext(a)[-1] in img_ext
for i, file in enumerate(os.listdir(path_i)):
    if not os.path.exists('removed'):
        os.mkdir('removed')
    if check_image(file):
        img_in = Image.open(file)
        img_out = remove(img_in)
        name  = file[:-4]+'bg_removed.png'
        img_out.save(f'./removed/{name}')
        print(f'./removed/{name}')