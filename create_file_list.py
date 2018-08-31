# coding=utf-8

import os 
import sys

def creat_file_list(imagePath, fileName = 'list.txt', withLabel = True, ext = ['jpg','png','bmp']):
    "imagePath：图片的顶层目录
     withLabel：默认有label，且图片所在目录就是label
     ext：可以选择多种图片格式
    "
    if not os.path.exists(imagePath):
        print "应该会报错吧"
    # 对路径做递归操作
    elif os.path.isdir(imagePath):
        subPath = os.listdir(imagePath)
        subPath = [os.path.join(imagePath, path) for path in subPath]
        for path in subPath:
            creat_file_list(path, fileName, withLabel)
    # 不是目录的话，则直接是图片的路径
    else:
        if imagePath[-3:] in ext:
            f = open(fileName, 'a')
        if withLabel:
            line = imagePath + ' ' + (imagePath.split('/'))[-2] + '\n'
        else:
            line = imagePath + '\n'
        f.writelines(line)
        f.close()

if __name__ == "__main__":
    imagePath = sys.argv[1]
    fileName = sys.argv[2]
    creat_file_list(imagePath, fileName, True)

