#coding=utf-8

import sys 
#import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 输入日志路径log或者txt格式，输出图片的路径png格式
log_path = sys.argv[1]
fig_path = sys.argv[2]
f = open(log_path, 'r')
accuracy = []
mbox_loss = []
detection_eval = []

# 初始化
max_iter = 0
test_iter = 0
test_interval = 0
display = 0
# 日志中的关键字符
# 通过索引关键字符，提取相应的值会便利一些
""
key_str = ['accuracy = ',
           'Test net output #0: detection_eval = ',
           'Train net output #0: mbox_loss = ',
           'max_iter: ',
           'test_iter: ',
           'test_interval: ',
           'display: ']

# 应该有简洁一点的方法
while True:
    line = f.readline()
    if len(line) < 1:
        break
    for i in range(len(key_str)):
        str = key_str[i]
        index = line.find(str)
        if index != -1:
            num = float(line[index + len(str):index + len(str) + 5])
            if i == 0:
                accuracy.append(num)
            if i == 1:
                detection_eval.append(num)
            if i == 2:
                mbox_loss.append(num)
            if i == 3:
                max_iter = float(line[index + len(str):])
            if i == 4:
                test_iter = float(line[index + len(str):])
            if i == 5:
                test_interval = float(line[index + len(str):])
            if i == 6:
                display = float(line[index + len(str):])
            else:
                pass
f.close()
print max_iter
print test_iter
print test_interval
print len(accuracy), len(detection_eval), len(mbox_loss)

_, ax1 = plt.subplots()
ax2 = ax1.twinx()
# 保持不错的想法
# 绘制train_loss曲线，颜色‘g'
ax1.plot(display*np.arange(len(mbox_loss)), mbox_loss, color='g', label='mbox_loss', linestyle='-')
# 绘制test_loss曲线，颜色'y'
ax2.plot(test_interval*np.arange(len(detection_eval)), detection_eval, color='y', label='detection_eval', linestyle='-')
# 绘制accuracy曲线，颜色'r'
#ax2.plot(test_interval*np.arange(len(accuracy)), accuracy, color='r', label='accuracy', linestyle='-')

# 设置标签
ax1.legend(loc=(0.7,0.8))
ax2.legend(loc=(0.7,0.72))
ax1.set_xlabel('iterations')
ax1.set_ylabel('loss')
ax2.set_ylabel('map')
# 像素的选择
plt.savefig(fig_path, dpi=100)
# plt.show()

