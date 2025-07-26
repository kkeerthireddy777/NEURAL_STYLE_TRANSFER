import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

# Load the pre-trained style transfer model
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Function to load and preprocess the image
def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, (256, 256))  # Resize for compatibility
    img = img[tf.newaxis, :]
    return img

# Load your content and style images
content_image = load_image('img.jpg')
style_image = load_image('monet.jpeg')

# Show style image
plt.imshow(np.squeeze(style_image))
plt.title("Style Image")
plt.axis('off')
plt.show()

# Generate stylized image
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

# Display the result
plt.imshow(np.squeeze(stylized_image))
plt.title("Stylized Output")
plt.axis('off')
plt.show()

# Save result
output_img = np.squeeze(stylized_image.numpy()) * 255
output_img = cv2.cvtColor(output_img.astype(np.uint8), cv2.COLOR_RGB2BGR)
cv2.imwrite('generated_img.jpg', output_img)
print("Stylized image saved as 'generated_img.jpg'")
