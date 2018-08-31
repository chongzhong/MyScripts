import caffe
import net.base as base
from net.comb.res_cf_unit import *

def get_net(data, label, num_classes):

    n = caffe.NetSpec()
    n.data = data
    n.bn_data = base.batch_norm(n.data, in_place=False)
    n.sc_data = base.scale(n.bn_data, bias_term=True, in_place=False)

    n.conv1 = base.conv(n.sc_data, 16, 5, 1, 2)

