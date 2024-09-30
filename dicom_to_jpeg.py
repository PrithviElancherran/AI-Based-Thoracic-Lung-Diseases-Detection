import os
import tensorflow as tf
import tensorflow_io as tfio

# Reading DICOM images

def read_dicom(path):
    image_bytes = tf.io.read_file(path)
    image = tfio.image.decode_dicom_image(
        image_bytes, 
        dtype = tf.uint16
    )
    
    image = tf.squeeze(image, axis = 0)
    
    image = tf.image.resize(
        image, 
        (500, 500), 
        preserve_aspect_ratio = True
    )
    
    image = image - tf.reduce_min(image)
    image = image / tf.reduce_max(image)
    image = tf.cast(image * 255, tf.uint8)
    
    return image

# Destination folder
destination = "E:\\VIN-Train-jpeg\\"
os.makedirs("train_jpeg", exist_ok = True)

# Source folder
source = "E:\\VinDr-CXR\\train\\"

for name in os.listdir(source):
    image = read_dicom(os.path.join(source, name))
    image = tf.io.encode_jpeg(
        image, 
        quality = 100, 
        format = 'grayscale'
    )
    
    name = name.replace(".dicom", ".jpeg")
    tf.io.write_file(os.path.join(destination, name), image)
