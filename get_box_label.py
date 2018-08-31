#coding=utf-8

import os
import cv2
import sys

image_dir = '/mnt/mfs3/lizhilong/data/Wider/WIDER_train/images/'
def load_bbx(txt_file):
    f = open(txt_file, "r")
    while True:
        line = f.readline()
        if len(line) < 1:
            break
        if line.find("jpg") != -1:
            path = line[:-1]
            image_path = image_dir + path
            image = cv2.imread(image_path)
            num_box = int(f.readline())
            for i in range(num_box):
                box = f.readline().split()
                box = map(int, box)
                # 在这插入处理图片的代码或函数
                draw(image=image, box=box)
            save(image=image, path=path)
    f.close()

def draw(image, box=[]):
    cv2.rectangle(image, (box[0],box[1]), (box[0]+box[2],box[1]+box[3]), (255, 0, 0), thickness=1)
    step = box[3] / 5
    x0 = box[0] + box[2]
    y0 = box[1]
    blur = str(box[4])
    expression = str(box[5])
    illumination = str(box[6])
    invalid = str(box[7])
    occlusion = str(box[8])
    pose = str(box[9])
    cv2.putText(image, blur, (x0,y0), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
    cv2.putText(image, expression, (x0,y0+1*step), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
    cv2.putText(image, illumination, (x0,y0+2*step), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
    cv2.putText(image, invalid, (x0,y0+3*step), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
    cv2.putText(image, occlusion, (x0,y0+4*step), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)
    cv2.putText(image, pose, (x0,y0+5*step), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1)


def save(image, path=''):
    root = '/mnt/mfs3/zhongchong/Wider/train_images/'
    a = path.split('/')
    traget_dir = root + a[0]
    if not os.path.exists(traget_dir):
        os.makedirs(traget_dir)
    save_name = root + path
    cv2.imwrite(save_name, image)

if __name__ == "__main__":
    labes = ["blur", "expression", "illumination", "invalid", "occlusion", "pose"]
    txt_file = '/mnt/mfs3/lizhilong/data/Wider/wider_face_split/wider_face_train_bbx_gt.txt'
    load_bbx(txt_file)
