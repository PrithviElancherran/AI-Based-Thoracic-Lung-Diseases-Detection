import numpy as np
import cv2
import pandas as pd
import PIL.Image as Image
import os
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
import matplotlib.pylab as plt
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from keras.models import load_model
from lime.lime_image import LimeImageExplainer
from skimage.segmentation import mark_boundaries

model = load_model('model.h5',custom_objects={'KerasLayer':hub.KerasLayer})
model.summary()

img = cv2.imread('C:\\Users\\prith\\Downloads\\VIN-Train-jpeg\\7c6f191b5d28bc1992e491d906f0d1a5.jpeg')
print(img.shape)
img1 = cv2.resize(img,(224,224))
print(img1.shape)
X = np.array([img1])
X=X/255

id_to_label = {
'Aortic enlargement':0,
'Atelectasis':1,
'Calcification':2,
'Cardiomegaly':3,
'Consolidation':4,
'ILD':5,
'Infiltration':6,
'Lung Opacity':7,
'Nodule/Mass':8,
'Other lesion':9,
'Pleural effusion':10,
'Pleural thickening':11,
'Pneumothorax':12,
'Pulmonary fibrosis':13,
'No finding':14,
'Pulmonary tuberculosis':15,
}

y=model.predict(X)
Id=np.argmax(y,axis=1)
print(ID)
print(id_to_label[ID])

y_pred = model.predict(X_test_scaled)
y_pred1 = np.argmax(y_pred, axis = 1)
print(y_pred1)

results = confusion_matrix(y_test,y_pred1)
print(results)