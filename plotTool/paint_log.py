from read_log import read
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_image')
    parser.add_argument('--y1', type=float, default=1.0, help="max loss y")
    parser.add_argument('--y2', type=float, default=1.0, help="max accuracy y")
    args = parser.parse_args()
    res = read(args.input_file)
    train_iter =[i['iters'] for i in res['loss']]
    train_iter = [sum(train_iter[i:i+10])/10 for i in range(len(train_iter) - 10)]
    train_loss = [i['loss'] for i in res['loss']]
    train_loss = [sum(train_loss[i:i+10])/10 for i in range(len(train_loss) - 10)]
    if 'accuracy' in res['train_output']:
        train_err = [ 1-i for i in res['train_output']['accuracy']]
        train_err = [sum(train_err[i:i+10])/10 for i in range(len(train_err) - 10)]
    train_iter = train_iter[:len(train_loss)]
    train_loss = train_loss[:len(train_loss)]

    test_iter = res['test_iter']
    test_loss = [i for i in res['test_output']['loss']]
    test_err = [ 1-i for i in res['test_output']['accuracy']]
    test_iter = test_iter[:len(test_err)]

    min_loss = min(test_loss)
    point_loss = test_loss.index(min_loss)
    min_err = min(test_err)
    point_err = test_err.index(min_err)

    _, ax1 =plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(train_iter, train_loss, 'y--', label='train loss')
    ax1.plot(test_iter, test_loss, 'b-', label='test loss')
    ax1.plot(test_iter[point_loss], min_loss, 'k*')

    if 'accuracy' in res['train_output']:
        ax2.plot(train_iter, train_err, 'r-', label='train error', linewidth=2.0)
    ax2.plot(test_iter, test_err, 'b-', label='test error', linewidth=2.5)
    ax2.plot(test_iter[point_err], min_err, 'k*')

    ax1.set_xlabel('Iteraion')
    ax1.set_ylabel('Loss')
    ax1.legend(loc='upper center')
    ax2.set_ylabel('Error')
    ax2.legend(loc='upper right')
    ax1.set_ylim(0, args.y1)
    ax2.set_ylim(0.0, args.y2)
    plt.title('Best test error %s' % (min(test_err)))
    plt.savefig(args.output_image)
