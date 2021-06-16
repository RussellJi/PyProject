import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.core.protobuf.config_pb2 import ConfigProto
from tensorflow.python.client.session import InteractiveSession

config = ConfigProto() 
config.gpu_options.allow_growth = True 
session = InteractiveSession(config=config)


# 定义一个callback
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self,epoch,logs={}):
        if(logs.get('loss')<0.4):
            print("\nLoss is low so cancelling training!")
            self.model.stop_training = True

callbacks = myCallback()

# 数据集
fashion_mnist = keras.datasets.fashion_mnist
# 获取训练集和测试集的数据和标签
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

# 归一化
train_images_scaled = train_images/255
test_images_scaled = test_images/255

# 打印训练集和测试集的样本数量和大小
print(train_images.shape)
print(test_images.shape)

print(test_images[0])
# plt.imshow(test_images[0])
# 建立模型
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(128,activation=tf.nn.relu))
model.add(keras.layers.Dense(10,activation=tf.nn.softmax))
# 模型展示
model.summary()

# 配置模型
model.compile(optimizer=tf.optimizers.Adam(),loss=tf.losses.sparse_categorical_crossentropy,metrics=["accuracy"])
# model.fit(train_images,train_labels,epochs=5)
model.fit(train_images_scaled,train_labels,epochs=5,callbacks=[callbacks])
model.evaluate(test_images_scaled,test_labels)

np.argmax(model.predict(test_images/255)[0])
