import re

def read(filename):
    loss = []
    with open(filename, 'r') as fin:
        string_buf = fin.read()
    pattern_loss = re.compile(r"Iteration (\d+) \(.+?\), loss = (\S+)")
    res_loss = pattern_loss.findall(string_buf)
    for iters, loss_value in res_loss:
        loss.append(dict(iters=int(iters), loss=float(loss_value)))

    pattern_test_iter = re.compile(r"Iteration (\d+), Testing net")
    test_iter = [int(i) for i in pattern_test_iter.findall(string_buf)]
    
    train_output = {}
    pattern_train_output = re.compile(r"Train net output #\d: (.+?) = (\S+)")
    train_res = pattern_train_output.findall(string_buf)
    for res in train_res:
        train_output.setdefault(res[0], []).append(float(res[1]))

    test_output = {}
    pattern_test_output = re.compile(r"Test net output #\d: (.+?) = (\S+)")
    test_res = pattern_test_output.findall(string_buf)
    for res in test_res:
        test_output.setdefault(res[0], []).append(float(res[1]))
    train_dis = loss[1]['iters'] - loss[0]['iters']
    test_dis = test_iter[1] - test_iter[0]
    return dict(loss=loss, test_iter=test_iter, train_dis=train_dis,
            test_dis=test_dis, train_output=train_output, 
            test_output=test_output)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    res = read(args.input_file)
    print 'train_dis', res['train_dis']
    print 'test_dis', res['test_dis']
    print 'train_output[loss3/loss3][0]', res['train_output']['loss3/loss3'][0]
    print 'test_output[loss3/top-1][-1]', res['test_output']['loss3/top-1'][-1]
