import os
import re
import pandas as pd
import cv2




path_t = 'data/tags'
images_path = 'data/imgs'


def txt_to_data(tags_path):
    number = os.path.basename(tags_path)
    number = os.path.splitext(number)[0]
    single_tag = []

    try:
        with open(tags_path,'r') as file:
            for line in file:
                line = re.sub(",", " ",line)
                for word in line.split():
                    single_tag.append(word.split('\n')) 

        file.close()
    except:
        pass

    return single_tag, number

def txt_processing():
    tags = {'name':[], 'tags':[]}
    for filename in os.scandir(path_t):
        tags_path=filename.path
        single_tag, number = txt_to_data(tags_path)
        tags['name'].append(number)
        tags['tags'].append(single_tag)
    return tags

def image_processing(images_path):
    images = {'image_num': [], 'image':[]}
    for img in os.listdir(images_path):
        image_num = os.path.basename(img)
        image_num = os.path.splitext(image_num)[0]

        pic = cv2.imread(os.path.join(images_path,img))
        pic = pic[50:, 50:]
        pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
        pic = cv2.resize(pic,(512,512))
        

        images['image_num'].append(image_num)
        images['image'].append(pic)
    return images




images = image_processing(images_path)
tags = txt_processing()

data = pd.concat(images, tags, axis = 1)
print(data)