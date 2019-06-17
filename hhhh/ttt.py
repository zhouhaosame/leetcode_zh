import tensorflow as tf
# 导入TensorFlow工具包并简称为tf
import pandas as pd
batch_size = 64
# 定义训练数据batch的大小

w1 = tf.Variable(tf.random_normal([76, 11], stddev = 1, seed = 1))
# 分别定义一二层和二三层之间的网络参数，标准差为1，随机产生的数保持一致
x = tf.placeholder(tf.float32, shape = (None, 76), name = 'x-input')
mode_list=tf.placeholder(tf.float32,shape=(None,11,12),name='mode-list')
# 只是占位，生成图的形式,表明不能更新。
y_ = tf.placeholder(tf.float32, shape = (None, 12), name = 'y-input')
# 输入为76个维度，即76个特征，输出为12列标签,声明数据类型float32，None即一个batch大小
# y_是真实的标签

a = tf.matmul(x, w1)
# matmul两个矩阵相乘，要满足矩阵相乘的行列，得到的还是矩阵
y = tf.matmul(a, mode_list)
# 定义神经网络前向传播过程
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = tf.clip_by_value(y, 1e-10, 1.0)))
# 这里的y_和y应该是一个二维数组，其中每行应该是一条训练数据的预测
# clip_by_value函数，输入一个张量A，把A中的每一个元素的值都压缩在min和max之间。
# tf.clip_by_value(A, min, max)，小于min的让它等于min，大于max的元素的值等于max。
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 定义损失函数和反向传播算法

# 产生128组数据
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]
# 将所有x1+x2<1的样本视为正样本，表示为1；其余为0
df = pd.read_csv("./train_processed.csv")
p_list=['p'+str(i) for i in range(67)]
df_p=df[p_list]
m_list=[]
X = df.values
Y
dataset_size = len(df)
# 创建会话来运行TensorFlow程序
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    # 初始化变量
    sess.run(init_op)
    
    print(sess.run(w1))
    # 打印出训练网络之前网络参数的值
    
    STEPS = 5000
    # 设置训练的轮数
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        # 每次选取batch_size个样本进行训练
        
        sess.run(train_step, feed_dict = {x: X[start:end], y_: Y[start:end]})
        # feed_dict,通过选取的样本训练神经网络并更新参数w1，其中字典的赋值只在当前函数中有用
        
        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict = {x: X, y_: Y})
            print("After %d training step(s),cross entropy on all data is %g" % (i, total_cross_entropy))
    # 每隔一段时间计算在所有数据上的交叉熵并输出，随着训练的进行，交叉熵逐渐变小
    
    print(sess.run(w1))
    print(sess.run(w2))
    # 打印出训练之后神经网络参数的值
