import os
import glob
import string
import random
from PIL import Image,ImageDraw,ImageFont

class i:
    def checker():
        try:
            if os.path.exists('captcha-output') and os.path.exists('captcha-output/pool.py'): 
                return True
        except FileNotFoundError: 
                return False

x = i
ldrs = ['captcha-images/templates/*.jpeg','captcha-images/templates/*.png']

def random_picture(): 
    if x.checker and ldrs:
        images = glob.glob(random.choice(ldrs))
        randompict = random.choice(images)
    elif not images or randompict:
        return
    return randompict

def random_seed(amount):
    if not amount and type(amount) != 'int':
        return
    chars = string.ascii_letters + string.digits
    return ''.join(
        random.choice(chars)
        for i in range(amount))

def generate_captcha(txt, output, font):
    if random_picture and (txt and output and font):
        img = Image.open(f"{random_picture()}")
        d1 = ImageDraw.Draw(img)
        fq = ImageFont.truetype(font, 50)
        d1.text((15,15), txt, (237, 230, 211), font=fq)
    return img.save(
        output,optimize=True, quality=50
    )

captchaid = random_seed(5)

generate_captcha(captchaid,f'captcha-images/captcha-output/{captchaid}.png','fonts/EraserDust-p70d.ttf')
print(captchaid + ' was generated!')
