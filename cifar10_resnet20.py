from net.comb.res_cf_uint import *
import net.base as base
import caffe

def get_net(data, label, num_classes):

    n = caffe.NetSpec()
    n.data = data # 3x24x24
    n.bn_data = base.batch_norm(n.data, in_place=False)
    n.sc_data = base.scale(n.bn_data, bias_term=True, in_place=False)

    n.conv1 = base.conv(n.sc_data, 16, 5, 1, 2) # 16x24x24
    n = res_cf(n, "conv1", "unit1", 16) # 16x24x24
  
    n = res_cf_samp(n, "unit1_elt", "unit2", 32) # 32x12x12
    n = res_cf(n, "unit2_elt", "unit3", 32) #32x12x12

    n = res_cf_samp(n, "unit3_elt", "unit4", 64) #64x6x6
    n = res_cf(n, "unit4_elt", "unit5", 64) # 64x6x6
    n = res_cf(n, "unit5_elt", "unit6", 64) # 64x6x6

    n.avg_pool = base.pool(n.unit6_elt, method='ave', 
            is_global=True)
    n.drop = base.dropout(n.avg_pool, in_place=True)

    n.fc = base.ip(n.drop, num_classes)
    if label is None:
        n.prob = base.softmax(n.fc)
    else:
        n.label = label
        n.loss = base.softmax_with_loss(n.fc, n.label)
        n.accuracy = base.accuracy(n.fc, n.label)
    return n
