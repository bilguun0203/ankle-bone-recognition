"""
Labelbox .json file to annotations.csv and validation.csv
"""

import json
from random import random

validation_data = True
validation_percent = 0.3

with_url = False

with open('data.json') as f:
    data = json.load(f)

annotations = open('../ankle_bones_dataset/annotations.csv', 'w')

if validation_data:
    validations = open('../ankle_bones_dataset/validations.csv', 'w')

for d in data :
    for i in d['Label']:
        if d['Label'] != 'Skip':
            for dd in d['Label'][i]:
                line_split = d["Labeled Data"].strip().split('/')
                x1 = dd['geometry'][0]['x'] if dd['geometry'][0]['x'] < dd['geometry'][2]['x'] else dd['geometry'][2]['x']
                y1 = 225 - (dd['geometry'][0]['y'] if dd['geometry'][0]['y'] > dd['geometry'][2]['y'] else dd['geometry'][2]['y'])
                x2 = dd['geometry'][0]['x'] if dd['geometry'][0]['x'] > dd['geometry'][2]['x'] else dd['geometry'][2]['x']
                y2 = 225 - (dd['geometry'][0]['y'] if dd['geometry'][0]['y'] < dd['geometry'][2]['y'] else dd['geometry'][2]['y'])
                sline = ''
                if with_url:
                    sline += d["Labeled Data"] + ','
                sline += 'images/' + line_split[6] + ',' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + i + '\n'
                if validation_data:
                    if random() < validation_percent:
                        validations.write(sline)
                    else:
                        annotations.write(sline)
                else:
                    annotations.write(sline)

annotations.close()

if validation_data:
    validations.close()