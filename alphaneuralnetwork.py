# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:57:31 2020

@author: vinay
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dropout
classifier = Sequential()
classifier.add(Convolution2D(64,3,3,input_shape=(80,80,1),activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))
classifier.add(Convolution2D(64,3,3,activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(output_dim=100,activation='softmax'))
classifier.add(Dropout(0.5))
classifier.add(Dense(output_dim=35,activation='softmax'))
classifier.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
from keras.preprocessing.image import ImageDataGenerator
train=ImageDataGenerator(rescale=1./225,
                         shear_range=0.2,
                         zoom_range=0.2)
test=ImageDataGenerator(rescale=1./225)
train_set=train.flow_from_directory('train_set',
                                    target_size=(80,80),
                                    batch_size=34,
                                    color_mode='grayscale',
                                    class_mode='categorical')
test_set=test.flow_from_directory('test_set',
                                    target_size=(80,80),
                                    batch_size=4,
                                    color_mode='grayscale',
                                    class_mode='categorical',shuffle=False)
classifier.fit_generator(train_set,steps_per_epoch=326,
                         epochs=326,validation_data=test_set,validation_steps=45)
#CONFUSIN& CLASSIFICATION:
test_set.reset()
from sklearn.metrics import confusion_matrix,classification_report
import numpy as np
import pandas as pd
Y_pred5 = classifier.predict_generator(test_set)
y_pred6 = np.argmax(Y_pred5, axis=1)
df1=pd.Series(y_pred6)
print('Confusion Matrix')
print(confusion_matrix(test_set.classes,y_pred6))
print('Classification Report')
#target_names = [1,2,3,4,5'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(classification_report(test_set.classes,y_pred6,))

from keras.preprocessing import image
import cv2
img=cv2.imread('C:/Users/vinay/OneDrive/Pictures/folder/frame5.jpg',0)
img=cv2.resize(img,(28,28))
arr=image.img_to_array(img) 
arr1=np.expand_dims(arr,axis=0)
cl=classifier.predict(arr1)
y_pred10 = np.argmax(cl, axis=1)
