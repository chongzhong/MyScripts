#coding=utf-8

import json

image_dir = '/mnt/mfs3/lizhilong/data/Wider/WIDER_val/images/'
def load_txt(file):
    json_list = []
    f = open(file, "r")
    while True:
        line = f.readline()
        if len(line) < 1:
            break
        
        if line.find("jpg") != -1:
            
            path = line[:-1]
            image_path = image_dir + '/' + path
            num_faces = int(f.readline())
            l = []
            for i in range(num_faces):
                box = f.readline().split()
                box = map(int, box)
                face = "%s,%s,%s,%s" % tuple(box[:4])
                l.append({"face": face, 
                          "blur": box[4],
                          "expression": box[5],
                          "illumination": box[6],
                          "invalid": box[7],
                          "occlusion": box[8],
                          "pose": box[9]})
            d = {"persons": l,
                 "image_path": image_path}  
            json_list.append(d)

    f.close()
    with open("val.json", "w") as j:
        json.dump(json_list, j, indent=3)
        print "写入json完成..."

if __name__ == "__main__":
    file = '/mnt/mfs3/lizhilong/data/Wider/wider_face_split/wider_face_val_bbx_gt.txt'
    load_txt(file)
