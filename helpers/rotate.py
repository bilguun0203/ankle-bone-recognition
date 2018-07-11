from os import listdir
from os.path import isfile, join


path = '/mnt/data/Bilguun/Documents/hicheel/Other/DeepLearningUB2018/project/dataset/images/'
files = [f for f in listdir(path) if isfile(join(path, f))]


import PIL
from PIL import Image, ExifTags

for f in files:
    path = 'dataset/images/'+f
    try:
        image=Image.open(path)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(image._getexif().items())

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
        image.save('dataset/images_new/'+f)
        image.close()

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass