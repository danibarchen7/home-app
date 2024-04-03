import tensorflow as tf
from tensorflow.keras.preprocessing import image  # For image preprocessing
import numpy as np
from tensorflow.keras.applications.imagenet_utils import preprocess_input

# Load the model (replace with your model loading logic)
model = tf.keras.models.load_model('Images/house3.h5',compile=False)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(256, 256))  # Adjust size as needed
    x = image.img_to_array(img)
    x = np.expand_dims(x/255.0, axis=0)  # Add batch dimension
    x = preprocess_input(x)  # Apply model-specific preprocessing (if needed)
    return x

def predict_image_class(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions)  # Assuming one class output
    return predicted_class
