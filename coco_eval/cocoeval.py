import json
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

annType = ['segm','bbox','keypoints']
annType = annType[1]

datadir = "/mnt/mfs3/lizhilong/data/coco"
annfile = "{}/annotations/instances_val2014.json".format(datadir)
cocoGt=COCO(annfile)
resfile = "result.json"
cocoDt=cocoGt.loadRes(resfile)
 
f = op
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imageIds
cocoEval.params.catIds = [1, 2, 3, 4, 6, 8]
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()


