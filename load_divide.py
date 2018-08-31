# coding=utf-8
import json
import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

jsonlist = ["double.json", "single.json", "green_car.json"]
for f in jsonlist:
  target = json.load(f)
  for i in target:
    imagepath = i["path"]
    box = i["plates"][0]["box"]
    newbox = [box[0],box[1],box[0]+box[2],box[1]+box[3]]
    color = i["plates"][0]["color"]
    id = i["plates"][0]["id"]
    im = Image.open(imagepath)
    region = im.crop(newbox)
    if color == 1:
        try:
            region.save("3s/%s.jpg" % id)
        except SystemError:
            os.remove("3s/%s.jpg" % id)
    if color == 2:
        try:
            region.save("4s/%s.jpg" % id)
        except SystemError:
            os.remove("4s/%s.jpg" % id)
    if color == 3:
        try:
            region.save("1s/%s.jpg" % id)
        except SystemError:
            os.remove("1s/%s.jpg" % id)
    if color == 4:
        try:
            region.save("2s/%s.jpg" % id)
        except:
            os.remove("2s/%s.jpg" % id)
    if color == 5:
        try:
            region.save("0s/%s.jpg" % id)
        except SystemError:
            os.remove("0s/%s.jpg" % id)
    if color == 6:
        try:
            region.save("5s/%s.jpg" % id)
        except SystemError:
            os.remove("5s/%s.jpg" % id)
    if color == 7:
        try:
            region.save("6s/%s.jpg" % id)
        except SystemError:
            os.remove("6s/%s.jpg" % id)



import os
import shutil

dirlsit = [0, 1, 2, 3, 4, 5, 6]
for x in dirlsit:
    newtestpath = "/data/zhongchong/plate_color/test/%s" % x
    newtrainpath = "/data/zhongchong/plate_color/train/%s" % x
    imagelist = os.listdir("%s" % x)
    num = len(imagelist)
    partition =int(num/5)
    for i in range(0, partition):
        oldimage = "%s/%s" % (x, imagelist[i])
        shutil.copy(oldimage, newtestpath)
    for j in range(partition, num):
        oldimage = "%s/%s" % (x, imagelist[j])
        shutil.copy(oldimage, newtrainpath)
