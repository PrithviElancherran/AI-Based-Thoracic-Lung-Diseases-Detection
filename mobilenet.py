import numpy as np
import cv2
import pandas as pd
import PIL.Image as Image
import os
import matplotlib.pylab as plt
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

IMAGE_SHAPE = (224, 224)
X, y = [], []

df=pd.read_csv('C:\\Users\\prith\\Downloads\\train1.csv')
path='C:\\Users\\prith\\Downloads\\VIN-Train-jpeg\\'

for i,row in df.iterrows():
    img_path=path+str(row['image_id'])+'.jpeg'
    img = cv2.imread(img_path)
    resized_img = cv2.resize(img,(224,224))
    X.append(resized_img)
    y.append(row['class_id'])
X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
random_state=0)

X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

feature_extractor_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
pretrained_model_without_top_layer = hub.KerasLayer(feature_extractor_model, input_shape=(224, 224, 3),trainable=False)

num_of_diseases = 16

model = tf.keras.Sequential([pretrained_model_without_top_layer,tf.keras.layers.Dense(num_of_diseases)])
model.summary()
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['acc']
    )

model.fit(X_train_scaled, y_train, epochs=7)
print("Training Done")
model.evaluate(X_test_scaled,y_test)
model.save("model.h5")