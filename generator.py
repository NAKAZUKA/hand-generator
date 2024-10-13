import time
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from keras_cv.models import StableDiffusion
from keras.models import load_model

model = load_model('generator_model.h5')
#model = StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image("palms", batch_size=3)
def plot_images(images):
     plt.figure(figsize=(20, 20))
     for i in range(len(images)):
         ax = plt.subplot(1, len(images), i + 1)
         plt.imshow(images[i])
         plt.axis("off")
plot_images(images)