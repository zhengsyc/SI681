# Improting Image class from PIL module 
from PIL import Image
import glob
import os
from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt


PATH_IMG = 'E:\\2021WIN\\SI681\\Decorrelated-Adversarial-Learning'
SRC = 'train'
DEST = 'train_crop'
dir_list = glob.glob(PATH_IMG + '\\' + SRC + '\\' + '*')
dir_name = [x.split('\\')[-1] for x in dir_list]

for dir in dir_name:
    try:
        os.makedirs(PATH_IMG + '\\' + DEST + '\\' + dir)
    except:
        print(dir + "existed")
    list_paths = glob.glob(PATH_IMG + '\\' + SRC + '\\' + dir + '\\' + '*.jpg')
    list_files_name = [x.split('\\')[-1] for x in list_paths]
    count = 0
    for file in list_files_name:
        # Opens a image in RGB mode
        image_path = PATH_IMG + '\\' + SRC + '\\' + dir + '\\' + file
        im = Image.open(image_path)
        try:
            img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        except:
            continue
        detector = MTCNN()
        detections = detector.detect_faces(img)
        # print(detections[0]['box'])
        if len(detections) < 1:
            continue
        if count == 6:
            break
        x, y, width, height = detections[0]['box']

        left = detections[0]['box'][0]
        right = left + detections[0]['box'][2]
        top = detections[0]['box'][1]
        bottom = top + detections[0]['box'][3]

        if detections[0]['box'][2] / detections[0]['box'][3] < 112 / 96:
            # width < height
            delta = 112 * detections[0]['box'][3] / 96 - detections[0]['box'][2]
            left -= delta / 2
            right += delta / 2
            # print("width < height: {}".format(delta))
        elif detections[0]['box'][2] / detections[0]['box'][3] > 112 / 96:
            delta = detections[0]['box'][2] - 112 * detections[0]['box'][3] / 96
            top -= delta / 2
            bottom += delta / 2
            # print("width > height: {}".format(delta))

        im = Image.open(image_path)
        im1 = im.crop((left, top, right, bottom))
        newsize = (112, 96)
        im1 = im1.resize(newsize)
        im1.save(PATH_IMG + '\\' + DEST + '\\' + dir + '\\' + file)
        count += 1
