#coding=utf-8

import os
import cv2
from numpy import *
import sys

img_dir = sys.argv[1]
img_list = os.listdir(img_dir)
R = 0
G = 0
B = 0
count = 0
# 可以设置resize大小
#img_size = sys.argv[2]
for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = cv2.imread(img_path)
  #  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  #  img = cv2.reszie(img, (img_size,img_size))
    R = R + img[:,:,2].mean()
    G = G + img[:,:,1].mean()
    B = B + img[:,:,0].mean()
    count += 1
# RGB的图片在ｏｐｅｎｃｖ中储存时ＢＧＲ格式
mean_R = R / count
mean_G = G / count
mean_B = B / count
img_mean = [mean_R, mean_G, mean_B]
print "RGB mean is {}".format(img_mean)

"""
import
"""
