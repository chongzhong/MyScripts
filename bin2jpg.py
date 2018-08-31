#coding=utf-8

import os
import cv2
import numpy as np
import pickle

# 新建文件夹
train_dir = "/data/zhongchong/cifar10/cifar10_train"
test_dir = "/data/zhongchong/cifar10/cifar10_test"
if os.path.exists(train_dir) == False:
    os.mkdir(train_dir)
if os.path.exists(test_dir) == False:
    os.mkdir(test_dir)

# 解压缩bin
def unpickle(file):
    fo = open(file, 'r')
    dict = pickle.load(fo)
    fo.close()
    return dict

def cifar10_jpg(file_dir):
    for i in range(1, 6):
        data_name = file_dir + '/' + "data_batch_" + str(i)
        jpg_dict = unpickle(data_name)

        for j in range(0, 10000):
            img = np.reshape(jpg_dict['data'][j],(3,32,32))
            img = img.transpose(1,2,0)
            picName = train_dir + '/' + str(jpg_dict['labels'][j]) + '_' + str(j+(i-1)*10000) + '.jpg'
            cv2.imwrite(picName, img)
    
    testName = file_dir + '/' + 'test_batch'
    test_dict = unpickle(testName)
    for i in range(0, 10000):
        img = np.reshape(test_dict['data'][i], (3,32,32))
        img = img.transpose(1,2,0)
        picName = test_dir + '/' + str(test_dict['labels'][i]) + '_' + str(i) + '.jpg'
        cv2.imread(picName, img)
    print "Done..."
    return

# label的对应关系
def label_name():
    label_name_dict = {
        'airplane':"0",
        'automobile':"1",
        'bird':"2",
        'cat':"3",
        'deer':"4",
        'dog':"5",
        'frog':"6",
        'horse':"7",
        'ship':"8",
        'truck':"9"
        }
    return label_name_dict


if __name__ == '__main__':
    file_dir = "/data/zhongchong/cifar10/jpgdata/cifar-10-batches-py"
    cifar10_jpg(file_dir)


