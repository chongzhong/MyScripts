#coding=utf-8
import os 
import lmdb
import cv2
import numpy as np

def checkImageIsValid(imageBin):
    if imageBin is None:
        return False
    imageBuf = np.fromstring(imageBin, dtype=np.uint8)
    
    # img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False
    width, height = img.shape[0], img.shape[1]
    if width * height == 0:
        return False
    return True


def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.iteritems():
            txn.put(k, v)


def createDataset(outputPath, imagePathList, labelList, lexiconList=None, checkValid=True):
    # 这里图片list和相应的label list分成了两个文件
    # 所以假定这两个list长度相等
    assert(len(imagePathList) == len(labelList))
    numImages = len(imagePathList)
    # 需要有足够大的缓存空间
    env = lmdb.open(outputPath, map_size=1099511627776) # 1TB的大小

    cache = {}
    cnt = 1
    for i in xrange(numImages):
        imagePath = imagePathList[i]
        label = labelList[i]
        if not os.path.exists(image_Path):
            print "%s 不存在" % imagePath
            continue
        with open(imagePath, 'r') as f:
            imageBin = f.read()
        if checkValid:
            if not checkImageIsValid(imageBin):
                print "%s 正常（不为空）" % imagePath
                continue


        '''
        lmdb数据库文件保存了两类数据，图片和标签数据，而且它们的key也不一样
        '''
        imageKey = "image-%09d" % cnt
        labelKey = "label-%09d" % cnt
        cache[imageKey] = imageBIN
        cache[labelKey] = label
        if lexiconList:
            lexiconKey = "lexicon-%09d" % cnt
            cache[lexiconKey] = ' '.join(lexiconList[i]
        if cnt % 1000 == 0:
            writeCache(env, cache)
            cache = {}
            print "写入%d / %d" % (cnt, numImages)
        cnt += 1
    numImages = cnt - 1
    cache['num-images'] = str(numImages)
    writeCache(env, cache)
    print "生成了数据库，数据来自 %d " % numImages)


def read_text(path):

    with open(path) as f:
        text = f.read()
    text = text.strip()

    return text 


import sys
import glob
if __name__ == '__main__':
    # 参数1：生成的lmdb数据的目录
    outputPath = sys.argv[1]
    # 图片的路径格式是这样的/data/*.jpg
    path = sys.argv[2]

    imagePathList = glob.glob(path)
    imageLabelLists = []
    for p in imagePathLists:
        try:
            imageLabelLists.append((p, read_text(p.replace('.jpg','txt'))))
        except:
            continue

    imageLabelLists = sorted(imageLabelLists,key = lambda x:len(x[1]))
    imagePaths = [p[0] for p in imageLabelList]
    txtLists = [p[1] for p in imageLabelList]

    createDataset(outputPath, imagePaths, txtLists, lexiconList=None, checkValid=True)


