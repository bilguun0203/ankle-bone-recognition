import csv
from os import listdir
from os.path import isfile, join


path = 'dataset/amaraa/images_300'
files = [f for f in listdir(path) if isfile(join(path, f))]

new_csv = open('images_300_a.csv', 'w')
new_write = csv.writer(new_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

new_write.writerow(['ImageURL'])

for f in files:
    new_write.writerow(['http://projects.bilguun.xyz/ankle_bone_recognition/dataset/images_300_a/'+f])