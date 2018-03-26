# coding:utf-8
# !/usr/bin/env python

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping

# load data
data = np.load("mnist.npz")
(X_train, y_train), (X_test, y_test) = data['arr_0']

print X_test.shape, X_train.shape

X_train = X_train.reshape(60000, 28, 28, 1).astype(np.float32)
X_test = X_test.reshape(10000, 28, 28, 1).astype(np.float32)

# 归一化
X_train = (X_train-127) / 127
X_test = (X_test-127) / 127

# one hot
nb_classes = 10
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()
model.add(Conv2D(16, (3, 3), strides=(1, 1), input_shape=(28, 28, 1), padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

model.add(Conv2D(8, (3, 3), strides=(1, 1), padding='same', activation='relu', kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
model.add(Flatten())

model.add(Dense(64, kernel_initializer='he_normal'))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))

optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-06)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

early_stop = EarlyStopping()
check_point = ModelCheckpoint(filepath="board_dir/4/weights-improvement-{epoch:02d}-{val_acc:.4f}.hdf5")
tb_cb = TensorBoard(log_dir='board_dir/4', write_images=1, histogram_freq=1)
# 设置log的存储位置，将网络权值以图片格式保持在tensorboard中显示，每个周期计算一次网络权值，每层输出值的分布直方图

model.fit(X_train, y_train, epochs=5, batch_size=16, verbose=1, validation_split=0.1,
          callbacks=[tb_cb, check_point, early_stop])

# save model
# load model

loss, accuracy = model.evaluate(X_test, y_test)
print 'Test loss:', loss, 'Accuracy:', accuracy

print 'predict probability:', model.predict(x=X_test[0:1])
print 'predict class:', model.predict_classes(x=X_test[0:1])
