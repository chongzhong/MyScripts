import sys

import cv2
import caffe

if __name__ == '__main__':

    deploy_file = sys.argv[1]
    caffemodel_file = sys.argv[2]
    image_file = sys.argv[3]

    im = cv2.imread(image_file, 0)
#    im = cv2.resize(im, (28,28))
    # import pdb; pdb.set_trace()
    print im.shape

    im_in = im.astype('float32') / 256.
    net = caffe.Net(deploy_file, caffemodel_file, caffe.TEST)

    net.blobs['data'].data[...] = im_in
    out = net.forward()
    prob =  out['prob'][0]
    print prob.argmax(), prob
