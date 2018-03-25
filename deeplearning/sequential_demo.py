# coding:utf-8
# !/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import np_utils

# load data
data = np.load("mnist.npz")
(X_train, y_train), (X_test, y_test) = data['arr_0']

print X_test.shape, X_train.shape
plt.imshow(X_train[0])

X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)

# 归一化
X_train = (X_train-127) / 127
X_test = (X_test-127) / 127

# one hot
nb_classes = 10
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)

model1 = Sequential()
model1.add(Dense(512, input_shape=(784,), kernel_initializer='he_normal'))
model1.add(Activation('relu'))
model1.add(Dropout(0.2))

model1.add(Dense(512, kernel_initializer='he_normal'))
model1.add(Activation('relu'))
model1.add(Dropout(0.2))

model1.add(Dense(nb_classes))
model1.add(Activation('softmax'))

model1.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model1.fit(X_train, y_train, epochs=20, batch_size=64, verbose=1, validation_split=0.05)

loss, accuracy = model1.evaluate(X_test, y_test)
print 'Test loss:', loss, 'Accuracy:', accuracy
