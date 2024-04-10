from PIL import Image
import os

mode = 'crop' # rename, crop
### set the directory to work with
print("""
#########################################################
########## Best Cropper For Coin images LOL !!###########
#########################################################
""")
path = input("Enter a path:\n")
os.chdir(rf'{path}')
img_ext = ['.jpg', '.png', '.JPG', '.PNG', '.JPEG', 'jpeg']


# print(os.listdir())
def is_image(file):
    return os.path.splitext(file)[-1] in img_ext
while path != 'quit':
    path = input("Enter a path:\n")
    os.chdir(rf'{path}')
    if mode == 'crop':
        for file in os.listdir():
            if not os.path.exists('crop'):
                os.mkdir('crop')
                os.mkdir('.\crop\Reverse')
                os.mkdir('.\crop\Obverse')
            if is_image(file):
                print(file)
                img = Image.open(file)
                width, height = img.size
                # obverse 
                top = 0
                left = 0
                right = (width / 2)
                right += 9
                bottom = height

                obv_img = img.crop((left, top, right, bottom))
                name_obv = f'Obverse_{file[0:-4]}'
                
                    
                obv_img.save(f'crop\Obverse\A_{name_obv}.png')

                # Reverse
                top = 0
                left = width/2
                left -= 5
                right = width
                bottom = height
                
                    
                name_rev = f'B_Reverse_{file[0:-4]}.png'
                rev_img = img.crop((left, top, right, bottom))
                rev_img.save(f'crop\Reverse\{name_rev}')
