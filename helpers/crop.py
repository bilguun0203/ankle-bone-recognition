from os import listdir
from os.path import isfile, join


path = 'dataset/bandikhuu/images_300/'
files = [f for f in listdir(path) if isfile(join(path, f))]

import PIL
from PIL import Image

for f in files:
    img = Image.open(path + f)
    w,h = img.size
    if h > 225:
        if f == 'b_img_111.jpg' or f == 'b_img_112.jpg' or f == 'b_img_113.jpg' or f == 'b_img_163.jpg' or f == 'b_img_210.jpg' or f == 'b_img_222.jpg' or f == 'b_img_050.jpg':
            img = img.crop((0, 40, w, 225+40))
        elif f == 'b_img_114.jpg' or f == 'b_img_115.jpg' or f == 'b_img_147.jpg' or f == 'b_img_148.jpg' or f == 'b_img_185.jpg' or f == 'b_img_206.jpg' or f == 'b_img_219.jpg' or f == 'b_img_220.jpg' or f == 'b_img_238.jpg' or f == 'b_img_255.jpg' or f == 'b_img_267.jpg' or f == 'b_img_270.jpg' or f == 'b_img_244.jpg' or f == 'b_img_250.jpg':
            img = img.crop((0, 30, w, 225+30))
        elif f == 'b_img_117.jpg' or f == 'b_img_131.jpg':
            img = img.crop((0, 50, w, 225+50))
        elif f == 'b_img_123.jpg' or f == 'b_img_122.jpg' or f == 'b_img_144.jpg' or f == 'b_img_145.jpg' or f == 'b_img_158.jpg' or f == 'b_img_178.jpg' or f == 'b_img_179.jpg' or f == 'b_img_192.jpg' or f == 'b_img_194.jpg' or f == 'b_img_195.jpg' or f == 'b_img_196.jpg' or f == 'b_img_211.jpg' or f == 'b_img_226.jpg' or f == 'b_img_228.jpg' or f == 'b_img_235.jpg' or f == 'b_img_276.jpg' or f == 'b_img_026.jpg' or f == 'b_img_051.jpg' or f == 'b_img_089.jpg' or f == 'b_img_090.jpg' or f == 'b_img_091.jpg' or f == 'b_img_105.jpg' or f == 'b_img_106.jpg':
            img = img.crop((0, 20, w, 225+20))
        elif f == 'b_img_149.jpg':
            img = img.crop((0, 90, w, 225+90))
        elif f == 'b_img_237.jpg':
            img = img.crop((0, 120, w, 225+120))
        else:
            img = img.crop((0, 60, w, 225+60))
    img.save('dataset/bandikhuu/a_images_' + str(300) + '/' + f)
