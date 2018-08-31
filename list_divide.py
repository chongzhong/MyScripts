#coding=utf-8
# 对一批数据，已经分出来了多个文件夹，每个文件夹下面存放的是相同类别的图片
# 根据这些文件夹生成图片列表，划分为测试集和训练集数据
import os
import shutil
import  random

def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    if len(FileNames)>0:
        for fn in FileNames:
            if len(FlagStr)>0:
                if IsSubString(FlagStr,fn):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else:
                fullfilename=os.path.join(FindPath,fn)
                FileList.append(fullfilename)


    if len(FileList)>0:
        FileList.sort()

    return FileList

def spiltdata(path_root,valratio=0.15):
    classify_temp=os.listdir(path_root)
    classify_file=[]
    for c in classify_temp:
        classify_file.append(os.path.join(path_root,c))



    for f in classify_file:
        imgfiles=GetFileList(f)
    for c in classify_temp:
        imgfiles=os.listdir(os.path.join(path_root,c))
        nval=int(len(imgfiles)*valratio)
        print nval
        imgfvals=imgfiles[:nval]
    #测试数据文件列表
        for j in imgfvals:
            if os.path.exists(os.path.join(path_root+'/'+'val',c)) is False:
                os.makedirs(os.path.join(path_root+'/'+'val',c))
            newname=os.path.join(path_root+'/'+'val',c)+'/'+j
            oldname=os.path.join(path_root,c)+'/'+j
            shutil.move(oldname,newname)
    #训练数据文件列表
        imgftrains=imgfiles[nval:]
        for j in imgftrains:
            if os.path.exists(os.path.join(path_root+'/'+'train',c)) is False:
                os.makedirs(os.path.join(path_root+'/'+'train',c))
            newname=os.path.join(path_root+'/'+'train',c)+'/'+j
            oldname=os.path.join(path_root,c)+'/'+j
            shutil.move(oldname,newname)



def writetrainlist(path_root):
    classify_temp=os.listdir(path_root)#['cropblack','cropbrown','cropwhite','cropyellow']
    classify_file=[]
    for c in classify_temp:
        classify_file.append(os.path.join(path_root,c))
    for f in classify_file:
        imgfiles=GetFileList(f)

    sorted(classify_file)
    strlist=''
    for i,f in enumerate(classify_file):
        imgfiles=GetFileList(f)
        for image in imgfiles:
            print image
            strlist+=image+' '+str(i)+'\n'



    txtlist=open(path_root+'.txt','w')
    txtlist.write(strlist)
    txtlist.close()



'''spiltdata('../headangle/data')'''
# writetrainlist('../faceshape/data/train')
# writetrainlist('../faceshape/data/val')


#spiltdata('../hair/data')
#writetrainlist('../hair/data/train')
#writetrainlist('../hair/data/val')




writetrainlist('../data/train')
writetrainlist('../data/val')