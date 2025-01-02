## 比较不同模型性能图像

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] 
# 模型性能数据
metrics = ['准确率', '召回率', 'AUC 值']
svm_scores = [0.9613, 0.9613, 0.5394]
rf_scores = [0.9613, 0.9613, 0.9852]
gbt_scores = [0.9695, 0.9695, 0.9963]

# 设置柱状图的位置和宽度
x = np.arange(len(metrics))  # 指标的位置
width = 0.2  # 柱状图的宽度

# 创建图形和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
rects1 = ax.bar(x - width, svm_scores, width, label='SVM', color='skyblue')
rects2 = ax.bar(x, rf_scores, width, label='随机森林', color='lightgreen')
rects3 = ax.bar(x + width, gbt_scores, width, label='GBT', color='salmon')

# 添加标签、标题和图例
ax.set_xlabel('指标')
ax.set_ylabel('分数')
ax.set_title('模型性能比较')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# 在柱状图上显示数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.4f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# 调整布局
plt.tight_layout()

# 保存为 PNG 图像
plt.savefig('model_performance_comparison.png', dpi=300)