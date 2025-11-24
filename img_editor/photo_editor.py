from PIL import Image, ImageEnhance,ImageFilter
import os

path = './imgs'
pathout = './editedimgs'

for filename in os.listdir(path):
    img = Image.open
