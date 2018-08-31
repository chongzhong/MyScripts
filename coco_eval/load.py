from pycocotools.coco import COCO
import numpy as np
import json
import os

datadir = "/mnt/mfs3/lizhilong/data/coco"
datatype = "val2014"
annfile = "{}/annotations/instances_{}.json".format(datadir, datatype)

coco = COCO(annfile)

needs = ["person", "bicycle", "car", "motorcycle", "bus", "truck"]
catIds = coco.getCatIds(catNms=needs)
labelDict = dict(zip(needs, catIds))

imageIds = []

for catId in catIds:
    imgIds = coco.getImgIds(catIds=catId)
    imageIds.extend(imgIds)

imagesIds = set(imageIds)
print(len(imagesIds))
images = []
for Id in imagesIds:
    img = coco.loadImgs(ids=Id)
    file_name = img[0]["file_name"]
    width = img[0]["width"]
    height = img[0]["height"]
    per_target = {"image_id": Id,
                  "image_file": "{}/{}/{}".format(datadir, datatype, file_name),
                  "width": width,
                  "height": height}
    images.append(per_target)
   

