# Import required libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from flask import Flask, request, jsonify

# Load and preprocess the dataset
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Define the model architecture
model = keras.Sequential([
    layers.Flatten(input_shape=(32, 32, 3)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10)

# Create a Flask app
app = Flask(__name__)

# Class labels
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

@app.route('/predict', methods=['POST'])
def predict():
    image = np.array(request.json['image'])
    image = image.reshape((1, 32, 32, 3))
    predicted_probabilities = model.predict(image)
    predicted_class = np.argmax(predicted_probabilities)
    return jsonify({'predicted_class': class_names[predicted_class]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
