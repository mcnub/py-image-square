###
import os
from PIL import Image

files = os.listdir('./in')
for file in files:
    filename, file_extension = os.path.splitext(file)

    if file_extension in ['.jpg', '.png']:
        img = Image.open('./in/' + file)
        size_h = 0
        size_w = 0

        if img.size[0] != img.size[1]:
            if img.size[0] > img.size[1]:
                size_w = img.size[0]
                size_h = img.size[0]
            else:
                size_w = img.size[1]
                size_h = img.size[1]

            offset_w = round((size_w / 2) - (img.size[0] / 2))
            offset_h = round((size_h / 2) - (img.size[1] / 2))

            new_img = Image.new('RGB', (size_w, size_h), color=(255,255,255,0))
            new_img.paste(img, (offset_w, offset_h))
            new_img.save('./out/' + file)
        else:
            img.save('./out/' + file)
